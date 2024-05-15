#!/usr/bin/env python3

"""
Tests for discovering and excluding files
"""

import pytest

from multiqc import config
from multiqc import report
from multiqc.core.file_search import file_search


@pytest.fixture
def search_files():
    file_search()


@pytest.fixture
def ignored_dirs():
    config.analysis_dir = ["data/exclusions/ignore_dirs"]
    config.fn_ignore_dirs = ["ignored", "*_ignored"]


@pytest.fixture
def ignored_paths():
    config.analysis_dir = ["data/exclusions/ignore_paths"]
    config.fn_ignore_paths = ["*/*_ignored"]


@pytest.fixture
def ignore_links(request):
    config.analysis_dir = ["data/special_cases/symlinks/linked"]
    config.ignore_symlinks = request.param


@pytest.mark.parametrize(
    ["ignore_links", "expected"],
    [(True, {"file"}), (False, {"filelink", "nested", "file"})],
    indirect=["ignore_links"],
)
def test_symlinked_files_found(ignore_links, parse_logs, expected):
    """
    Tests that symlinked files are discovered and ignored properly.
    """
    filenames = {f[0] for f in report.searchfiles}
    assert filenames == expected


def test_excluded_dirs(ignored_dirs, parse_logs):
    """
    Tests that ignored folder names are ignored
    """
    expected_files = {"should_be_included"}
    filenames = {f[0] for f in report.searchfiles}
    assert filenames == expected_files


def test_excluded_paths(ignored_paths, parse_logs):
    """
    Tests that ignored *folder* paths are ignored
    """
    expected_files = {"should_be_included"}
    filenames = {f[0] for f in report.searchfiles}
    assert filenames == expected_files
