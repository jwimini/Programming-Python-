import pickle

from person import Person

# 객체 생성하기
번호15 = Person('이재령', '흰색')
번호17 = Person('임사랑', '핑크')

# 리스트로 만들어서
칭긔 = [번호15, 번호17]
print(칭긔)
for 친구 in 칭긔:
    print(친구)

# 저장하기
# 1. 객체 하나 저장
import pickle

with open('object.bin', 'wb') as f:
    pickle.dump(번호15, f)

# 2. 객체 여러 개 저장
with open('objects.bin', 'wb') as f:
    pickle.dump(친구, f)
