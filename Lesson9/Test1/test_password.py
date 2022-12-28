#!/usr/bin/python3

import password_for_check

def test_pas_dfg():
    assert password_for_check.check_passwd('gfd') == False

def test_pass_PAsSwoRD():
    assert password_for_check.check_passwd('PAsSwoRD') == False

def test_pass_abcde4():
    assert password_for_check.check_passwd('abcde4') == True

def test_pass_123456():
    assert password_for_check.check_passwd('123456') == False

def test_pass_123g56():
    assert password_for_check.check_passwd('123g56') == True

def test_pass_sym():
    assert password_for_check.check_passwd('!@#$$%^&*') == False
 
def test_pass_combo():
    assert password_for_check.check_passwd('jdgb#&745f') == True
