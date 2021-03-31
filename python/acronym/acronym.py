def abbreviate(words):
    words = words.replace("-"," ").replace("_"," ")
    acronym = ''.join(word[0] for word in words.upper().split())
    return acronym