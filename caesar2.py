mylist = []
l1 = 0
l2 = 0

def lang_test(latter):
    limit1 = 0
    limit2 = 0
    if 1040 <= ord(latter) <= 1071:
        limit1 = 1040
        limit2 = 1071
    elif 1072 <= ord(latter) <= 1103:
        limit1 = 1072
        limit2 = 1103
    elif 65 <= ord(latter) <= 90:
        limit1 = 65
        limit2 = 90
    elif 97 <= ord(latter) <= 122:
        limit1 = 97
        limit2 = 122        
    return limit1, limit2

def caesar_do(string, drop):
    mylist = []
    
    for c in string:
        limit1, limit2 = lang_test(c)
        if limit1 <= ord(c) <= limit2:
            if (ord(c) + drop) <= limit2:
                mylist.append(chr(ord(c) + drop))
            else:
                mylist.append(chr(limit1 + ((ord(c) + drop - 1) - limit2)))     
        else:
            mylist.append(c)
    print(''.join(mylist), end = ' ')

def cleaner(string):
    spisok = []
    for c in string:
        if c.isalpha() == True or c == ' ':
            spisok.append(c)
    string = ''.join(spisok)
    return string

s = input()

spisok = cleaner(s).split()

for i in range(len(spisok)):
    k = len(spisok[i])
    caesar_do(str(spisok[i]), k)
    


