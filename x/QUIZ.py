#1번
import math
price = 59827
print(f'{round(price, -2)}원')

# -------------------------

print(price//100*100)
print(price-price%100)
print(math.floor(price/100)*100)
print(int(price/100)*100)

#2번
score = 56
print(f'{round(score, -1)}점')
score1 = 93
print(f'{round(score1, -1)}점')

# ------------------------------

print(round(score/10)*10)
print(round(score, -1))

#3번
import random
lotto = random.sample(range(1, 46), 6)
print(lotto)

# -------------------------------
#
# print(random.sample(range(1, 45+1)))

#4번
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = []
for i in range(3):
    number = random.choice(list2)
    list3.append(str(number))
    list2.remove(number)
print(list3[0] + list3[1] + list3[2])

# -----------------------
# l = random.sample(range(1, 9+1), 3)
# print(l)
# print(str(l))
# print("".join(n)for n in l)
# print("".join(map(str, l)))


# 5번
import datetime
now = datetime.datetime.now()
birthday = datetime.datetime(2004,7, 9)
left = now - birthday
print(left.days,'Days')

# ------------------------
now = datetime.datetime.now()
birthday = datetime.datetime(2004,7, 9)
print(now - birthday)


# 6번
import datetime
now = datetime.datetime.now()
xmas = datetime.datetime(2021,12,25)
left = xmas - now
print(left.days, 'Days')

# ---------------------


# 7번
import datetime
fu = datetime.datetime(2022, 7, 9)
now = datetime.datetime.now()
left = fu - now
print(left.days, 'Days')

# -----------------------------

mb = datetime.datetime(2021,7,9)
if mb < now:
    mb = mb.replace(year=2022)

print(mb - now)

#8번

# 마지막 번호 묻기
last_number = input("마지막 번호 :")
# 1~ 마지막번호까지 리스트 만들기
list_class = list(range(1, int(last_number)+1))

while True:
# 뺄 번호 묻고 빼기 반복
    exclude_number = input("뺄 번호(enter = stop) : ")
    if exclude_number == '':
        break
    list_class.remove(int(exclude_number))
    print(list_class)
# 다 뺏으면 반복 끝내기
random.shuffle(list_class)
# 섞고 출력하기
print(f'자리\t학생번호')
for i,number in enumerate (list_class):
    print(f'{i}\t{number}')
