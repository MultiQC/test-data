#!/usr/bin/python

""" Template for writing new test classes.
"""

import unittest
import sys, os, re

# from multiqc import ...

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0,'../MultiQC')


class T(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
