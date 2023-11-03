def fast_exponentiation(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0: # 짝수
        half_result = fast_exponentiation(base, (exponent // 2))
        return half_result * half_result
    else: # 홀수
        half_result = fast_exponentiation(base, (exponent - 1) // 2)
        return half_result * half_result * base
    
base, exponent = map(int, input().split())
result = fast_exponentiation(base, exponent)