def anagrams(word, words):
    return [i for i in words if get_dict(word) == get_dict(i)]


def get_dict(word):
    return {i: word.count(i) for i in word}


w = 'racer'
data = ['crazer', 'carer', 'racar', 'caers', 'racer']
print(anagrams(w, data))
