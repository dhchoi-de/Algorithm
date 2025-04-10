"""
    연속된 숫자를 단일 숫자롤 변환해서 기존 순서를 유지한 리스트를 반환하는 문제
    배열의 마지막 원소를 previous_number와 비교하고 그 값이 다르면 previous_number를 마지막 원소로 업데이트 시켜나가면서 풀 수 있다.
"""

def solution(arr):
    previous_number = None
    answer = []
    for number in arr:
        if previous_number != number:
            answer.append(number)
            previous_number = number
    return answer

if __name__ == "__main__":
    arr = [1, 1, 3, 3, 0, 1, 1] 
    answer = solution(arr)
    assert answer == [1,3,0,1] , f"The answer is not {answer}"
