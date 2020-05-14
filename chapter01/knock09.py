from random import sample


def make_shuffle_text(text):
    text_list = []
    for t in text.split():
        word = ''
        if len(t) > 4:
            word += t[0]
            word += ''.join(sample(list(t[1:-1]), len(t[1:-1])))
            word += t[-1]
        else:
            word = t
        text_list.append(word)
    return text_list


text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
text_list = make_shuffle_text(text)
print(text_list)
