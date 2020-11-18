"""

"""

import random as rnd
import datetime
import os
import sys
import logging

#Future enhancment: Constans can be seperated to be per feature, so each feature has its own CONSTANS class
class constants(object):
    def __init__(self):
        self.ISRANDOM = False
        self.RVC_NIGHTMODE = True
        self.AMBIANT_TEMP = 25
        self.HIGH_TEMP = 55
        self.RAISE_EXECPTION = False
        self.DISPLAYMODE = ["Radio","RVC","Info","Navigate"]
        self.USERDISPLAYMODE = ["Radio","Info","Navigate"]
        self.RGB_IMAGES = ["RED","GREEN","BLUE"]
              


#singleton - allow only one instanse         
class globalVars(object):  
    _globalVars_instance_obj = None
    _globalVars_instance_obj_created = False        
    def __init__(self):
        if globalVars._globalVars_instance_obj_created :
            return
        globalVars._globalVars_instance_obj_created  = True
        super(globalVars,self).__init__()                
        self.const = constants()
        self.tests = list()
        #################################################################
        self.current_rep = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists('results'):
            os.makedirs('results')    
            
        self.filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')    
            
        self.file_name = self.filename +".log"   
        self.file_res_des = self.current_rep+"\\results\\"+self.file_name
        #################################################################
        self.logger = logging.getLogger('')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.file_res_des)
        sh = logging.StreamHandler(sys.stdout)
        #formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
        formatter = logging.Formatter('[%(asctime)s]  %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)        
        #################################################################
        
       
        
    
   
        
      
    def __new__(cls, *args, **kwargs):
        if not globalVars._globalVars_instance_obj:            
            globalVars._globalVars_instance_obj=  super(globalVars,cls).__new__(cls)
        return globalVars._globalVars_instance_obj                 

    #unction will also prints to logs,\
    #Varation details + Test name + test results ( + opetiona lwhich checker has failed, which one pass)                
    def runSeriesOfTests(self):
        tests = self.tests
        if len(tests) == 0:
            return
        #printUtils.PrintLineSeparator(self)
        self.logger.info("Number Of Tests to Run: [{}]".format(len(tests)))
        #printUtils.PrintLineSeparator(self)
        for i,(test,res) in enumerate(tests):
            self.logger.info("Run Test index [{}] out of [{}]. cycles: [{}]".format(i,len(tests),test.test.cycles))   
            for icycle in range(test.test.cycles):                
                if hasattr(test,'setup'):
                    res = test.setup()            
                if hasattr(test,'run'):
                    res = test.run()
                    tests[i][1] = res 
                self.logger.info("End Running Test index [{}] out of [{}]. cycle#: [{}]".format(i,len(tests),icycle+1))       
        self.logger.info("END Running Total Of: [{}]".format(len(tests)))        
                
                
    def _selectNextDisplay(self,current_screen):
        next_screen = rnd.choice(self.const.USERDISPLAYMODE)
        if next_screen == current_screen and next_screen != None:
            self._selectNextDisplay(current_screen)
        else:
            self.logger.info("get_next screen: [{}].".format(next_screen))
            return next_screen       
        
         

class utility(object):
    def __init__(self,globalVars = globalVars):
        #self.logger.info("initializa test utilities")
        self.gVars = globalVars()
        self.logger = self.gVars.logger
        self.const = self.gVars.const        
        self.temp = 25
        self.isdaylight = True
        self.cycles = 1

    def set_temp(self,temp):        
        self.temp = temp
        self.logger.info("set temprature: {} ".format(temp))

    def set_day_light_condition(self,isdaylight):        
        self.isdaylight = isdaylight
        self.logger.info("set_day_light_condition: [{}]".format(isdaylight))
                                                                
    def set_cycles(self,cycles=1):        
        self.cycles = cycles
        self.logger.info("set_cycles: [{}]".format(self.cycles))                                                                
        


class test(object):
    def __init__(self):
        self.testname = None
        self.cycles = 1
        self.settings = dict()
        self.settings["Temp"] = 25
        self.settings["IsDay"] = False








# allow only one einstanse of the test exceution 
class TestExec(object):
    def __init__(self,test):
        self.test = test
        self.u = utility()
        self.gVars = self.u.gVars
        self.logger = self.gVars.logger
        self.const = self.gVars.const  
        self.p = printUtils()       
        #self._test_Setup()
        #self._test_run()
        #self._test_teardown()


    # get test setting, parse and save them for use during run    
    #prints test variation
    #print settings
    def _test_Setup(self):
        #self.p.PrintLineSeparator() 
        self.print_test_configuration()
        self.u.set_temp(self.test.settings["Temp"])
        self.u.set_day_light_condition(self.test.settings["IsDay"])
       #self.u.set_cycles(self.test.cycles)
       
        # add configuraton set   
        #self.p.PrintLineSeparator()

        pass

    def print_test_configuration(self):       
        self.p.PrintTestObjective(self.test.testname)
        if len(self.test.settings)>0:
            for k, v in self.test.settings.items():
                self.logger.info("TestName:[{}]. [{} = {}].".format(self.test.testname,k,v))

    #test run 
    def _test_run(self):
        #self.p.PrintLineSeparator() 
        self.test

        pass

    #test teardown
    def _test_teardown(self):
        #self.p.PrintLineSeparator() 
        pass


class printUtils(object):
    def __init__(self, globalVars = globalVars):
        self.gVars = globalVars()
        self.logger = self.gVars.logger
        self.const = self.gVars.const 
        self.step = 0
        pass

    def PrintTestObjective(self, TestObjective):
        """
        This API will Print the Test Objective at the beginning of the testcase.

        @param TestObjective [str] Accepts the test Objective as a string

        @return None

        @code:
        	<PrintUtilsObj>.PrintTestObjective("
        	blah1
        	blah2
        	blah3
        	")

        	Prints:
        	********************************************************************************************************
        	*                                          TEST OBJECTIVE                                              *
        	* blah1                                                                                                *
        	* blah2                                                                                                *
        	* blah3                                                                                                *
        	********************************************************************************************************
        """
        lines = TestObjective.splitlines()
        maxLength =max(82, max([len(line) for line in lines ]) + 4)
        string = "*"*(maxLength+4)
        string += "\n"
        string += "* {0} *".format("TEST OBJECTIVE".center(maxLength))
        for line in lines:
            string += "\n* {0} *".format(line.ljust(maxLength))

        string +="\n"
        string += "*"*(maxLength+4)

        self.logger.info("\n{0}\n".format(string))

    def PrintStep(self):
        """
        This API will print the Step Number in a standard format.

        @param None

        @return None

        @code:
        	<PrintUtilsObj>.PrintStep()
        	Prints:
        			~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start of Variation #1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        self.logger.info('{s:{c}^{n}}'.format(s="\t Start of Variation #" + str(self.step) + "\t", n=100, c='~'))        

    def PrintStepSeparator(self):
        """
        This API will print the End of step in a standard format.
        Every time this API is called step will automatically get incremented.

        @param None

        @return None

        @code:
        <printUtilsObj>.PrintStepSaperator()
        Prints :
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End of Variation #1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
        """
        self.logger.info('{s:{c}^{n}}'.format(s="\t End of Variation #" + str(self.step) + "\t", n=100, c='~'))
        self.step += 1 # Increment the step every time this API is called.
        self.logger.info("\n")        



    def PrintLineSeparator(self):
        """Prints a separator line between the steps.

        @param None

        @return None

        @return None

        """

        self.logger.info("")
        self.logger.info("~" * 100)
        self.logger.info("")      
        self.logger.info("\n")   
        
    def PrintLineSeparator_Short(self):
        """Prints a separator line between the steps.

        @param None

        @return None

        @return None

        """

        
        self.logger.info("~" * 50)           
                 
