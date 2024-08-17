# 알파벳 소문자로만 이루어진 단어5

# word = input()
# # 인덱스 번호 활용. z는 공백
# alphabet = 'abcdefghijklmnopqrstuvwxyz' # 26개
# result = [-1] * 26
#
# for char in word:
#     for i in range(len(alphabet)):
#         if char == alphabet[i]:
#             if char == 'z':
#                 result[i] = ' '
#             else:
#                 result[i] = i
#
#
# print(result)


# for char in word: # 입력받은 word에서 한 문자 씩 가져오기
#     for idx in range(len(alphabet)): # 알파벳 문자열에서 하나씩 가져오기
#         if char in alphabet:
#             result = idx
#             result_list.append(result)
#             if char == 'z':
#                 result_list.append(' ')
#         elif char not in alphabet:
#             result_list.append(-1)

