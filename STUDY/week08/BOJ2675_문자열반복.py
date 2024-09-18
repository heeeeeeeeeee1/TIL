T = int(input())

for _ in range(T):
    R, word = input().split()
    new_word =''
    for i in word:
        new_word += i*int(R)
    print(new_word)