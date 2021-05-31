# 3. Quiz
# 3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
# 예시
# id_number = 020316 일 때
#
# 출력 예시
# 02
# 0316
# 732

# id_number = "040709"
# print(id_number[0:2])
# print(id_number[2:6])
# print(int(id_number[0:2]) + int(id_number[2:6]))
# ----------------------------------------------------------

# 3-2. 집 전화번호를 phone_number
# 에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# 예시
# phone_number =  또는 032-9876-4321

# 출력 예시
# 02 또는 032
# 5678 또는 4321
# phone_number = "02-1234-5678".split("-")
# print(phone_number[0] + "\n" + phone_number[2])

# ----------------------------------------------------------

# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

# student_number = '2416'
#
# if student_number[1] == "1":
#     print("{0}반 뉴미디어소프트웨어과".format(student_number[1]))
# elif student_number[1] == "2":
#     print("{0}반 뉴미디어소프트웨어과".format(student_number[1]))
# elif student_number[1] == "3":
#     print("{0}반 뉴미디어웹솔루션과".format(student_number[1]))
# elif student_number[1] == "4":
#     print("{0}반 뉴미디어웹솔루션과".format(student_number[1]))
# elif student_number[1] == "5":
#     print("{0}반 뉴미디어디자인과".format(student_number[1]))
# elif student_number[1] == "6":
#     print("{0}반 뉴미디어디자인과".format(student_number[1]))
# else:
#     print("잘못 입력했습니다.")
#
#
# student_number = '2416'
# number = student_number[1]
# number = int(number)
# majors = ['0', '뉴소과',  '뉴웹과',  '뉴디과']
# if 1 <= number and number <= 6:
#     print(f"{number}반 {majors[(number -1)//2]}")  # -1을 하는 이유, 1 -> 0, 2 ->2  // 나누면 정수가 나옴 / 나눠서 실수가 나온다.
# else:
#     print("잘못입력했습니다.")
# ----------------------------------------------------------
# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
#  grade, major = get_major('2188')
#  print(major, grade) #뉴미디어소프트웨어과 2

# def get_major(argument):
#     if argument[1] == "1" or argument[1] == "2":  # "1" == argument[1] and  argument[1] == "2":
#         major = "뉴미디어소프트웨어과"
#         return argument[0], major
#     elif argument[1] == "3" or argument[1] == "4":
#         major = "뉴미디어웹솔루션과"
#         return argument[0], major
#     elif argument[1] == "5" or argument[1] == "6":
#         major = "뉴미디어디자인과"
#         return argument[0], major
#
#
# grade, major = get_major("2416")
# print(major, grade)


# def get_major(student_number):
#     majors = ['소', '소', '솔', '솔', '디', '디']
#     grade = student_number[0]
#     classroom = int(student_number[1])
#     return grade, majors[classroom-1]
#
# grade, major = get_major("2416")
# print(major, grade) # 뉴미디어소프트웨어과 2

# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# def average(*number):
#     sum = 0
#     for i in number:
#         sum += i
#         i += 1
#     average =(sum/len(number))
#
#     print(average)
# average(10, 20, 30)
# average(4, 23)
#
#
# def average(*numbers):
#     count = 0
#     sum_value = 0
#     for number in numbers:
#         sum_value += number
#         count += 1
#     return sum_value/count
#
#     print(average)
# print(average(10, 20, 30))
# print(average(4, 23))
#
# def average(*numbers):
#     return sum(numbers)/len(numbers)  # len 길이 재는것
#
# print(average(10, 20, 30)) # 큐플
# print(average(4, 23))


# ----------------------------------------------------------

# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
#
# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

# def get_BMI(height, weight):
#     BMI = round((weight / (height * height)), 1)
#     height /= 100
#
#     if BMI > 18.5:
#         return "저체중"
#     elif 18.5 >= BMI < 23:
#         return "보통"
#     elif 23 >= BMI < 25:
#         return "과체중"
#     else:
#         return "비만"
#
#
#
# print(get_BMI(179,69))
#
#
# def get_bmi(height, weight):
#     height /= 100
#     bmi = weight / height ** 2
#     return round(bmi, 1)
#
# bmi = get_bmi(176, 69)
# print(bmi)  # 22.3
#
# if bmi <18.5:
#         print('저체중')
# elif bmi < 23:
#         print('보통')
# elif bmi < 25 :
#         print('과체중')
# else:
#         print('비만')

print("----------------------------------------")
'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''


def n_sum(number):
    sum = 0
    if number < 1000000000:
        for i in str(number):
            sum += int(i)
        return sum
    else:
        return -1


result = n_sum(10)
print(result)  # 1
result = n_sum(331)
print(result)  # 7
result = n_sum(408)
print(result)  # 12
result = n_sum(1000000000)
print(result)  # -1

print("\n")
'''
Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''
import math
def get_subway_fare(km):
    price = 0
    if km < 10:
        fee = 720
        return fee
    elif 10 <= km < 50:
        fee = 720
        price = math.ceil((km - 10) / 5) * 100 + fee
        return price
    elif 50 < km:
        fee = 1520
        price = math.ceil((km - 50) / 8) * 100 + fee
        return price


fare = get_subway_fare(5)
print(fare)  # 720
fare = get_subway_fare(26)
print(fare)  # 1120
fare = get_subway_fare(61)
print(fare)  # 1720

print("\n")
print("----------------------------------------")
'''
Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''


# def get_three_six_nine(num):
#     if num == 3 or num == 6 or num == 9:
#         return "짝"
#     elif num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
#         return "짝짝"
#     else:
#         return num
def get_three_six_nine(num):
    num = str(num)
    g = (num.count("3") + num.count("6") + num.count("9"))
    if g == 0:
        return num
    else:
        return g * "짝"


result = get_three_six_nine(1)
print(result)
result = get_three_six_nine(3)
print(result)
result = get_three_six_nine(36)
print(result)

print("\n")
print("----------------------------------------")
'''
Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
1. 함수의 이름을 정해준다.
2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
3. 리턴하는 것을 말해준다.
4. 출력 예시를 보여준다.
5. 내가 낸 문제의 답안을 제출한다.
'''

'''
함수 compare()를 만든다. 숫자를 갯수 상관 없이 배열에 넣어 설정한다. 
그다음 list안에 있는 숫자들을 비교한다
list에 들어 있는 숫자중 최대값을 반환한다.
ex)
list = [1,54,65,78,45,65]
print("입력한 수 :", list)     # 입력한 수 : [1,54,65,78,45,65]
print("가장 큰 수 :", compare(list))   # 가장 큰 수 : 78
'''


def compare(list):
    num = len(list)              #len() 어떤 리스트 안에 들어 있는 자료 개수를 알 수 있음

    compare = list[0]
    for i in range(1, num):
        if list[i] > compare:
            compare = list[i]
    return compare


list = [10, 54, 98, 12, 65, 9]
print("입력한 수 :", list)
print("가장 큰 수 :", compare(list))

list = [4, 57, 54, 45, 3, 24, 78, 2]
print("입력한 수 :", list)
print("가장 큰 수 :", compare(list))

print("----------------------------------------")
'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return "소수 아님"
        return "소수"

result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

print("----------------------------------------")
'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 
이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!'
 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
def get_compliment(text):
    if "고구마" in text:
        return "왓쇼이"
    elif "맛있는" in text:
        return "우마이!"
    elif "놀랄 만한" in text:
        return "요모야..!"
    elif "황당한" in text:
        return "요모야..!"
    elif "굉장한" in text:
        return "요모야..!"
    else:
        return "으무!"

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!