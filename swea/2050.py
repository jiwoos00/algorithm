alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dic = dict()
for i in range(len(alpha)):
    dic[alpha[i]] = i + 1

s = input()
for i in s:
    print(dic[i], end = ' ')