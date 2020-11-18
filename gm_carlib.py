import math
import os
import numpy as np
import random as rnd
from collections import OrderedDict
from gm_testlib import globalVars


               

          
                
#gear states:
#1: park
#2: Drive
#3: Reverse  
class gear(object):        
        def __init__(self,globalVar = globalVars):  
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.const = self.gVars.const
                self.gearDict ={"P":1,"D":2,"R":3}
                self.gearStates  = [1,2,3]                    
                self.P = "P"
                self.D = "D"
                self.R = "R"
                self.gear_modes = list()
                self.gear_modes.append(self.P)
                self.gear_modes.append(self.D)
                self.gear_modes.append(self.R)
                self.PrevGear = -1
                self.current_gear = self.P                
                self.isRandom = False
            
            
        def reset(self):
                self.PrevGear = -1
                self.current_gear = 1     
            
        def get_gear(self):
                return self.current_gear    
        
            
        def change_Gear(self,next_gear) : 
                if self.const.ISRANDOM:
                        if not rnd.choice[True,False]:
                                return False
                        
                        
                self.PrevGear = self.P
                if next_gear == self.current_gear:
                        return True
                elif next_gear in self.gear_modes:
                        self.PrevGear = self.current_gear
                        self.current_gear = next_gear
            
                else:
                        return False
                
                self.logger.info("change_Gear: Prev:[{}]-->New:[{}]".format(self.PrevGear,self.current_gear))
                
               
                              
                return True
            
            
              
#return angle to 0 after each set_stearing_angle            
class wheel(object):
        def __init__(self,globalVar = globalVars):
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.const = self.gVars.const
                self.angle = 0  
                self.isRight = None
            
        def reset(self):
                self.angle = 0  
                self.isRight = None
                
        def get_angle(self):
                return self.angle    
          
        
        
        # Sets the steering wheel angle to the give
        # degress paramter
        # Returns True if succeeded and False if failed.
        #
        def set_steering_wheel_angle(self,degrees):
                # Add "implementation" here
                self.angle = degrees 
                self.isRight = True if degrees < 180 else False
                self.logger.info("Wheel:set_stearing_angle:degrees[{}]. change to:[{}]".format(degrees,"RIGHT" if self.isRight else "LEFT"))       
               
                if self.const.ISRANDOM:
                        return rnd.choice[True,False]
                               
                return True   
        
class InfoDisplay(object):
        def __init__(self,globalVars = globalVars):
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.const = self.gVars.const
                self.radio = "Radio"
                self.Reverse = "RVC"
                self.CarInfo = "Info"
                self.Navigate = "Navigate"
                self.display_modes = list()
                self.display_modes.append(self.radio)
                self.display_modes.append(self.Reverse)
                self.display_modes.append(self.CarInfo)
                self.display_modes.append(self.Navigate)
                self.current_screen  = self.CarInfo
                self.prev_screen = -1 
                
        def reset(self):
                self.current_screen  = self.CarInfo
                self.prev_screen = -1                 
                
        
        def get_Display(self):
                self.logger.info("Get_display:[{}]".format(self.current_screen))
                return self.current_screen
        
        def set_display(self,next_screen):
                if next_screen == self.current_screen:
                        return True
                elif next_screen in  self.display_modes:
                        self.prev_screen = self.current_screen
                        self.current_screen = next_screen
                        
                else:
                        return False
                return True
        
        #merge guideline image on top of live image
        def add_guideline(self):
                # add implamentation
                self.logger.info("guidlines added")
                return True
        
        #Remove guideline image on top of live image
        def remove_guideline(self):
                # add implamentation
                self.logger.info("guidlines removed")
                return True        
                
        
class Night_Mode_sensor(object):
        def __init__(self,globalVars= globalVars):
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.const = self.gVars.const
                self.isdaytime = self._isdaytime() 
        def _isdaytime(self):
                self.isdaytime = rnd.choice([True,False])  
                #self.logger.info("night_mode_sensor:[{}]".format(self.isdaytime))
                
        def get_isdaytime(self):
                return self.isdaytime      
        
        def set_isdaytimeOn(self):
                self.isdaytime = True
                
        def set_isdaytimeOff(self):
                self.isdaytime = False                

