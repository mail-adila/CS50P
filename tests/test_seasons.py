from week_eight_oops.seasons import calculate_minutes
from week_eight_oops.seasons import get_input

import pytest
from datetime import date
#from seasons import minutes_between, format_minutes

def test_one_year():
    d = date(2025, 3, 12)
    today = date(2026, 3, 12)
    assert (today - d).days * 1440 == 525600

def test_leap_year():
    d = date(2024, 1, 1)
    today = date(2025, 1, 1)  # 366 days — includes Feb 29 2024
    assert (today - d).days * 1440 == 527040


