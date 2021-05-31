phone_number1 = "010-2540-5357"
phone_number2 = "010 7584 1367"
phone_number3 = "01073201685"

result = phone_number1.replace("-",' ').replace(' ','')
print(result)
# -----------------------------------
# range # 시작은 포함 stop 은 포함X
# range(start, stop)
# range( start, stop, step)
# start <= 숫자 <stop

range(1,11,2) # 2는 2칸씩 뛴다는 말
range(10,1,-2)

# ----------------------------------------

# 구구단 7단 출력하기
# i : 1~ 9
# for i in range(1, 10):
#     print(f'7 x {i} = {7*i}')

# 구구단 2~9단 출력하기
for dan in range(2, 10):
    print()
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')

print("----------------------------------------")


# 구구단 2 ~ 7 출력 break
for dan in range(2, 10):
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')
    print()
    if dan == 7:
        break

print("----------------------------------------")
# 구구단 2~7단까지 1 3 5 7 9  출력하기 break coutinue
for dan in range(2, 10):
    for i in range(1,10):
        if i % 2 == 0: #i == 2  or i == 4 or i == 6 or  i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print()
    if dan == 7:
        break

print("----------------------------------------")
def get_three_six_nine(num):
    num = str(num)
    if(num.count("3") >=1 or num.count("6") >=1 or num.count("9") >=1):
        return "짝"*(num.count("3")+num.count("6")+num.count("9"))
    else:
        return num

result = get_three_six_nine(1)
print(result)
result = get_three_six_nine(3)
print(result)
result = get_three_six_nine(36)
print(result)