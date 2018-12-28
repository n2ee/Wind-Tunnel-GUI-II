#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:54:40 2017

@author: markm
"""
import datetime

class SensorSample(object):

    def __init__(self, volts = 0.0, amps = 0.0,
                 airspeed = 0.0, hotwire = 0.0, drag = 0.0,
                 timestamp = datetime.datetime.now()):
        self.volts = volts
        self.amps = amps
        self.airspeed = airspeed
        self.hotwire = hotwire
        self.drag = drag
        self.timestamp = timestamp

    def __repr__(self):
        return "volts: %f, amps: %f, airspeed: %f, " \
                "hotwire: %f, drag: %f, timestamp: %s" % \
            (self.volts, self.amps, self.airspeed,
             self.hotwire, self.drag, self.timestamp)        
        
if __name__ == "__main__":
    testSensor = [SensorSample(i / 10.0, i / 10.0, i, i/ 10.0, \
                               i / 10.0, i / 10.0, i / 10.0) \
                               for i in range(10)]

    for i in range(10):
        print (testSensor[i])
 
    print ("done")
    
