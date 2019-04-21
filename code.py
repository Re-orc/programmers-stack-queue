def solution(heights):
    answer=[]
    for i in range(len(heights)-1,-1,-1):
        for j in range(len(heights[0:i]),-1,-1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
        if heights[i] >= heights[j]:
            answer.append(0)
    return answer[::-1]
