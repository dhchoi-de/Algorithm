"""
    progress에 speed를 점진적으로 더하고 100이 됐을 때, 배열의 인덱스 순서대로 progress가 100인 작업을 모두 배포한다
    모든 작업이 배포됐을 때 각 배포마다 몇 개의 작업이 배포될 것인가를 푸는 문제
    배열의 인덱스 순서대로 배포해야 하기 때문에 queue의 FIFO가 문제해결의 Key가 될 수 있다.(popleft)
    첫 번째 인덱스가 조건을 만족(progress=100)시킬 때 큐의 popleft()를 이용해서 원소를 비워주고
    progress가 100이 아닌 원소가 나올 때 까지 반복하면서 배포 횟수를 더해준다.
    모든 작업을 다 배포할 때 까지 반복한다.
"""
from collections import deque

def solution(progresses, speeds):
    answer = []
    is_break = False
    while progresses:
        if is_break:
            break

        release = 0
        progresses = [min(progress+speed, 100) for progress, speed in zip(progresses, speeds)]

        queue = deque(progresses)
        speed_queue = deque(speeds)

        while queue:
            if queue[0] == 100:
                queue.popleft()
                speed_queue.popleft()
                release += 1
            else:
                if release >= 1:
                    answer.append(release)
                progresses = list(queue)
                speeds = list(speed_queue)
                break
            
            if not queue:
                answer.append(release)
                is_break = True
                break
        
    return answer


if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    answer = solution(progresses, speeds)