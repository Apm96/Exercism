def count_words(sentence):
     sentence = sentence.lower()
     sentence = sentence.replace(","," ").replace("'"," ").replace("can t", "can't").replace("!!&@$%^&"," ").replace("_"," ").replace("."," ").replace(":"," ").replace("don t", "don't")
     counts = dict()
     words = sentence.split()

     for word in words:
         
        if word in counts:            
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

     return counts