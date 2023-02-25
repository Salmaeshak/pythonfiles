""""find all the words from sentence that are less than 4 letters"""
sentance = input('enter the sentance:')
word = sentance.split(" ")
print(word)
result = [x for x in word if len(x)<4]
print(result)