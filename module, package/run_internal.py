# #math
# import math
# print(math.ceil(3.5))       # ceil : 천장, 올림
# print(math.floor(3.5))      # floor : 바닥, 내림
# print(round(3.5))           # round:반올림
# print(round(3.4))           # round : 반올림
# print(math.pow(2,10))
# print(math.sin(math.pi/2))
# # random
# import random
# print(random.random())
# print(random.randrange(1,10))
# print(random.randint(1,10))
# list1 = ['굶었씀', '피자','김치찜','닭 찌찌']
# print(random.choice(list1))         #list1중 하나
#
#
# print(list1)
# print(random.shuffle(list1))
# print(list1)
#
# print(random.sample(list1,2))

#dtetime
import datetime
now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.hour)
birthday = datetime.datetime(2004, 7, 9)
print(birthday)
print(now - birthday)