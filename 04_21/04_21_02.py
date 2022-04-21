# 문제
# 민수는 친구 중 동명이인이 몇명인지 알고싶어져서, 주소록을 살펴보기로 했다.
#
# 민수의 주소록은 리스트로 구성되어 있으며, 리스트의 각 원소는 [친구이름, 전화번호]의 리스트로 되어 있다.
#
# 민수는 친구의 전화번호를 저장할 때 -기호를 쓰기도 하고, 생략하기도 하고, 띄어쓰기로 기재하기도 했다.
# 010-1234-5678이라는 전화번호를
#
# 01012345678
# 010-1234-5678
# 010 1234 5678
# 의 세 가지 방법 중 하나로 저장해 두었다.
#
# 민수의 주소록은 여러 방법으로 저장한 주소록을 모아둔 것이기 때문에, 같은 전화번호를 가진 친구가 여러번 나타날 수 있다.
#
# 전화번호가 변경된 친구는 없다고 가정할 때, 민수의 친구 중 동명이인의 수를 출력하시오.
#
# 입력 설명
# [친구이름, 전화번호]로 구성된 길이가 100000 이하의 리스트
#
# 출력 설명
# 동명이인인 친구의 수
#
# 입력 예시
# [['kim', '012-423-0044'], ['park', '042-512-4555'], ['choi', '555-523'], ['kim', '444-524'], ['kim', '0124230044']]
#
# 출력 예시
# 2


# def solution(address_book):
#     for address in address_book:
#         answer = address
#         print(address)
#     return answer
#


import re
def solution(address_book):
    address_list = []
    count = {}
    for i in range(len(address_book)):
        address= re.split(r'-', address_book[i][1])
        address = "".join(address)
        address_list.append(address)

    for i in address_list:
        try: count[i] += 1
        except: count[i]=1

    answer = count[i]
    return answer

address_book = [['kim', '012-423-0044'], ['park', '042-512-4555'], ['choi', '555-523'], ['kim', '444-524'], ['kim', '0124230044']]
print(len(address_book))
print(solution(address_book))