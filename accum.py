#1

def accum(s):
    newlist = []
    count = 1

    for letter in s:
        newlist.append(letter*count)
        count += 1

    newString = '-'.join(letter for letter in newlist).title()
    return newString
print(accum("abc"))


# 2

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
# print(accum("abc"))


