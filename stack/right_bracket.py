"""
    "(" 와 ")" 가 올바른 괄호의 형태 "()" or "(())" ... 를 띄며 그 짝이 맞는지 확인하는 문제
    "(" 가 등장하면 그에 맞게 ")" 가 적절히 등장해야 하기 떄문에 ")" 부터 나올때 마다 가장 나중에 나온 "(" 을 전체 배열에서 제거하는 방식으로 
    전체 배열을 줄여나가고(LIFO) 최종적으로 전체 배열이 모두 비워지지 않거나 중간에 조건을 만족하지 못하면 False를 반환하면 되는 문제
"""
def solution(s):
    answer = []
    for bracket in s:
        if bracket == '(':
            answer.append(bracket)
        else:
            if answer == []:
                return False
            else:
                answer.pop()

    if answer:
        return False
    return True

if __name__ == "__main__":
    s = "(())))"
    answer = solution(s)
    
