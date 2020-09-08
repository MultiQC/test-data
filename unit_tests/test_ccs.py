#!/usr/bin/env python3

import unittest
import sys

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0,'../MultiQC')

from multiqc.modules.ccs.ccs import parse_ccs_log

class Test(unittest.TestCase):

    def test_parse_line(self):
        with open('data/ccs/ccs.report.txt') as fin:
            data = parse_ccs_log(fin)
            assert data['ZMWs input'] == 93

if __name__ == '__main__':
    unittest.main()
