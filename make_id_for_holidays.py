import math


def make_id(sentence: str) -> str:
    dont_include = ["a", "day", "of", "for", "the", "an"]
    words = [word.lower() for word in sentence.split() if word.lower() not in dont_include]
    abbreviated_id = []
    if len(words) == 1:
        abbreviated_id.append(words[0].lower())
    else:
        for word in words:
            word = word.strip('.()')
            if word in dont_include:
                continue
            word_id = [ltr for ltr in word if ltr.lower() not in "aeiou"]
            max_length = math.ceil(len(word_id)/2) if len(word_id) > 4 else len(word_id)
            append_word = "".join(word_id)[:max_length]
            abbreviated_id.append(append_word)
    return "_".join(abbreviated_id)


print(make_id("Memory Day (day truce)"))
