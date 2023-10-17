# 시간초과
def solution(phoneBook):
    phoneBook.sort()
    
    for i in range(len(phoneBook) - 1):
        for j in range(i + 1, len(phoneBook)):
            if phoneBook[i] in phoneBook[j]:
                if phoneBook[j].index(phoneBook[i]) == 0:
                    return False
                
    return True


# 해시
def solution(phone_book):
    # hashmap
    phone_book_dict = {}
    for number in phone_book:
        phone_book_dict[number] = True
    
    # prefix check
    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_book_dict:
                return False
    return True
    