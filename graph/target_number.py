"""

"""

def main(numbers, target):
    answer = 0
    cur = [0]
    for number in numbers:
        temp = []
        for c in cur:
            temp.append(c + number)
            temp.append(c - number)
        cur = temp
    
    for c in cur:
        if c == target:
            answer += 1

    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target =  3
    answer = main(numbers, target)
    assert answer== 5, f"Answer is not {5}"