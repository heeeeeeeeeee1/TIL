# 오름차순이면 ascending, 내림차순이면 descending, 둘다 아니면 mixed

melody = list(map(int,input().split()))


if melody == sorted(melody):
    print('ascending')
elif melody == sorted(melody,reverse=True):
    print('descending')
else:
    print('mixed')

'''
리뷰
1. for문으로 요소 하나씩 가져와야 하나 했다가
1-1. 내장함수 사용
1-2. .sort() 메서드 사용했다가 원본 값을 바꿔버려서 꼬이는 것 같아 sorted 사용
1-3. 늘 헷갈리는 sort와 sorted(sort는 원본 리스트 수정, sorted는 새로운 리스트 반환) 
'''