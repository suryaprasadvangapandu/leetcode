class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        div = len(tasks)//len(processorTime)
        sum =0
        r=[]
        for i in range(len(processorTime)):
            sum =processorTime[i]+tasks[i*div]
            r.append(sum)
        return max(r)
