import functools
def solution(numbers):
    
    # 문자로 변경하여 비교
    numbers = list(map(str, numbers))
    
    def cmp(x, y):
        if y + x > x + y:
            return 1
        elif x + y > y + x:
            return -1
        else:
            return 0
            
    numbers.sort(key = functools.cmp_to_key(cmp))
    
    # 모든 숫자가 0인 경우
    if numbers[0] == '0':
        return '0'
    
    return ''.join(numbers)

"""

functools.cmp_to_key(compare)
compare 함수의 리턴값
    -1 : x가 y보다 앞에 정렬
    1 : y가 x보다 앞에 정렬, 자리바꿈

"""