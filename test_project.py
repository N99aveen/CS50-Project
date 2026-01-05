import math
import pytest

from project import (
    calculate_compound_interest,
    calculate_emi,
    calculate_sip_future_value
)

# =========================================================
# TEST: COMPOUND INTEREST
# =========================================================

def test_calculate_compound_interest_basic():
    result = calculate_compound_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00


def test_calculate_compound_interest_zero_rate():
    result = calculate_compound_interest(5000, 0, 5)
    assert result == 5000


def test_calculate_compound_interest_large_years():
    result = calculate_compound_interest(1000, 12, 20)
    assert result > 9000


# =========================================================
# TEST: EMI CALCULATOR
# =========================================================

def test_calculate_emi_basic():
    emi = calculate_emi(100000, 10, 1)
    assert emi > 8000
    assert emi < 9000


def test_calculate_emi_long_tenure():
    emi = calculate_emi(500000, 8, 20)
    assert emi > 0


def test_calculate_emi_zero_interest():
    with pytest.raises(ZeroDivisionError):
        calculate_emi(100000, 0, 5)


# =========================================================
# TEST: SIP CALCULATOR
# =========================================================

def test_calculate_sip_future_value_basic():
    fv = calculate_sip_future_value(1000, 12, 10)
    assert fv > 200000


def test_calculate_sip_future_value_short_term():
    fv = calculate_sip_future_value(2000, 10, 1)
    assert fv > 24000


def test_calculate_sip_future_value_zero_return():
    fv = calculate_sip_future_value(1000, 0.0001, 1)
    assert fv > 12000


# =========================================================
# EDGE CASE TESTS
# =========================================================

def test_negative_values():
    fv = calculate_sip_future_value(1000, 12, 0)
    assert fv == 0
