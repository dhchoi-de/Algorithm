"""

"""

def solution(bridge_length, weight, truck_weights):
    step = 0
    board = []
    weight_sum = []
    while truck_weights or board:
        if truck_weights:
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
        else:
            board = [b-1 for b in board]
            if any(b <= 0 for b in board):
                board.pop(0)
                weight_sum.pop(0)
            step += 1
        print(board)
        
    print(step-1)
    return step-1

if __name__ == "__main__":
    # bridge_length = 2
    # weight = 10
    # truck_weights = [7,4,5,6]
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    step = solution(bridge_length, weight, truck_weights)
    # assert step == 8, "Wrong Answer"