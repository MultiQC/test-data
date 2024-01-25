#!/usr/bin/env python3

"""
Tests for discovering and excluding files
"""

import pytest
import sys
from multiqc import config
from pathlib import Path

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0, "../MultiQC")

from multiqc.utils import report


@pytest.fixture
def data_dir():
    yield Path(__file__).parent.parent / "data"


@pytest.fixture
def report_init():
    report.init()


@pytest.fixture
def ignored_dirs(data_dir):
    config.analysis_dir = [data_dir / "exclusions/ignore_dirs"]
    config.fn_ignore_dirs = ["ignored", "*_ignored"]


@pytest.fixture
def ignored_paths(data_dir):
    config.analysis_dir = [data_dir / "exclusions/ignore_paths"]
    config.fn_ignore_paths = ["*/*_ignored"]


@pytest.fixture
def ignore_links(request):
    config.analysis_dir = [Path(__file__).parent.parent / "data/special_cases/symlinks/linked"]
    config.ignore_symlinks = request.param


@pytest.mark.parametrize(
    ["ignore_links", "expected"],
    [(True, {"file"}), (False, {"filelink", "nested", "file"})],
    indirect=["ignore_links"],
)
def test_symlinked_files_found(report_init, ignore_links, expected):
    """
    Tests that symlinked files are discovered and ignored properly.
    """
    report.get_filelist([])
    filenames = {f[0] for f in report.searchfiles}
    assert filenames == expected


def test_excluded_dirs(ignored_dirs, report_init):
    """
    Tests that ignored folder names are ignored
    """
    expected_files = {"should_be_included"}
    report.get_filelist([])
    filenames = {f[0] for f in report.searchfiles}
    assert filenames == expected_files


def test_excluded_paths(ignored_paths, report_init):
    """
    Tests that ignored *folder* paths are ignored
    """
    expected_files = {"should_be_included"}
    report.get_filelist([])
    filenames = {f[0] for f in report.searchfiles}
    assert filenames == expected_files
