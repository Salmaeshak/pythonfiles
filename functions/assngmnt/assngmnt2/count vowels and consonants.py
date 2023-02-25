def count(word):
    vcount = 0
    ccount =0
    for i in range(len(word)):
        if word[i] in ["a","e","i","o","u"]:
            vcount = vcount+1
        else:
            ccount = ccount+1
    print("the number of vowels are",vcount)
    print("the number of consonant are",ccount)
word = input("enter a word:")
count(word)