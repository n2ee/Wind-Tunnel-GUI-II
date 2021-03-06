#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:54:40 2017

@author: markm
"""
import datetime

class ProcessedSample(object):

    def __init__(self, volts = 0.0, amps = 0.0, watts = 0.0,
                 rawAirspeed = 0.0, airspeed = 0.0, hotwire = 0.0, 
                 liftLeft = 0.0, liftCenter = 0.0, liftRight = 0.0, 
                 totalLift = 0.0, totalLiftStdDev = 0.0, 
                 drag = 0.0, dragStdDev = 0.0, pitchmoment = 0.0,
                 pitchMomentStdDev = 0.0,
                 timestamp = datetime.datetime.now()):
        
        self.volts = volts
        self.amps = amps
        self.watts = watts
        self.rawAirspeed = rawAirspeed
        self.airspeed = airspeed
        self.hotwire = hotwire
        self.liftLeft = liftLeft
        self.liftCenter = liftCenter
        self.liftRight = liftRight
        self.totalLift = totalLift
        self.totalLiftStdDev = totalLiftStdDev
        self.drag = drag
        self.dragStdDev = dragStdDev
        self.pitchMoment = pitchmoment
        self.pitchMomentStdDev = pitchMomentStdDev
        self.timestamp = timestamp

    """
    Report the header fields, suitable for writing into a csv file.
    Note that the headers need to be kept in sync with the data fields
    reported by __repr__().
    """
    @staticmethod
    def header():
        return "Volts, Amps, Watts, Raw Airspeed, Airspeed MPH, " \
               "Hotwire MPH, LiftLeft Kg, LiftCenter Kg, LiftRight Kg, " \
               "TotalLift Kg, TotalLiftStdDev, " \
               "Drag Kg, DragStdDev, PitchMoment Kg-in, PitchMomentStdDev, " \
               "Timestamp"
               
    def __repr__(self):
        return "%f, %f, %f, " \
                "%f, %f, %f, " \
                "%f, %f, %f, " \
                "%f, %f, %f, " \
                "%f, %f, %f, %s" % \
            (self.volts, self.amps, self.watts,
             self.rawAirspeed, self.airspeed, self.hotwire, 
             self.liftLeft, self.liftCenter, self.liftRight, 
             self.totalLift, self.totalLiftStdDev, self.drag, 
             self.dragStdDev, self.pitchMoment, self.pitchMomentStdDev, 
             self.timestamp)        
        
if __name__ == "__main__":
    testSample = [ProcessedSample(i / 10.0, i / 10.0, i / 10.0, i / 10.0, i/ 10.0, \
                                  i/ 10.0, i / 10.0, i / 10.0, \
                                  i / 10.0, i / 1.0, i / 10.0, \
                                  i / 10.0, i / 1.0, i / 10.0, \
                                  i / 10.0, i / 10.0, i / 10.0, i) \
                    for i in range(10)]

    print (ProcessedSample.header())
    
    for i in range(10):
        print (testSample[i])
 
    print ("done")
    
