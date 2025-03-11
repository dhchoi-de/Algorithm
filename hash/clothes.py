"""

https://school.programmers.co.kr/learn/courses/30/lessons/42578

Key Point
- 옷을 종류 별로 구분하되, 종류별로 최소 1개의 옷을 입는 게 아니라 안 입어도 되는게 포인트
- 옷의 각 종류 별로 안 입어도 되는 경우 None을 추가해 주고 모든 조합을 계산한다
- 아무 것도 입지 않은 경우 None을 추가했기 때문에 모든 경우가 None인 경우 1번을 전체 조합의 수에서 빼준다

"""

# Hash 이용한 해결
# reduce(집계 함수, 순회 가능한 데이터[, 초기값]) 를 활용한 옷의 종류별 개수 집계
def solution_hash(clothes):
    from functools import reduce
    answer = dict()
    for _, type in clothes:
        answer[type] = answer.get(type, 0) + 1 
    answer = reduce(lambda x, value: x * (value+1), answer.values(), 1) - 1
    return answer

# 중복된 데이터가 저장된 배열에서 각 원소가 몇 번씩 나오는지 저장된 객체를 얻기위한 Counter 활용
def solution_counter(clothes):
    from functools import reduce
    from collections import Counter
    cloth_type_counter = Counter([type for _, type in clothes])
    answer = reduce(lambda x, value: x * (value+1), cloth_type_counter.values(), 1) - 1
    return answer

if __name__ == "__main__":
    test_data = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = solution_counter(test_data)
    assert answer == 5 , f"The answer is not {answer}"

