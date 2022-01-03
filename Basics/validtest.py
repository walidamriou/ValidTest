import unittest
import cffi
import importlib
import tracemalloc
# pip install html-testRunner
import HtmlTestRunner
import os

# This name will put in the rapport title
projectname = "Test code_add(int a, int b) function"
# This is the files .c and .h name 
c_code_module_name = 'sourcecode_core'

# Start tracing Python memory allocations.
tracemalloc.start()

def load(filename):
    SourceBuffer = open(filename + '.c','r')
    source = SourceBuffer.read()
    IncludesBuffer = open(filename + '.h','r')
    includes = IncludesBuffer.read()
    SourceBuffer.close()
    IncludesBuffer.close()
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source(filename + '_', source)
    ffibuilder.compile()
    module = importlib.import_module(filename + '_')
    return module.lib

  
class SourcecodeCoreTest(unittest.TestCase):
    def setUp(self):
        self.module = load(c_code_module_name)
    
    #########################################
    ### Function of the test              ###
    #########################################
    
    # Test 0 of code_add(int a, int b) function: Test if 4+2 = 5, it should equal 6 
    # This test should not pass 
    def test_zero(self):
        self.assertEqual(self.module.code_add(4,2), 5,'Test 1 / Error / Not passed')
    
    # Test 1 of code_add(int a, int b) function: Test if 1+3 = 4, it should equal 4
    # This test should pass
    def test_one(self):     
        self.assertEqual(self.module.code_add(1,3), 4,'Test 1 / Error / Not passed')
    
    # Test 2 of code_add(int a, int b) function: Test if 2+3 = 3, it should equal 5
    # This test should not pass 
    def test_two(self):
        self.assertEqual(self.module.code_add(2,3), 3,'Test 2 / Error / Not passed')

    #########################################
    ### End Function of the test          ###
    #########################################


if __name__ == '__main__':
    dir_name = "{0}".format(os.getcwd())
    unittest.main(exit=False,testRunner=HtmlTestRunner.HTMLTestRunner(
        template=''+dir_name+'/rapport_template/index.html', 
        open_in_browser=True,
        report_title='Test Rapport of '+projectname,
        # verbosity=2,
        report_name='rapport',
        )
        )
    # Delete the files that created to unittest
    extensionslist = [".o", "_.c",".so"]
    #dir_name = "{0}".format(os.getcwd())
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(tuple(extensionslist)):
            os.remove(os.path.join(dir_name, item))

    
    



