from week_five_unit_tests.twttr import shorten

def test_shorten():
    assert shorten("adila") == "dl"
    assert shorten("twitter") == "twttr"

