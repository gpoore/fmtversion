# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Geoffrey M. Poore
# All rights reserved.
#
# Licensed under the BSD 3-Clause License:
# http://opensource.org/licenses/BSD-3-Clause
#


from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import sys
if sys.version_info.major == 2:
    from io import open
import pytest
import fmtversion as mdl




def test_doc():
    # Make sure README and doc in `fmtversion.py` match
    with open('fmtversion.py', encoding='utf8') as f:
        doc = f.read().split("'''", 2)[1].strip('\n ')
    with open('README.rst', encoding='utf8') as f:
        readme = f.read().rstrip('\n ')
    assert doc == readme


def test_get_version_dev():
    assert mdl.get_version(0, 0, 1, 'dev', 2) == '0.0.1.dev2'
    assert mdl.get_version(0, 1, 0, 'dev', 3, usemicro=False) == '0.1.dev3'

def test_get_version_alpha():
    assert mdl.get_version(0, 0, 1, 'a', 2) == '0.0.1a2'
    assert mdl.get_version(0, 0, 1, 'alpha', 2) == '0.0.1a2'

def test_get_version_beta():
    assert mdl.get_version(2, 3, 1, 'b', 4) == '2.3.1b4'
    assert mdl.get_version(2, 3, 1, 'beta', 4) == '2.3.1b4'

def test_get_version_candidate():
    assert mdl.get_version(2, 3, 0, 'c', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'rc', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'candidate', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'releasecandidate', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'pre', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'preview', 3, usemicro=False) == '2.3c3'

def test_get_version_final():
    assert mdl.get_version(4, 6, 7, 'final', 0) == '4.6.7'
    assert mdl.get_version(4, 6, 0, 'final', 0, usemicro=False) == '4.6'
    assert mdl.get_version(4, 0, 0, 'final', 0, usemicro=False) == '4.0'
    with pytest.raises(ValueError):
        mdl.get_version(4, 0, 0, 'final', 1)

def test_get_version_post():
    assert mdl.get_version(4, 6, 7, 'post', 0) == '4.6.7.post0'
    assert mdl.get_version(4, 6, 0, 'post', 3, usemicro=False) == '4.6.post3'
    assert mdl.get_version(4, 6, 0, 'r', 3, usemicro=False) == '4.6.post3'
    assert mdl.get_version(4, 6, 0, 'rev', 3, usemicro=False) == '4.6.post3'

def test_get_version_releaselevel():
    test_list = ['alph', 'bet', 'cand', 'fin']
    for t in test_list:
        with pytest.raises(ValueError):
            mdl.get_version(1, 1, 1, t, 0)

def test_get_version_useserial():
    assert mdl.get_version(1, 2, 3, 'final', 0, useserial=False) == '1.2.3'
    assert mdl.get_version(1, 2, 3, 'beta', 0, useserial=False) == '1.2.3b'
    assert mdl.get_version(1, 2, 3, 'rc', 0, useserial=False) == '1.2.3c'
    assert mdl.get_version(1, 2, 0, 'dev', 0, usemicro=False, useserial=False) == '1.2.dev'
    assert mdl.get_version(4, 6, 7, 'post', 0, useserial=False) == '4.6.7.post'
    with pytest.raises(ValueError):
        assert mdl.get_version(4, 6, 0, 'post', 3, usemicro=False, useserial=False) == '4.6.post3'
    with pytest.raises(ValueError):
        assert mdl.get_version(4, 6, 0, 'r', 3, usemicro=False, useserial=False) == '4.6.post3'
    with pytest.raises(ValueError):
        assert mdl.get_version(4, 6, 0, 'rev', 3, usemicro=False, useserial=False) == '4.6.post3'

def test_get_version_case():
    assert mdl.get_version(2, 3, 0, 'C', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'RC', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'Candidate', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'ReleaseCandidate', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'Pre', 0, usemicro=False) == '2.3c0'
    assert mdl.get_version(2, 3, 0, 'Preview', 3, usemicro=False) == '2.3c3'

