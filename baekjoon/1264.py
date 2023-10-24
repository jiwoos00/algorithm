vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text = []
while True:
    t = input()
    if t == '#':
        break
    text.append(t)

for t in text:
    cnt = 0
    for i in t:
        if i in vowel:
            cnt += 1
    print(cnt)
