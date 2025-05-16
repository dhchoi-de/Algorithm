"""
    순서대로 다리를 건너려는 트럭들이 대기하고 있고 모든 트럭이 조건하에 다리를 건너는 최소 시간을 구하는 문제
    다리로 진입하는 트럭의 순서가 정해져있기 때문에 조건만 만족하면 바로바로 다리위로 올려서(board) 달리게 해야한다.
    모든 트럭은 1초에 1만큼의 거리를 갈 수 있다. 첫 번째 트럭은 반드시 조건을 만족시킨다. 
    모든 트럭이 다리위로 진입해도(truck_weights) 다리 길이에 따라 여전히 달려야 되는 경우(board)를 고려한다.
"""

def solution(bridge_length, weight, truck_weights):
    step = 1
    board = []
    weight_sum = []
    while truck_weights:
        cur = truck_weights[0]
        if sum(weight_sum) + cur <= weight:
            truck_weights.pop(0)
            weight_sum.append(cur)
            board.append(bridge_length)

        board = [b-1 for b in board]
        if any(b <= 0 for b in board):
            board.pop(0)
            weight_sum.pop(0)
        step += 1

    while board:
        board = [b-1 for b in board]
        if any(b <= 0 for b in board):
            board.pop(0)
            weight_sum.pop(0)
        step += 1
    
    return step

if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10]
    step = solution(bridge_length, weight, truck_weights)
    assert step == 101, "Wrong Answer"