# 1. a, b, c 처럼 문자가 해당 문자열에 얼마나 있는지 파악, 그 갯수가 가장 크다면 반환해줘야 하는 값을 알파벳으로 치환
# a -> hello my name is dingcodingco -> 0 max_occurence = 0 max_alphabet = a
# def find_max_occurred_alphabet(string):
#     alphabet_array = [
#         "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
#         "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#         "w", "x", "y", "z"
#     ]
#     max_occurence = 0;
#     max_alphabet = alphabet_array[0]
#
#     for alphabet in alphabet_array:
#         occurenece = 0;
#         for char in string:
#             if char == alphabet:
#                 occurenece += 1
#         # print("alphabet : ", alphabet, " occurenece : ", occurenece)
#
#         if occurenece > max_occurence :
#             max_alphabet = alphabet
#             max_occurence = occurenece
#
#     return max_alphabet

# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다
# 그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트
def find_max_occurred_alphabet(string):
    max_occurence = 0
    max_alphabet_index = 0

    for index in range(len(find_alphabet_occurrence_array(string))):
        alphabet_occurrence = find_alphabet_occurrence_array(string)[index]

        if alphabet_occurrence > max_occurence:
            max_occurence = alphabet_occurrence
            max_alphabet_index = index

    # print(max_alphabet_index)
    # max_alphabet_index -> 인덱스 값 -> 아스키코드 형태로 변경 -> 알파벳으로 치환
    res = chr(max_alphabet_index + ord('a'))
    return res

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():                      # 알파벳 검사
            continue
        arr_index = ord(char) - ord('a')            # 해당 문자를 인덱스로 치환
        alphabet_occurrence_array[arr_index] += 1   # 빈도수 배열에 인덱스로 찾아가 해당 값을 추가

    return alphabet_occurrence_array

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


