##
#"""
#@file test_Park_defaultCheck
#@brief test to validate the default parking mode after system power ON
#@Steps
#1. Power On system
#2. select variation : 
#   Temprature - Low\Hi
#   light condition - day\night
#   Optional - Mositure, Foggy weather - need to research on camerae additional modes
#3. run validation check on the feature
#
#@details following check will be done, raise exception if one of below conditions violate
#1. If default Info Display not recive from display screen ; How? by comparing 'default image' to current image recieved 
#2. If RVC turn ON ; How? I assume Camera will be in standby mode, and can return its state to VCU
#3. if any feature wake up settings wasnt mathcing : RVC,InfoDisplay,VCU



# @author David Tsairi
# @date 11/17/2020
#"""


import math
import os
import sys
import numpy as np
import random as rnd
from collections import OrderedDict
import gm_carlib as clib
import gm_testlib as tlib




    

class test_Reverse_WheelAngleCheck(tlib.TestExec):
    def __init__(self,test):
        self.pc = clib.Car_PC()
        self.const = self.pc.const
        self.test = test
        self.test_status= True
        self.test_exec = tlib.TestExec(test)
        self.p = self.test_exec.p
        self.gVars = self.pc.gVars    
        self.logger = self.gVars.logger
        self.gVars.tests.append([self,None])
        
    
    #parse & print setting
    def setup(self):
        self.test_exec._test_Setup() 
        if self.test_exec.u.isdaylight:
            self.pc.set_night_mode_Off()
        else:
            self.pc.set_night_mode_On()   
            
            
        self.pc.enable_guidelines()    
        
        
    def set_testFail(self):
        if self.test_status:
            self.test_status = False
        return
    
    def get_test_status(self):
        return self.test_status
        
    def run(self):  
        try:
            
            
            self.test_exec.p.PrintStep()
            self.pc.change_gear_to_park ()              
            self.pc.w.set_steering_wheel_angle(self.test.settings["Wheel_angle"])
            self.pc.change_streaing_angle()
            self.pc.change_gear_to_reverse()
          
            
            
            
            if not self.pc.rvc.get_is_rvc_on():
                self.set_testFail()
                self.logger.info("ASSERT:RVC IS NOT IN CORRECT STATE")
            if  self.pc.display.get_Display() != self.pc.display.Reverse:
                self.set_testFail()
                self.logger.info("ASSERT:DISPLAY IS NOT IN CORRECT STATE")
                
            if self.pc.rvc.get_night_mode() and self.test_exec.u.isdaylight:
                self.set_testFail()
                self.logger.info("ASSERT:NIGHT-MODE ACTIVATE UNEXPECTEDLY")  
                
                
            if self.pc.vcu.get_streaing_angle()  != self.pc.w.get_angle()  :
                self.set_testFail()
                self.logger.info("ASSERT:GUIdelines CALCULATION ERROR")                  
                
                
                      
          
            self.logger.info("Test name:[{}]. Test Status:[{}].".format(self.__class__.__name__, "PASS" if self.get_test_status() else "FAIL"))
            
            self.test_exec.p.PrintStepSeparator()
        except :            
            self.logger.info("Unexpected error:[{}].".format(sys.exc_info()[0]))
                          
            
        
        finally:
            self.end()
        
    def end(self):
        self.pc.g.reset()
        self.pc.w.reset()
        self.pc.rvc.reset()
        self.pc.display.reset()
        self.pc.vcu.reset()
        if not self.get_test_status():
            if self.const.RAISE_EXECPTION:
                raise Exception ("TEST FAILED")
            else:
                return self.get_test_status()
        self.test_exec._test_teardown()
    
    
  
def test_package(): 
    gVars = tlib.globalVars()
    
   
    
    
    
    #variation 1: Room temperture , day time
    usecase_P2R_wheel_angle = tlib.test()   
    usecase_P2R_wheel_angle.testname = "usecase_gear_Park2Reverse"
    usecase_P2R_wheel_angle.settings["Temp"] = gVars.const.AMBIANT_TEMP
    usecase_P2R_wheel_angle.settings["IsDay"] = False
    usecase_P2R_wheel_angle.settings["Wheel_angle"] = 90
    usecase_P2R_wheel_angle.cycles = 1        
    test_Reverse_WheelAngleCheck(usecase_P2R_wheel_angle)
    
    
    #variation 1: Room temperture , day time
    usecase_P2R_wheel_angle = tlib.test()   
    usecase_P2R_wheel_angle.testname = "usecase_gear_Park2Reverse"
    usecase_P2R_wheel_angle.settings["Temp"] = gVars.const.AMBIANT_TEMP
    usecase_P2R_wheel_angle.settings["IsDay"] = False
    usecase_P2R_wheel_angle.settings["Wheel_angle"] = 270
    usecase_P2R_wheel_angle.cycles = 1        
    test_Reverse_WheelAngleCheck(usecase_P2R_wheel_angle)    
  
  
    
   
    
    
   
    #gVars.runSeriesOfTests()
       
    
  
   
  
    
    
#if __name__ == "__main__":
    #main()
   
    
