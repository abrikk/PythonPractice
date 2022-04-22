phrase = input().split()
if len(phrase) > 1:
    phrase_id = "".join([word[0].lower() for word in phrase])
else:
    phrase_id = "".join([word.lower() for word in phrase[0] if word.lower() not in 'aeiou'])
print(phrase_id)
