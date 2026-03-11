from week_seven_regular_expressions.um import count_ums

def test_count_ums():
    assert count_ums("um") == 1
    assert count_ums("um?") == 1
    assert count_ums("Um, thanks for the album.") == 1
    assert count_ums("Um, thanks, um...") == 2