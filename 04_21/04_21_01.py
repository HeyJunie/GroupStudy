# 문제
# 두 문자열 s1와 s2가 있을 때, 두 문자열의 '최대공약문자열' s3를 아래와 같이 정의하자.
#
# 문자열 s3를 반복하여 문자열 s1와 s2를 생성할 수 있다.
# 가능한 s3 중에 가장 긴 문자열을 s3로 한다.
# 위 조건을 만족하는 s3가 없으면 빈 문자열을 s3로 한다.
# 이 때, 문자열 s1와 s2를 입력받아 s3를 출력하는 프로그램을 작성하시오.
#
# 입력설명
# 매개변수 s1과 s2가 주어지며, len(s1)과 len(s2)는 최대 100000이다.
#
# 출력설명
# 가능한 s3 중 가장 긴 s3를 반환하시오.
#
# 매개변수 형식
# s1 = 'abababab'
# s2 = 'abab'
#
# 반환값 형식
# 'abab'

def solution(s1, s2):
    def isDivisor(string, divisor):
        n = len(divisor)
        if len(string) % n != 0:
            return False

        while string != '':
            if string[:n] != divisor:
                return False
            string = string[:n]
        return True

    if len(s1) > len(s2):
        str1, str2 = s1, s2
    else:
        str1, str2 = s1, s2

    divisor = str2
    m = 1
    while divisor != '':
        if isDivisor(str2, divisor) and isDivisor(str1, divisor):
            return divisor
        m += 1
        divisor = str2[:len(str2) // m]

    return ''

s1 = 'abababab'
s2 = 'abab'
print(solution(s1, s2))