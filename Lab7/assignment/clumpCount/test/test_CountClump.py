# Lab#7 - Whitebox testing
# นายชนินทร์ ธัญสิริพัฒนธาดา 653380125-2 sec.1
import unittest
import sys
sys.path.insert(0,'/workspaces/Lab7_653380125-2/Lab7/assignment/clumpCount/source/')
from CountClump import CountClump

class test_CountClump_C_DC(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start testing class CountClump.")

    @classmethod
    def tearDownClass(cls):
        print('\nFinish testing class CountClump.')

    def setUp(self):
        self.count = CountClump()
        testname = self.shortDescription()
        if testname == "tc001 input=None":
            self.nums = None

        if testname == "tc002 input=[]":
            self.nums = []

        if testname == "tc003 input=[1,1,1]":
            self.nums = [1,1,1]

        if testname == "tc004 input=[1,2]":
            self.nums = [1,2]

        
    def tearDown(self):
        print('\nend of test', self.shortDescription())
        
    def test_tc001(self):
        """tc001 input=None"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 0)

    def test_tc002(self):
        """tc002 input=[]"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 0)

    def test_tc003(self):
        """tc003 input=[1,1,1]"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 1)
    
    def test_tc004(self):
        """tc004 input=[1,2]"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()