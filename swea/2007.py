def solv(s):
    word = s[0]

    # 단어 만들기
    for i in range(1, len(s)):
        word += s[i]

        if s[i] == word[0]:
            if word[0:len(word)] == s[i:i+len(word)]:
                word = word[0:-1]
                break
    
    return len(word)

T = int(input())

for idx in range(T):
    s = input()
    
    print(f'#{idx+1} {solv(s)}')