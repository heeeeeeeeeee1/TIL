# 난쟁이 9명 키 정보 받아서 heights 리스트에 추가
# 리스트에서 7개 뽑았을 때 합이 100인 모든 경우 찾기
# -> 9명의 키를 다 더한 값에서 100을 빼면, 7명의 난쟁이에 포함되지 않는 난쟁이 2명의 키 합이 나옴
heights = []
for _ in range(9):
    h = int(input())
    heights.append(h)

# 9명의 키 합
heights_9 = sum(heights)

# 7명에 포함되지 않는 2명의 키 합
heights_2 = heights_9 - 100

# 9명 중 2명을 뽑았을 때 heights_2가 되는 모든 경우의 수 따지기
result = []
find = 0
for a in range(8):  # 아...^^ 범위 틀렸..? 2명 뽑으니까 7까지 순환
    for b in range(a+1,9):        # 범위 이거 맞나
        total = heights[a] + heights[b]   # 아무거나 2개 뽑았는데
        if total == heights_2:  # 그 2명의 키 합이 미포함 2명 키 합과 같다면
            for i in heights:
                if i != heights[a] and i != heights[b]:
                    result.append(i)
            find = 1
            break
    if find == 1:
        break


# 케이스가 여러개라면 아무 숫자 조합이나 출력
result.sort()    # 오름차순 출력해야한다. 문제를 잘 읽자^^

for r in result:
    print(r)





'''
리뷰
1. 생각없이 하다가 블랙잭이랑 섞여서 3명 뽑는 걸로 구상함;
1-1. 7명을 뽑던가 2명을 뽑아야 되는데...
2. 저번에도 아닌애들 2명을 리스트에서 제거하는게 어려웠던 것 같다.
heights.pop(heights[a])
heights.pop(heights[b])

3. 문제를 푸는과정보단 리스트 수정, 출력형태 맞추는게 더 어려웠다.
3-1. 아니 그럴 필요도 없었네...pop을 못써서 그랬네...
4. 41분 걸림 -> 1시간 2분 ㅜ pop(인덱스)인데 왜 값을 괄호안에 넣었을까?ㅋ
5. -> 1시간 11분 자고 싶어서 이전코드 대충봤는데 범위 문제였네^^
6. 아^^ 문제 안읽어서 오름차순 출력 안봤네 ㅋ
7. 결국 이 아래 처럼 하는게 맞았다. pop은 아마 원본 리스트 훼손해서 안되나ㅜ 쉽게 가려다 망함
7-1. 근데 저번에도 이랬던듯

        for i in range(9):
            if heights[i] != heights[a] and heights[i] != heights[b]:
                result.append(heights[i])
        find = 1
        break
if find == 1:
    break

'''