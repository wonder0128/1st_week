input = "abadabac"

# O(N)
def find_not_repeating_first_character(string):
    # 반복되지 않는 첫번째 알파벳
    # 반복되는지 안되는지 판단

    # 1. string에서 알파벳의 빈도수를 찾는다
    # O(N)
    occurrence_array = find_alphabet_occurrence_array(string)

    # 2. 빈도수가 1인 알파벳들 중 string에서 무엇이 먼저 나왔는지 찾는다
    not_repeating_character_array = []

    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    # print(not_repeating_character_array)
    # O(N)
    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():                      # 알파벳 검사
            continue
        arr_index = ord(char) - ord('a')            # 해당 문자를 인덱스로 치환
        alphabet_occurrence_array[arr_index] += 1   # 빈도수 배열에 인덱스로 찾아가 해당 값을 추가

    return alphabet_occurrence_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))