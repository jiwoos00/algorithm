def solution(clothes):
    clothes_dict = {}
    
    for name, types in clothes:
        if types in clothes_dict:
            clothes_dict[types] += 1
        else:
            clothes_dict[types] = 1
    s = 1
    for types in clothes_dict.values():
        s *= (types + 1) # 하나도 선택하지 않는 경우 고려
        
    # 하나도 선택하지 않는 경우 제외
    return s - 1
    