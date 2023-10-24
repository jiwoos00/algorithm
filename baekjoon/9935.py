text = input()
bomb = input()

stack = []

for t in text:
    stack.append(t)

    if len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))
