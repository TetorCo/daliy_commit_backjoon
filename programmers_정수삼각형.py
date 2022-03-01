def solution(triangle):
    ### 밑에서 부터 보는 코드
    # for i in range(len(triangle-2), -1, -1):
    #     for j in range(len(triangle[i])):
    #         triangle[i][j] += max(triangle[i+1][j:j+2])
    for row in range(1, len(triangle)):
        for idx in range(len(triangle[row])):
            print(triangle[row][idx])
            if idx == 0:  # 왼쪽 끝
                triangle[row][idx] += triangle[row-1][idx]
            elif idx == row:  # 오른쪽 끝
                triangle[row][idx] += triangle[row-1][-1]
            else:  # 그외의 사이 값
                triangle[row][idx] += max(triangle[row-1][idx-1], triangle[row-1][idx])
            print(triangle)
    answer = max(triangle[-1])
    return answer

t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(t))