def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        c = a[i] * b[i]
        answer += c
    return answer