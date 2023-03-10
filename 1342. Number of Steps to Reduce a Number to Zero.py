###Python

##My solution:
class Solution:
    def numberOfSteps(self, num: int) -> int:
        m=0
        while num:
            if (num/2)%1==0:
                num=num/2
                m=m+1
            else :
                num=num-1
                m=m+1
        return m
        
## Better solution

## using bitwise operations to solve this
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            ans += num & 1  #use num&1 to determine whether the num is odd or even
            if num > 1:
                ans += 1
            num >>= 1
        return ans

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-to-zero/solution/jiang-shu-zi-bian-cheng-0-de-cao-zuo-ci-ucaa4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
