# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위헤 작성 추천
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제1
from re import T
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1
sub.sub1.module1.mod1_test2

sub.sub2.module2.mod2_test1
sub.sub2.module2.mod2_test2

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()

# 예제4
from sub.sub3 import Chapter06_02
from sub.sub3 import Chapter06_02

print(Chapter06_02.add(10, 5))
print(Chapter06_02.divide(10, 2))
print(Chapter06_02.multiply(5, 5))
print(Chapter06_02.power(10, 3))
print(Chapter06_02.subtract(20, 10))
