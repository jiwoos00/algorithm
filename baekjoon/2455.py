people, max_people = 0, 0

for _ in range(4):
    off, on = map(int, input().split())
    people += on 
    people -= off


    if max_people < people:
        max_people = people
    
print(max_people)