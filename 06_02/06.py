# k개 홀수가 있는 연속부분수열

def solution(nums, k):
    answer = 0

    def count(m):
        res=0
        cnt=0
        left=0
        for right in range(len(nums)):
            if nums[right] % 2 ==1:
                cnt+=1
            while cnt>m:
                if nums[left]%2==1:
                    cnt-=1
                left+=1
            res+=(right-left+1)
        return res
    answer = count(k)-count(k-1)

    return answer

print(solution([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))