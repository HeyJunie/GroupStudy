# 1. collections 모듈에서 deque 불러오기
from collections import deque

# 2. deque 생성
deq = deque()
print(deq)
# print결과 -> deque([])

# 3. append(): deque에서 오른쪽(뒤)에 값 추가
deq.append(6)
deq.append(7)
print(deq)
# print결과 -> deque([6, 7])

# 4. appendleft(): deque에서 왼쪽(앞)에 값 추가
deq.appendleft(5)
deq.appendleft(4)
print(deq)
# print결과 -> deque([4, 5, 6, 7])

# 5. extend(): deque 오른쪽(뒤)에 리스트의 객체들을 앞쪽부터 순환해서 차례대로 추가
deq.extend([4, 8, 9, 10])
print(deq)
# print결과 -> deque([4, 5, 6, 7, 8, 9, 10])

# 6. extend(): deque 왼쪽(앞)에 리스트의 객체들을 뒤쪽부터 순환해서 차례대로 추가
deq.extendleft([4, 3, 2, 1])
print(deq)
# print결과 -> deque([1, 2, 3, 4, 4, 5, 6, 7, 4, 8, 9, 10])

# 7. remove(): deque 안의 특정한 값 삭제
# 여러개일땐 앞에서부터 하나씩 제거됨
deq.remove(3) # print결과 -> deque([1, 2, 4, 4, 5, 6, 7, 4, 8, 9, 10])
deq.remove(1) # print결과 -> deque([2, 4, 4, 5, 6, 7, 4, 8, 9, 10])
deq.remove(4) # print결과 -> deque([2, 4, 5, 6, 7, 4, 8, 9, 10])
deq.remove(4) # print결과 -> deque([2, 5, 6, 7, 4, 8, 9, 10])
deq.remove(4) # print결과 -> deque([2, 5, 6, 7, 8, 9, 10])
print(deq)


# 8. pop(): deque에서 오른쪽(뒤)값 삭제 후 반환
pop_value = deq.pop()
print(deq)          # print결과 -> deque([2, 5, 6, 7, 4, 8, 9])
print(pop_value)    # print결과 -> 10

# 9. popleft(): deque에서 왼쪽(앞)값 삭제 후 반환
pop_value = deq.popleft()
print(deq)          # print결과 -> deque([2, 5, 6, 7, 4, 8, 9])
print(pop_value)    # print결과 -> 10

# 10. rotate(): deque안의 값들을 회전
deq.rotate(1) # print결과 -> deque([9, 5, 6, 7, 8])
print(deq)
deq.rotate(4) # print결과 -> deque([5, 6, 7, 8, 9])
print(deq)
deq.rotate(-1) # print결과 -> deque([6, 7, 8, 9, 5])
print(deq)
deq.rotate(-4) # print결과 -> deque([5, 6, 7, 8, 9])
print(deq)