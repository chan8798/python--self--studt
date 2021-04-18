a=125
b=-5
c=-1.2
print(a+b+c)

#case1 지수법칙을 이용한 연산#(e-n을 이용){e-n=10**n n은 상수}
a=1.2e-10
b=1.2e10
print(a*b)

#case2 지수법칙을 이용한 연산#(E-n을 이용){E-n=10**n n은 상수}
a=1.1E-10
b=1.1E10
print(a*b)

#8진수와 16진수# #8진수-0o 16진수-0x#

a=0o123  #8진수#
a

b=0xAAACCC #16진수#
b

#복소수# #우리가 일상 복소수(허수)는 i오 사용했는데 파이썬에서는 복소수를 j를 사용한다#
a=1+2j 
b=3-4j

#real-복소수의 실수부분. imag-복소수의 허수부분 conjugate-켤레 복소수 abs-절댓값#

a=2j
a.real # 2j=0+2j 로 나타낼 수 있으므로 실수부분은 0이다.# 
a.imag  # 2j=0+2j 로 나타낼 수 있으므로 허수부분은 2이다.#
a.conjugate() # conjugate-켤레 복소수#
abs(a) # 0+2j의 절댓값은 0*2+2*2=4 abs(a)**2=4 ,abs(a)>0, abs(a)=2 #
       # abs(a)**2=4 abs(a)=X X**2=4 의 X에관한 이차방정식 (X>0) X=2 #

b=1+3j
b.real
b.imag
b.conjugate()
abs(b)

c=2+10j
c.real
c.imag
c.conjugate()
abs(c)

#연산(실수범위)#
a=3
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b/a)
print(a%b)
print(b%a)
print(a//b)
print(b//a)
print(a**b)
print(b**a)
a/b
b/a
a%b
b%a
a//b
b//a

a=2.56
b=8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b/a)
print(a%b)
print(b%a)
print(a//b)
print(b//a)
print(a**b)
print(b**a)
a/b
b/a
a%b
b%a
a//b
b//a

#연산(복소수 범위)#
a=1+2j
b=2

print(a**b)
print(b**a)
print(b/a)
print(a/b)
print(a//b) # type error # -실수범위에서만 된다.
print(b//a) # type error # -실수범위에서만 된다.
print(a%b)  # type error # -실수범위에서만 된다.
print(b%a)  # type error # -실수범위에서만 된다.
print(a+b)
print(a-b)
print(a*b)

a=2+2j
b=3+j
print(a**b)
print(b**a)
print(b/a)
print(a/b)
print(a//b) # type error # -실수범위에서만 된다.
print(b//a) # type error # -실수범위에서만 된다.
print(a%b)  # type error # -실수범위에서만 된다.
print(b%a)  # type error # -실수범위에서만 된다.
print(a+b)
print(a-b)
print(a*b)

a=12
b=0
print(a**b)
print(b**a)
print(b/a) 
print(a/b)  #0으로는 나눌 수 없다#
print(a//b) #0으로는 나눌 수 없다#
print(b//a) 
print(a%b)  #0으로는 나눌 수 없다#
print(b%a)  
print(a+b)
print(a-b)
print(a*b)

#복소수 범위로 나누면 a+bj꼴로 나타냄#
a=1+2j
b=0
print(a**b)
print(b**a) #정의 되지 않음#
print(b/a)  
print(a/b)  #0으로는 나눌 수 없다#
print(a//b) #0으로는 나눌 수 없다# # type error # -실수범위에서만 된다.
print(b//a) # type error # -실수범위에서만 된다.
print(a%b)  #0으로는 나눌 수 없다# # type error # -실수범위에서만 된다.
print(b%a)  # type error # -실수범위에서만 된다.
print(a+b) 
print(a-b)
print(a*b)

a=1+2j
c=a.conjugate()
c
b=3+4j
d=abs(b)
d
print(c+d)