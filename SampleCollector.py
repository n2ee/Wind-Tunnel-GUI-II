#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 21:48:24 2017

@author: markm

Listens on the dataQ and collects samples arriving there. Feeds
samples to the display UI and/or writes to a file.


"""
import os
from pathlib import Path
from math import radians, cos, sin, sqrt

from PyQt5.QtCore import QThread, pyqtSignal

from TunnelConfig import TunnelConfig
from TunnelPersist import TunnelPersist
from ProcessedSample import ProcessedSample
from Filter import KalmanFilter, RollingAverageFilter

class SampleCollector(QThread):
    dataQ = None
    tunnelWindow = None
    saveSamples = False
    samplesToSave = 1
    f = None
    dragTare = 0.0
    updateLoadTare = False
    airspeedTare = 0
    updateAirspeedTare = False
    dumpInterval = 0
    persist = TunnelPersist()
    runConfigComment = ""

    updateWindow = pyqtSignal('PyQt_PyObject')

    def __init__(self, dQ):
        QThread.__init__(self)
        self.dataQ = dQ
        config = TunnelConfig()
        self.dragScaling = float(config.getItem("StrainGauges", "dragscaling"))

        self.voltsSlope = float(config.getItem("Volts", "slope"))
        self.voltsZero = float(config.getItem("Volts", "zero"))

        self.ampsSlope = float(config.getItem("Amps", "slope"))
        self.ampsZero = float(config.getItem("Amps", "zero"))
        self.shuntOhms = float(config.getItem("Amps", "shunt"))

        self.airspeedSlope = float(config.getItem("Airspeed", "slope"))
        self.airspeedLowerLimit = float(config.getItem("Airspeed",
                                                       "lowerlimit"))

        self.hotwireLowerLimit = float(config.getItem("Hotwire",
                                                       "lowerlimit"))

        self.hotwireZero = float(config.getItem("Hotwire", "zero"))
        self.hotwireSlope = float(config.getItem("Hotwire", "slope"))

        airspeedTare = self.persist.getItem("Airspeed", "Tare")
        if airspeedTare == None:
            self.airspeedTare = 0
        else:
            self.airspeedTare = int(airspeedTare)


    def __del__(self):
        self.wait()

    def doSave(self, destFile = Path(os.devnull), runName = "", config = "",
               comments = ""):
        try:
            self.runConfigComment = ', "' + \
                                    runName + '", "' + \
                                    config + '", "' + \
                                    comments + '"\n'

            if not destFile.is_file():
                self.f = open(destFile, "w")
                self.f.write(str(ProcessedSample.header()))
                self.f.write(", run name, configuration, comments\n")
                self.f.close()

            self.f = open(destFile, "a")
            self.saveSamples = True
        except IOError:
            print ("Could not open: ", destFile)
            self.saveSamples = False

    def setLoadTare(self):
        self.updateLoadTare = True

    def setAirspeedTare(self):
        self.updateAirspeedTare = True

    def getRunName(self):
        runNameText = self.persist.getItem("General", "RunName")
        if runNameText == None:
            runNameText = ""
        
        return (runNameText)

    def saveRunName(self, runNameText):
        self.persist.setItem("General", "RunName", runNameText)
            
    def getConfiguration(self):
        configText = self.persist.getItem("General", "Configuration")
        if configText == None:
             configText = ""
             
        return (configText)
    
    def saveConfiguration(self, configText):
        self.persist.setItem("General", "Configuration", configText)
            

    def dumpData(self, processedSample):
        if self.dumpInterval == 10:
            self.dumpInterval = 0
            print("V=%f, A=%f, as=%f, hw=%f, uncorrDrag=%f, drag=%f" \
                  % (processedSample.volts, processedSample.amps,
                     processedSample.airspeed, processedSample.hotwire,
                     self.uncorrectedDrag, processedSample.drag))
        else:
            self.dumpInterval += 1

    def run(self):
        # This method runs as its own thread, catching SensorSamples,
        # updating the GUI, processing data, and tossing it into a file
        # when asked to.

        dragFilter = RollingAverageFilter(10)
        airspeedFilter = RollingAverageFilter(10)
        hotwireFilter = RollingAverageFilter(20)
        
        drag = 0.0

        while (True):
            latestSample = self.dataQ.get(True)

            if (self.updateLoadTare):
                self.updateLoadTare = False
                self.dragTare = latestSample.drag

            if (self.updateAirspeedTare):
                self.updateAirspeedTare = False
                self.airspeedTare = int(latestSample.airspeed)
                self.persist.setItem("Airspeed", "Tare",
                                     str(self.airspeedTare))

            # Get the latest drag, adjust for tare
            netDragCounts = latestSample.drag - self.dragTare

            # Scale to taste
            volts = latestSample.volts * self.voltsSlope + self.voltsZero
            # Because of the A/D resolution and the small values of deltaVolts,
            # we may need to filter amps to smooth out the appearance on the
            # display.
            deltaVolts = latestSample.amps * self.ampsSlope + self.ampsZero
            amps = deltaVolts / self.shuntOhms

            # Scale the drag value
            self.uncorrectedDrag = netDragCounts * self.dragScaling
            
            # FIXME - Any drag corrections here?
            drag = self.uncorrectedDrag
                   
            # Compute actual airspeed
            asCounts = latestSample.airspeed
            asPressure = (asCounts - self.airspeedTare) / 1379.3
            try:
                airspeed = self.airspeedSlope * sqrt((asPressure * 144.0 * 2.0) / 0.002378) * 0.682
            except ValueError:
                # airspeedPressure went negative due to rounding errors
                airspeed = 0.0

            if (airspeed < self.airspeedLowerLimit):
                # Think of this as a high-pass brickwall filter
                airspeed = 0.0

            # Compute hotwire speed
            hotwireCounts = latestSample.hotwire
            hotwirePressure = (hotwireCounts - self.hotwireZero) / 1379.3

            try:
                hotwire = sqrt((hotwirePressure * self.hotwireSlope * 144.0  * 2.0) / 0.002378)
            except ValueError:
                # hotwirePressure went negative due to rounding errors
                hotwire= 0.0

            if (hotwire < self.airspeedLowerLimit):
                hotwire = 0.0

            # Generate filtered values
            fDrag = dragFilter.get_filtered_value(drag)
            fDragStdDev = sqrt(dragFilter.get_variance())
            fAirspeed = airspeedFilter.get_filtered_value(airspeed)
            fHotwire = hotwireFilter.get_filtered_value(hotwire)

            processedSample = ProcessedSample(volts,
                                              amps,
                                              (volts * amps),
                                              latestSample.airspeed,
                                              fAirspeed,
                                              fHotwire,
                                              fDrag,
                                              fDragStdDev,
                                              latestSample.timestamp)

            if (self.saveSamples):
                self.saveSamples = False
                # f is opened in doSave(), and remains open until
                # the requested samples are written here.
                self.f.write(str(processedSample) + self.runConfigComment)
                self.f.close()

            self.updateWindow.emit(processedSample)

            self.dumpData(processedSample)






