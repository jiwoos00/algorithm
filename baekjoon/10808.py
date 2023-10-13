S = input()

cnt = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for alpha in alphabet:
    cnt[alpha] = 0

for alpha in S:
    cnt[alpha] += 1
  

print(' '.join(map(str, list(cnt.values()))))