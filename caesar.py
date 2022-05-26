s = input()

k = int(input())

my_string = [chr(ord(c) + k) for c in s if c != ',' or c != ' ' or c != '.']



print(*my_string)
