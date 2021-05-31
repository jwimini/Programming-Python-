# price: 원가, grade 회원 등급
def solution(price, grade): # S 5 프로, G 10 프로,  V 15 프로
    reduced_price = 0
    if grade == "S":
        # 5프로 할인하는 코드
    할인가 = price * 0.05
    elif grade == "G":
        # 10프로 할인하는 코드
    할인가 = price * 0.1

    elif grade == "V":
        # 15프로 할인하는 코드
    할인가 = price * 0.15
    return price - 할인가

# testcase 를 위한 output
price = 5000
grade = "S"
ret = solution(price, grade)
print("Solution: return value of the function is", ret, ".")
# price1 = 2500
# grade1 ="V"
# ret1 = solution(price1, grade1)
# print("Solution: return value of the function is", ret1, ".")
#
# price2 = 96900
# grade2 = "S"
# ret2 = solution(price2, grade2)
# print("Solution: return value of the function is", ret2, ".")