class RVC (object):
        def __init__(self,isdaytime=True,globalVars= globalVars):
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.const = self.gVars.const
                self.isdaytime = isdaytime
                self.is_rvc_on = False
                self.enable_camera = True
                self._night_mode = False if self.isdaytime else True
                
        
        
        def _set_night_mode(self):
                if self.const.ISRANDOM:
                        if not rnd.choice([True,False]):
                                return  False
                
                self._night_mode = False if self.isdaytime else True  
                return True        
        
                
        def get_night_mode(self):
                self.logger.info("night_mode:[{}]".format(self._night_mode))
                return self._night_mode         
                
        def reset(self):
                self.is_rvc_on = False
                self.enable_camera = True   
                
        def get_is_rvc_on(self):
                self.logger.info("is_rvc_on:[{}]. enable_camera:[{}]".format(self.is_rvc_on,self.enable_camera))
                return self.is_rvc_on
                
                
        def set_rvc_on(self):
                if self.enable_camera:                        
                        if self.const.ISRANDOM:
                                if not rnd.choice[True,False]:
                                        return False  
                        self.is_rvc_on = True   
                return True   
            
        def set_rvc_off(self):
                if  self.is_rvc_on:
                        if self.const.ISRANDOM:
                                if not rnd.choice[True,False]:
                                        return False
                        
                        self.is_rvc_on = False   
                return True   
                            
     
        
        
        
class VCU(object):
        def __init__(self,globalVars=globalVars):
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.nsense = Night_Mode_sensor()
                self.rvc = RVC(isdaytime=self.nsense.get_isdaytime())
                self.display = InfoDisplay()    
                self.const = self.gVars.const            
                self.is_guideline_enable = False
                self.image_RVC = None
                self.image_Disaply = None
                self._stearing_angle= 0
                
                
        def reset(self):
                self.is_guideline_enable = False
                self.image_RVC = None
                self.image_Disaply = None 
                self._stearing_angle= 0
                
        
        #get complition from rvc for turn on the camera                
        def enter_reverse_mode(self):
                if self.rvc.enable_camera:
                        self.rvc.set_rvc_on()
                        self.display.set_display(self.display.Reverse)
                
        def exit_reverse_mode(self):
                if not self.rvc.set_rvc_off()  : return False
                if not self.display.set_display(self.display.prev_screen): return False
                return True
                
                
        def user_display_req(self,next_screen) :
                return self.display.set_display(next_screen)
        
        def __str__(self):
                self.logger.info("is_guideline_enable:[{}]. image_RVC: [{}]. image_Disaply:[{}]".format(self.is_guideline_enable,self.image_RVC,self.image_Disaply))
                
            
            
        def _rvc_snaphot(self):
                self.logger.info("run snapshot commant on RVC to get current image")
            
        def _infoDisaplay_snaphot(self):
                self.logger.info("run snapshot commant on Info-Disaply to get current image")        
    
        def set_enable_guideline(self):       
                self.is_guideline_enable = True
                
        def get_enable_guideline(self):       
                return self.is_guideline_enable               
            
        def reset_enable_guideline(self):       
                self.is_guideline_enable = False
            
        def get_image_from_RVC_snapshopt(self):
                return self._rvc_snaphot() 
        
        def get_image_from_Info_Disaplay_snapshopt(self):
                return self._infoDisaplay_snaphot()    
        
        def get_streaing_angle(self):
                return self._stearing_angle
        
        def set_strearing_angle(self,angle):
                if not int(angle):
                        return False
                
                assert(0<=int(angle) and int(angle)<= 360), "Unexpected angle recived"
                
                self._stearing_angle = angle
                
                return True
                        
                
        def calc_guidelines_angle(self):
                self.logger.info("calc and apply guidelines calculation: degress [{}]".format(self._stearing_angle))
                
                if self.get_enable_guideline():
                        self.display.add_guideline()
                else:
                        self.display.remove_guideline()   
                        
                return True        
                
    
        
        
        
                
    
        

