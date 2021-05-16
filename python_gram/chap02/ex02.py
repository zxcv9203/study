# print - end옵션

print('Welcome to', end=' ')		# 출력 후 마지막으로 출력할 문자를 지정 기본 값은 개행(\n)이다.
print('Python', end=' 3.9.4 ')		# end 옵션의 문자는 다양한 문자들이 올 수 있다.
print(':)')							# 아무 것도 입력안할 시 기본 값인 개행이 이루어지는 것을 볼 수 있다.

# print - file 옵션

import sys

# print로 출력하는 문구를 어디로 보낼지 지정할 수 있다. (표준 출력을 하지않고 특정 파일에다 해당 내용을 작성하는 식)
print("Learn Python", file=sys.stdout)	# 현재는 sys.stdout(표준 출력)으로 했기 때문에 잘 출력되는 것을 볼 수 있다.
print()

# print - format 사용(d, s, f)
# d -> 정수, s -> 문자열, f -> 실수

# 해당 구문 두개는 출력 값은 똑같습니다.
print("%s %s" % ("one", "two"))				# 명시적으로 자료형을 적어주면서 사용 (어떤 자료형이 와야하는지 한눈에 볼 수 있음)
print("{} {}".format("one", "two"))			# format 함수가 내부적으로 처리해줘서 유연하게 처리될 수 있음

print("{1} {0}".format("one", "two"))		# 다음과 같이 매개변수의 순서를 지정할 수 있습니다.