#02/24/2026 - Tuesday

def test_one():
    # Indoor voice
    what_to_say = input("Enter the text to say:")
    print(what_to_say.lower())

def test_two():
    # Playback speed
    what_to_slow_down = input("Enter the text that needs to be slowed down")
    print(*what_to_slow_down.split(), sep="...")

#test_one()
#test_two()