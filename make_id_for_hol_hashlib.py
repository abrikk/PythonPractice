import hashlib


def make_id(sentence: str) -> str:
    """
    Make a unique id for a sentence.
    """
    return hashlib.shake_256(sentence.encode('utf-8')).hexdigest(5)


print(make_id('World Wind Day'))
