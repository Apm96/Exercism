import string
def is_pangram(sentence, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(sentence.lower()) 
