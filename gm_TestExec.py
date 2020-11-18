##


import math
import os
import numpy as np
import random as rnd
from collections import OrderedDict
import gm_carlib as clib
import gm_testlib as tlib




    

class test_Park_defaultCheck(tlib.TestExec):
    def __init__(self,test):
        self.pc = clib.Car_PC()
        self.test = test
        self.test_exec = tlib.TestExec(test)
        self.setup()
        self.run()
        self.end()
    
    #parse & print setting
    def setup(self):
        self.test_exec._test_Setup()  
        
    def run(self):        
        self.test_exec.p.PrintStep()
        self.pc.change_gear_to_park ()  
      
        
        assert not self.pc.rvc.get_is_rvc_on(),"ASSERT:RVC IS NOT IN CORRECT STATE"
        assert self.pc.display.get_Display() == self.pc.display.CarInfo,"ASSERT:DISPLAY IS NOT IN CORRECT STATE"
        
        print ("Test name",self.__class__.__name__,"pass")
        
        self.test_exec.p.PrintStepSeparator()
        
        
    def end(self):
        self.test_exec._test_teardown()
    
    
    
def main(): 
    usecase_gearPark_dfeault = tlib.test()   
    usecase_gearPark_dfeault.testname = "usecase_gearPark_dfeault"
    usecase_gearPark_dfeault.settings["Temp"] = 25
    usecase_gearPark_dfeault.settings["IsNight"] = False
    usecase_gearPark_dfeault.cycles = 1
    
    ISRANDOM = True
    test_1 = test_Park_defaultCheck(usecase_gearPark_dfeault)
    
  
  
  
    
    
if __name__ == "__main__":
    main()
   
    
