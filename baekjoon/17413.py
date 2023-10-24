def reverse_words(s):
    res = []
    word = []
    ch = 0

    for char in s:
        if char == '<':
            # 태그 시작
            res.extend(reversed(word))
            word = []
            ch = 1
            res.append(char)
        elif char == '>':
            ch = 0
            res.append(char)
        elif ch == 1:
            # 태그 내부
            res.append(char)
        else:
            # 태그 외부 - 공백
            if char.isspace():
                res.extend(reversed(word))
                res.append(char)
                word = []
            else:
                word.append(char)
    res.extend(reversed(word))
    return ''.join(res)

s = input().strip()
res = reverse_words(s)
print(res)