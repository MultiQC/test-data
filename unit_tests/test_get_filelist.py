#!/usr/bin/env python3

import pytest
import sys
from multiqc import config
from pathlib import Path

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0,'../MultiQC')

from multiqc.utils import report

@pytest.fixture
def analysis_dir():
    config.analysis_dir = [Path(__file__).parent / "../data/special_cases/symlinks/linked"]
    yield

@pytest.fixture
def report_init():
    report.init()
    yield

def test_symlinked_files_found(analysis_dir, report_init):
    expected = ["filelink.txt", "nested.txt"]
    report.get_filelist([])
    searchfiles_names = [f[0] for f in report.searchfiles]
    assert all(f in searchfiles_names for f in expected)