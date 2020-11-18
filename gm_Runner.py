##
#"""
#@file gm_Runner
#@brief Run series of registered Tests  
#@Steps
#1.None
##@details None
#1. None




# @author David Tsairi
# @date 11/17/2020
#"""


import math
import os
import sys
import datetime
import numpy as np
import random as rnd
from collections import OrderedDict
import gm_carlib as clib
import gm_testlib as tlib

#from gm_test_Park_defaultCheck import test_Park_defaultCheck
import gm_test_Park_defaultCheck
import gm_test_Drive_defaultCheck
import gm_test_Reverse_defaultCheck
import gm_test_DriveToReverse_defaultCheck
import gm_test_DToRToD_defaultCheck
import gm_test_DToRToP_defaultCheck
import gm_test_Reverse_WheelAngleCheck
import gm_test_Reverse_DisplayEqToRVC
import gm_test_Reverse_disCamera
import gm_test_Reverse_disCameraCycles




    
# add option to run as command line 
# select single variation or runAll variations for the targeted test
# future enhancment : load variations from JSON file
def main(): 
    gVars = tlib.globalVars()    
    gVars.tests = list()
    logger = gVars.logger
  
    
    
    
   
    
    #State Parking :  RVC OFF + Disply at desfult mode
    gm_test_Park_defaultCheck.test_package()
    
    #State Parking2Drive :  RVC OFF + Disply at desfult mode
    gm_test_Drive_defaultCheck.test_package()
    
    #State Parking2Reverse : RVC ON + Disaply at RVC mode
    gm_test_Reverse_defaultCheck.test_package()
    
    #State Drive2Reverse : RVC ON + Disaply at RVC mode
    gm_test_DriveToReverse_defaultCheck.test_package()
    
    #Exit Parking-->Drive-->Reverse-->Drive : RVC OFF + Disaply set to Previous mode [Info/Radio/Navigate], Previous Mode to be randomize
    gm_test_DToRToD_defaultCheck.test_package()
    
    #Exit Parking-->Drive-->Reverse-->Parking : RVC OFF + Disaply set to Previous mode [Info/Radio/Navigate], Previous Mode to be randomize
    gm_test_DToRToP_defaultCheck.test_package()
    
    #Change into different Wheel angle and compare to vcu guidelines calc angle, add Wheel angle as variation, Gear Park--> Reverse, Camera enabled.
    gm_test_Reverse_WheelAngleCheck.test_package()
    
    #Check rvc output is matching Display output, compare RVC, Disaply Vs. Predefined Images , for instanse: R.G.B (3 images), Ref_image abs path, can be added as variation
    gm_test_Reverse_DisplayEqToRVC.test_package()
    
    #check camera disable\enable
    gm_test_Reverse_disCamera.test_package()
    
    #check camera disable\enable with cycles
    gm_test_Reverse_disCameraCycles.test_package()    
    
    #check wheel angle show on display,Gear Park--> Reverse, Camera enabled , guidelines enable, How? compare image to referance image with same guideline angle    
    #Check wheel angle show on display according to guidlines enable\disable configuration  
    #check components statnd alone functionality : RVC , for example connectivity, Quality: check image noise , saturation, RGB separation ( need more data of how to do that)
    #check components statnd alone functionality : Info-Display, for example connectivity, touch screen options per screen mode, Quality: check image noise , saturation, RGB separation ( need more data of how to do that)
    #check components statnd alone functionality : Wheel-angle, for example connectivity, ( need more data of how to do that)
    #check components statnd alone functionality : VCU, for example connectivity,  ( need more data of how to do that)
    #Master Test : random any gear state, with mix on features disable\enables while, diffrent pre conditions
    #Guidleines check in various condition, for instanse : edge angles, stanind close to an object (need more data of feature operative work range)
    
    
   
    
    gVars.runSeriesOfTests()
       
    
  
   
  
    
    
if __name__ == "__main__":
    main()
   
    
