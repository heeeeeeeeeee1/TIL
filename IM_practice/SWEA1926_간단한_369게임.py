N = int(input())

for num in range(1,N+1):
    num = str(num)
    if ('3' in num) or ('6' in num) or ('9' in num):
        cnt3 = num.count('3')
        cnt6 = num.count('6')
        cnt9 = num.count('9')
        result = '-' * (cnt3+cnt6+cnt9)
    else:
        result = num

    # print(''.join(result),end = ' ')
    print(result,end = ' ') # 위 처럼 할 필요없었다.


'''
리뷰
1. 처음에 어렵게 접근함(아래 코드)
2. 출력형태 맞추기 헷갈림
'''


#
#
# num = '111323456'
# z = num.count('6')
#
# print(z)


# result_lst = []
# for num in range(1, N+1): #33
#     num = str(num)
#     if len(num) >= 2:   # 두자리수 이상이면? -> len(num) >= 2 len 만큼 반복하면서 +
#         for n in num:   # 3
#             # n = str(n)
#             cnt = 0
#             if n == '3' or n == '6' or n == '9':
#                 cnt += 1
#                 result = cnt * '-'  # cnt만큼 '-' 출력
#                 result_lst.append(result)
#             else:
#                 for _ in range(len(num)):
#                     result += n
#                 result_lst.append(result)
#     else:
#         for n in num:   # 3
#             # n = str(n)
#             cnt = 0
#             if n == '3' or n == '6' or n == '9':
#                 cnt += 1
#                 result = cnt * '-'  # cnt만큼 '-' 출력
#                 result_lst.append(result)
#             else:
#                 result = n
#                 result_lst.append(result)
#
# print(' '.join(result_lst))
#



