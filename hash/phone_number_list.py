"""

https://school.programmers.co.kr/learn/courses/30/lessons/42577

KeyPoint
가장 단순한 방법은 2중 반복문을 통해 전부 다 비교하기
한 번만 반복해서 찾을 수 없을까? 를 고민
숫자로 구성된 문자열이기 때문에 이것을 정렬 했을 때 어떻게 정렬되는지를 알면 힌트가 될 수 있다.
ex) '1521' < '2'

"""

def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        if phone_book[idx+1].startswith(phone_book[idx]):
            return False
    return True

if __name__ == "__main_-":
    phone_book = ["119", "97674223", "1195524421"]
    assert solution(phone_book) == False, f"Answer is not True"