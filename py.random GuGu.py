from random import randint
print('구구단 외우기')
while True:
    a = randint(1,9)
    b = randint(1,9)
    print('{}x{}='.format(a,b),end="")
    answer=int(input())
    if a*b is answer:
        print('정답')
    else:
        print('오답')
