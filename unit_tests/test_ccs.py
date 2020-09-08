#!/usr/bin/env python3

import pytest
import sys

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0,'../MultiQC')

from multiqc.modules.ccs.ccs import parse_PacBio_log, parse_line

PARSABLE_LINES  = [
        ('', {}),
        ('ZMWs input (A) :', {'name':'ZMWs input', 'annotation':'A'}),
        ('ZMWs input :', {'name':'ZMWs input'})
        #('ZMWs input          (A)  : 93', {'name':'ZMWs input', 'count': 93})
        #('ZMWs input          (A)  : 93', {'name':'ZMWs input', 'count': 93})
]

@pytest.mark.parametrize(['line', 'data'], PARSABLE_LINES)
def test_parsable_lines(line, data):
    parsed_line = parse_line(line)
    assert parsed_line == data
