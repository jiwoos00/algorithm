S = input()

suffixes = [S[i:] for i in range(len(S))]
suffixes.sort()

for suffix in suffixes:
    print(suffix)