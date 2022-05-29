# put your python code here
word = input() + ' запретил букву'
for i in range(ord('Я'), ord('я') + 1):
    mylist = [c for c in word if c != chr(i)]
    word = ''.join(mylist)
    
    if chr(i + 1) not in word:
        continue   
    else:    
        print(word.lstrip().replace('  ', ' ') + ' ' + chr(i + 1)) 
    mylist = []
