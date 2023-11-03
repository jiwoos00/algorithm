def fast_exponentiation(base, exponent, div):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0: # 짝수
        half_result = fast_exponentiation(base, (exponent // 2), div)
        return (half_result * half_result) % div
    else: # 홀수
        half_result = fast_exponentiation(base, (exponent - 1) // 2, div)
        return (half_result * half_result * base) % div
    
base, exponent, div = map(int, input().split())
result = fast_exponentiation(base, exponent, div)
print(result)