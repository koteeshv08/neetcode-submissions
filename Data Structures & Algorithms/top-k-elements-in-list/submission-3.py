class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        nums.sort()
        l = []
        for i in nums:
            dic[i] += 1
        if(len(dic)==k):
            return list(dic.keys())
        print(dic)
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        print(dic)
        for key,value in dic.items():
            if(k):
                l.append(key)
                k-=1
        return l