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
def data_dir():
    yield Path(__file__).parent.parent / 'data'

@pytest.fixture
def report_init():
    report.init()
    yield

@pytest.mark.parametrize(["ignore_links", "expected"], [(True, ["file"]), (False, ["filelink", "nested", "file"])])
@pytest.mark.parametrize(["traverse_method"], [(report.oswalk,), (report.pathwalk,)])
def test_symlinked_files_found(report_init, traverse_method, ignore_links, expected):
    """
    Tests that symlinked files are discovered and ignored properly.
    """
    config.analysis_dir = [Path(__file__).parent.parent / "data/special_cases/symlinks/linked"]
    config.ignore_symlinks = ignore_links
    report.get_filelist([], traverse_method=traverse_method)
    searchfiles_names = [f[0] for f in report.searchfiles]
    assert all(f in searchfiles_names for f in expected)