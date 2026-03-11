from week_seven_regular_expressions.watch import get_shareable_link

def test_get_shareable_link():
    assert get_shareable_link('<iframe width="560" height="315" src="https://www.youtube.com/' +
                              'embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" ' +
                              'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '+
                              'gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_invalid_link():
    assert get_shareable_link('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"'
                              '></iframe>') is None

def test_valid_link():
    assert get_shareable_link('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'