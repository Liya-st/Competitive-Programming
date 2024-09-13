class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end],arr[start]
                start +=1
                end-=1
        for i in range((len(arr)-1),-1,-1):
            max = i
            for j in range(i,-1,-1):
                if arr[j] > arr[max]: max = j
            if max != i:
                flip(max)
                flip(i)
                res.append(max+1)
                res.append(i+1)
        return res   

             

