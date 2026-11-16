class Solution:
    def digitSum(self, s: str, k: int) -> str:
        v=s
        while len(v)>k:
            t=[]
            for i in range(0,len(v),k):
                t.append(v[i:i+k])
                # print(t)
            we=[]
            for i in t:
                summ=0
                for j in i:
                    summ+=int(j)
                we.append(str(summ))
            v="".join(we)
        return(v)
        