class Car_PC(object):
        def __init__(self,globalVars = globalVars):
                #self.logger.info("Initialize CAR PC")
                self.gVars = globalVars()
                self.logger = self.gVars.logger
                self.const = self.gVars.const        
                self.g = gear()
                self.w = wheel()
                self.vcu = VCU()
                self.rvc = self.vcu.rvc
                self.display =self.vcu.display  
            
     
    
        # Changes the car gear to "Drive",
        # Returns True if succeeded and False if failed.
        def change_gear_to_drive(self):
                # Add "implementation" here
                if self.g.current_gear == self.g.R:
                        if not self.vcu.exit_reverse_mode(): return False                 
                if not self.g.change_Gear(self.g.D): return False
                 
        
        
        # Changes the car gear to "Park",
        # Returns True if succeeded and False if failed.
        def change_gear_to_park(self):
                if self.g.current_gear == self.g.R:
                        if not self.vcu.exit_reverse_mode(): return False                                
                if not self.g.change_Gear(self.g.P): return False
        
        
        # Changes the car gear to "Reverse",
        # Returns True if succeeded and False if failed.
        def change_gear_to_reverse(self):
                if not self.g.change_Gear(self.g.R) : return False
                if not self.vcu.enter_reverse_mode(): return False
                      
        
        
        # Enable the Guidelines in rear view camera screen,
        # Returns True if succeeded and False if failed.
        def enable_guidelines(self):
                # Add "implementation" here
                self.vcu.set_enable_guideline()
                return True
        
        
        # Disable the Guidelines in rear view camera screen,
        # Returns True if succeeded and False if failed.
        def disable_guidelines(self):
                # Add "implementation" here
                self.vcu.reset_enable_guideline()
                return True
        
        
        # Disable the rear view camera from working and sending
        # camera images.
        # Returns True if succeeded and False if failed.
        def disable_camera(self):
                # Add "implementation" here
                self.rvc.enable_camera = False
                return True
            
        
        # Enable the rear view camera to work and send
        # camera images.
        # Returns True if succeeded and False if failed.
        def enable_camera(self):
                # Add "implementation" here
                self.rvc.enable_camera = True
                return True
        
        
        def setDisaply(self, next_screen):
                return self.vcu.user_display_req(next_screen)
        
        
        #set light sensor , isDay = True\False, if False , RVC will be change to night mode and vise versa
        def set_night_mode_On(self):
                self.vcu.nsense.set_isdaytimeOn()
                self.vcu.rvc.isdaytime = False
                self.vcu.rvc._set_night_mode()
                
                
        #set light sensor , isDay = True\False, if False , RVC will be change to night mode and vise versa
        def set_night_mode_Off(self):
                self.vcu.nsense.set_isdaytimeOff()
                self.vcu.rvc.isdaytime = True   
                self.vcu.rvc._set_night_mode()
                
                
        def change_streaing_angle(self):
                self.vcu.set_strearing_angle(self.w.get_angle())
                self.vcu.calc_guidelines_angle()
                
                return True
                
                        
        
        
    
        
        
        # Returns a boolean value for whether the rear view camera image is displayed
        # on infotainment screen or not
        def is_rear_view_camera_displayed_on_screen(self,ref_image):
                # Add "implementation" here
                
                image_screen = self.vcu.get_image_from_Info_Disaplay_snapshopt()
                image_rvc = self.vcu.get_image_from_RVC_snapshopt()
                
                if self._compare_image(image_screen, ref_image) and self._compare_image(image_rvc, ref_image):
                        return True 
                
                return False
        
        
        def _compare_image(self,image1,image2):
                #add implamentation of comparing images , return True if match
                
                if self.const.ISRANDOM:
                        return rnd.choice([True,False])        
                else :
                        return True
