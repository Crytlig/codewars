'''
    Convert a string to a new string.
    If a character appears once add "(".
    If a character appears more than once add ")".
    Ignore capitalization

    Example I/O:
    "din" => "((("
    "recede" => "()()()"
    "Success" => ")())())"
    "(( @" => "))(("

'''
# clear initial solution
def duplicate_encode(word):
    word_list = [x.lower() for x in word]
    output_string = ""

    for k in word_list:
        if word_list.count(k) > 1:
            output_string += ')'
        else:
            output_string += '('
    return output_string

# list comprehensions
def duplicate_encode(word):
    word_list = [x.lower() for x in word]
    return ''.join([('(' if word_list.count(s) == 1 else ')') for s in word_list])

# comprehension without list
def duplicate_encoder(word):
    return ''.join((')' if word.lower().count(i) > 1 else '(' for i in word.lower()))
