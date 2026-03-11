from week_seven_regular_expressions.response import validate_email

def test_validate_email():
    assert validate_email("malan@harvard.edu") == True
    assert validate_email("mail.adila@gmail.com") == True

def test_validate_email_negative():
    assert validate_email("malan@@@harvard.edu") == False
    assert validate_email("mail.adila@gmail..com") == False

