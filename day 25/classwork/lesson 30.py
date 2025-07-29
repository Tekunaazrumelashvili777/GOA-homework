def longer_word(word1, word2):
    if len(word1) > len(word2):
        print(word1)
    elif len(word2) > len(word1):
        print(word2)
    else:
        print("ორივე სიტყვა ერთნაირი სიგრძისაა")
longer_word("apple", "banana")   
longer_word("dog", "cat")      
longer_word("hello", "world") 