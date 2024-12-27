# 내가 푼거
# def find_max_num(array):
#     result = max(array)
#     return result

# 1. 모든 숫자를 다른 숫자와 비교
# def find_max_num(array):
#     for number in array:
#         is_max_num = True;
#         for compare_number in array:
#             if number < compare_number:
#                 is_max_num = False;
#         if is_max_num:
#             return number;

# 2. 배열 내에 가장 큰 수 찾기
def find_max_num(array):
    max_num = array[0]
    for number in array:
        if number > max_num:
            max_num = number
    return max_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))