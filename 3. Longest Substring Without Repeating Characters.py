###Python

class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int :
        #哈希集合，记录每个字符是否出现过
        occ=set()
        n=len(s)
        #右指针，初始值为-1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk,ans=-1,0
        for i in range(n):
            if i !=0 :
                #做指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
                while rk + 1 < n and s[rk+1] not in occ:
                    #不断地移动右指针
                    occ.add(s[rk+1])
                    rk+=1
                #第i到rk个字符是一个极长的无重复字符子串
                ans = max(ans,rk-i+1)
         return ans

    
    
    
##Another solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0 #如果s是空序列就返回0
        if len(s) == 1:return 1 #如果s的len只有1，就返回1
        n = len(s)
        res = []
        cur = ""#做子串
        for i in range(n):
            if s[i] not in cur:
                cur += s[i]
                count = len(cur)
                res.append(count)
            else:
                while s[i] in cur:
                    cur = cur[1:i]
                cur += s[i]
                res.append(len(cur))
        
        return max(res)
