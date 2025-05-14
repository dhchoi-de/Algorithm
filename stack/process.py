"""
    n번 째 인덱스가 운영체제의 규칙 속에서 몇번 째에 실행되는지 찾는 문제
    배열의 순서가 계속 바뀌기 때문에 location 값에 해당하는 원소를 추적하기 위해 튜플을 활용한다.

"""

def solution(priorities, location):
    answer = 0
    queue = [(idx, process) for idx, process in enumerate(priorities)]
    
    while queue:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

if __name__ == "__main__":
    priorities = [2,1,3,2]
    location = 2
    answer = solution(priorities, location)
    assert answer == 1, "Wrong Answer"