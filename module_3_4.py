def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        if len(root_word) <= len(i):
           if root_word in i.lower():
                same_words.append(i)
        else:
            if i.lower() in root_word:
                same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)