def test_get_version_type_checking():
    assert mdl.get_version('1', '2', '3', 'b', '4') == '1.2.3b4'
    with pytest.raises(TypeError):
        mdl.get_version('wag')
    with pytest.raises(TypeError):
        mdl.get_version('wag', 'snag', 'brag')
    with pytest.raises(TypeError):
        mdl.get_version(1, 2, 3, 5, 4)

def test_get_version_value_checking():
    test_list = [(-1, 0, 0, 'final', 0), #negative int
                 (1, 1, 1, 'final', 1), #final with non-zero serial
                 (1, 2, 3, '5', 4), #releaselevel not in dict
                ]
    for t in test_list:
        with pytest.raises(ValueError):
            mdl.get_version(*t)
    with pytest.raises(ValueError):
        mdl.get_version(1, 1, 1, 'final', 0, usemicro=False)

def test_get_version_info():
    assert mdl.get_version_info('1', '2', '3', 'b', '4') == mdl.VersionInfo(1, 2, 3, 'b', 4)
    assert mdl.get_version_info('1', '2', '3', 'BETA', '4') == mdl.VersionInfo(1, 2, 3, 'b', 4)

def test_get_version_plus_info():
    assert mdl.get_version_plus_info(1, 2, 0, 'dev', 0, usemicro=False, useserial=False) == ('1.2.dev', mdl.VersionInfo(1, 2, 0, 'dev', 0))
    assert mdl.get_version_plus_info(1, 2, 0, 'dev', 0, usemicro=False) == ('1.2.dev0', mdl.VersionInfo(1, 2, 0, 'dev', 0))
    assert mdl.get_version_plus_info(1, 2, 0, 'dev', 0, useserial=False) == ('1.2.0.dev', mdl.VersionInfo(1, 2, 0, 'dev', 0))
    assert mdl.get_version_plus_info(1, 2, 0, 'dev', 0) == ('1.2.0.dev0', mdl.VersionInfo(1, 2, 0, 'dev', 0))
    with pytest.raises(TypeError):
        mdl.get_version_plus_info(1, 2, 0, 'dev', 0, unknownkey=123)

def test_pep440_examples():
    # Examples adapted from https://www.python.org/dev/peps/pep-0440/,
    # from the list under "Summary of permitted suffixes and relative ordering"
    assert mdl.get_version(1, 0, 0, 'dev', 456, usemicro=False) == '1.0.dev456'
    assert mdl.get_version(1, 0, 0, 'a', 1, usemicro=False) == '1.0a1'
    assert mdl.get_version(1, 0, 0, 'a', 2, usemicro=False) == '1.0a2'
    assert mdl.get_version(1, 0, 0, 'a', 12, usemicro=False) == '1.0a12'
    assert mdl.get_version(1, 0, 0, 'b', 1, usemicro=False) == '1.0b1'
    assert mdl.get_version(1, 0, 0, 'b', 2, usemicro=False) == '1.0b2'
    assert mdl.get_version(1, 0, 0, 'c', 1, usemicro=False) == '1.0c1'
    assert mdl.get_version(1, 0, 0, 'final', 0, usemicro=False) == '1.0'
    assert mdl.get_version(1, 0, 0, 'post', 456, usemicro=False) == '1.0.post456'
    assert mdl.get_version(1, 0, 0, 'post', 456, usemicro=False) == '1.0.post456'
    assert mdl.get_version(1, 1, 0, 'dev', 1, usemicro=False) == '1.1.dev1'


def test_get_version_from_version_py_str():
    for version_py_str in ["__version__ = get_version(1, 0, 0, 'dev', 456, usemicro=False)",
                           "# comment\n__version__ = get_version(1, 0, 0, 'dev', 456, usemicro=False)",
                           "# comment\n \n__version__ = get_version(1, 0, 0, 'dev', 456, usemicro=False)\n\n\n",
                           "__version__, __version_info__ = get_version_plus_info(1, 0, 0, 'dev', 456, usemicro=False)\n",
                           "__version__ = fmtversion.get_version(1, 0, 0, 'dev', 456, usemicro=False)",
                           "__version__, __version_info__ = fmtversion.get_version_plus_info(1, 0, 0, 'dev', 456, usemicro=False)\n"]:
        assert mdl.get_version_from_version_py_str(version_py_str) == '1.0.dev456'
