#!/usr/bin/python3

import kvur

def test_check_cf_0_2_3():
    assert kvur.check_cf(0, 2, 3) == True

def test_check_complex_cf():
    assert kvur.check_complex_cf(3, 2j, 5) == True

def test_discriminant_1_2_3():
    assert kvur.discriminant(1, 2, 3) == -8.0

def test_discriminant_j_j_j():
    assert kvur.discriminant(1j, 1j, 1j) == 3 + 0j

def test_root_x1_1_minus_13_36():
    assert kvur.root_x1(1, -13, 36) == 9.0

def test_root_x2_1_minus_13_36():
    assert kvur.root_x2(1, -13, 36) == 4.0

def test_root_x1_complex():
    assert kvur.root_x1(1, 1-2j, -1-1j) == 1j

def test_root_x2_complex():
    assert kvur.root_x2(1, 1-2j, -1-1j) == -1+1j
