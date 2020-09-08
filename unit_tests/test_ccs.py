#!/usr/bin/env python3

import pytest
import sys

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0,'../MultiQC')

from multiqc.modules.ccs.ccs import parse_PacBio_log, parse_line

PARSABLE_LINES  = [
        '',
        'ZMWs input :',
        'ZMWs input (A) :',
        'ZMWs input : 93',
        'ZMWs input (A) : 93',
        'Coefficient of correlation    : 28.78%',
        'ZMWs generating CCS (B)  : 44 (47.31%)',
        'Coefficient of correlation  (A)  : 28.78%',
]

PARSED_RESULTS = [
        {},
        {
            'name':'ZMWs input'
        },
        {
            'name':'ZMWs input',
            'annotation':'A'
        },
        {
            'name':'ZMWs input',
            'count': 93
        },
        {
            'name':'ZMWs input',
            'annotation':'A',
            'count': 93
        },
        {
            'name': 'Coefficient of correlation',
            'percentage': 28.78
        },
        {
            'name': 'ZMWs generating CCS',
            'annotation': 'B',
            'count': 44,
            'percentage': 47.31
        },
        {
            'name': 'Coefficient of correlation',
            'percentage': 28.78,
            'annotation': 'A'
        }
]

MARK = zip(PARSABLE_LINES, PARSED_RESULTS)


@pytest.mark.parametrize(['line', 'data'], MARK)
def test_parsable_lines(line, data):
    parsed_line = parse_line(line)
    assert parsed_line == data
