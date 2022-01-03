import unittest
import cffi
import importlib
import tracemalloc
# pip install html-testRunner 
# https://github.com/oldani/HtmlTestRunner
import HtmlTestRunner


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
    filename = ffibuilder.compile()
    module = importlib.import_module(filename + '_')
    return module.lib

  
class SourcecodeCoreTest(unittest.TestCase):
    def setUp(self):
        self.module = load('sourcecode_core')
        
    def test_zero(self):
        self.assertEqual(self.module.code_add(4,2), 5,'Test 1 / Error / Not passed')

    def test_one(self):     
        self.assertEqual(self.module.code_add(1,3), 4,'Test 1 / Error / Not passed')

    def test_two(self):
        self.assertEqual(self.module.code_add(2,3), 3,'Test 3-1 / Error / Not passed')

template_args = {
    "user": "w"
}

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        template='TestRapport',
        open_in_browser=True,
        report_title='Rapport of sourcecode_core',
        verbosity=2,
        report_name='repporttest_file_sourcecode_core',
        template_args=template_args
        )
        )
    # unittest.main()


