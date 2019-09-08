#1
def capitals_first(text):
    words = text.split()
    st1 = []
    st2 = []
    for word in words:
        if word[0].isalpha():
            if word[0].isupper():
                st1.append(word)
            else:
                st2.append(word)
    return " ".join(st1 + st2)

print(capitals_first("sort Hey You, me "))


# shorter and cleaner solution
# def capitals_first(string):
#     return ' '.join([word for word in string.split() if word[0].isupper()] + [word for word in string.split() if word[0].islower()])
# print(capitals_first("sort Hey You, me"))
