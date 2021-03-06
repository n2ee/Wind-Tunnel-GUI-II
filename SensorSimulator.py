#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 09:19:20 2017

@author: markm

SensorSimulator() generates fake sensor data, primarily for exercising the UI.
"""
import sys
import math
import time
import datetime
from queue import Queue
from PyQt5.QtCore import QThread

from SensorSample import SensorSample


class SensorSimulator(QThread):
    
    def __init__(self, tw, dataQ):
        QThread.__init__(self)
        self.dataQ = dataQ
        self.tw = tw
        
    def __del__(self):
        self.wait()
     
    def run(self):
        theta = 0
        dummySample = SensorSample()
        
        while (True):
            theta = (theta + 1) % 360 
            dummySample.volts = 4.5 + 0.5 * math.cos(math.radians(theta))
            dummySample.amps = abs(0.25 * math.sin(math.radians(theta)))
            dummySample.aoa = 500.0 + int(math.cos(math.radians(theta)) * 500)
            dummySample.airspeed = 500.0 + int(math.cos(math.radians(theta / 3)) * 500)
            dummySample.hotwire = 500.0 + int(math.cos(math.radians(theta / 3)) * 500)
            dummySample.drag = theta / 8
            dummySample.timestamp = datetime.datetime.now()
            self.dataQ.put_nowait(dummySample)
            if (self.tw == None):
                sampleDelay = 1.0 / 2.0
            else:
                sampleDelay = (1.0 / self.tw.outSampleRate.value())
                
            time.sleep(sampleDelay)
         

if __name__ == "__main__":
    testQ = Queue(16384)
    sensorSim = SensorSimulator(None, testQ)
    sensorSim.start()
    
    while (True):
        testSample = testQ.get(True)
        print (testSample)
        
        
    sys.exit(0)
