word = input()
alphabet = list('abcdefghijklmnopqrstuvwxyz')   # 문자열로도 될 것 같은데? 문자열로하면 값 바꾸는게 안되던가 하면서 이것 저것 바꾸다가 이런 형태가 됨

for w in word:
    for a in range(len(alphabet)):    
        if w == alphabet[a]: 
            alphabet[a] = word.index(w) # index는 아마 같은 문자 있으면 처음 등장하는 위치 반환할걸?
        
for i in range(len(alphabet)):
    if str(alphabet[i]).isalpha():      # 아직 영문 소문자로 되어있다면
        alphabet[i] = -1                # -1로 바꿔라
    else:
        continue
print(*alphabet) 

'''
리뷰
1. 이중for문 안에서 해당 없는 경우 -1로 한번에 바꾸고 싶었는데
1-1. else로 넣으면 전부다 -1로 바뀜
2. (생각하기 싫은건지) 생각 안나서 그냥 한번 더 일함
2-1. 값을 바꿀건데 인덱스 접근을 안한...ㅋ
'''