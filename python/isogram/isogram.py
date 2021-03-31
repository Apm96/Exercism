def is_isogram(string):
    validate = True
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    
    for i in letters:
      count = string.count(i)
      if count > 1:
         validate = False
    return validate