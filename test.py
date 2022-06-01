mylist = []
temp = []
ver = []
st = input()
temp = st.split(' ')
st = ' '.join(temp)
ver = st[0]
for c in st:
    if c == ver[-1]:
        ver.append(c)
    else:
        continue
    mylist.append(ver)
    print(mylist)
