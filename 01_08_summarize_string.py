input_str = "acccdeee"

def summarize_string(input_str):
    occurrence_array = find_alphabet_occurrence_array(input_str)
    result_array = []
    for i in range(len(occurrence_array)):
        alpha_occurrence = occurrence_array[i]
        if alpha_occurrence != 0:
            result_array.append(chr(i + ord('a'))+"/"+str(alpha_occurrence))
    return result_array

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():                      # 알파벳 검사
            continue
        arr_index = ord(char) - ord('a')            # 해당 문자를 인덱스로 치환
        alphabet_occurrence_array[arr_index] += 1   # 빈도수 배열에 인덱스로 찾아가 해당 값을 추가

    return alphabet_occurrence_array


print(summarize_string(input_str))