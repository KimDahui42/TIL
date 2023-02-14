def solution(numbers):
    sorted_array=sorted(numbers,key=lambda val:str(val)*5,reverse=True)
    return ('').join(list(map(lambda val:str(val),sorted_array)))


numbers=[6, 10, 2]
print(solution(numbers))

num=[3, 30, 34, 5, 9]
print(solution(num))