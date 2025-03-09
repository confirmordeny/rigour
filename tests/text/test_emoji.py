from rigour.text.emoji import remove_emoji


def test_remove_emoji():
    assert remove_emoji("abc") == "abc"
    assert remove_emoji("ab⚔️🚩cd") == "abcd"
    assert remove_emoji("\U0001f600\U0001f601") == ""
    assert remove_emoji("ЙГЗЖ") == "ЙГЗЖ"
