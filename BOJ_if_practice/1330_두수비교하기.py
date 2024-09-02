A, B = map(int,input().split())

if A > B:   # A가 B보다 크면
    print('>')
elif A < B: # A가 B보다 작으면
    print('<')
else:
    print('==')