# return a string with dash (-) marks before and after each odd integer
# do not begin or end the string with dash (-)
def dashatize(num):
    lstnum = [int(x) for x in str(num)]
    numstr = ""

    for i in lstnum:
        if i % 2:
            numstr += '-' + str(i) + '-'
        else:
            numstr += str(i)

    return numstr.strip('-').replace('--','-')
dashatize(12234)

# loop through numbers as strings instead for a cleaner solution
def dashatize(num):
     num_str = str(num)
     for i in ['1','3','5','7','9']:
         num_str = num_str.replace(i,'-' + i + '-')
     return num_str.strip('-').replace('--','-')
