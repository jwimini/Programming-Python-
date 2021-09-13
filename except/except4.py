list = [1,2,3]

try:
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])
except ValueError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print('error')
else:
    print('It does work well')
finally:
    print('finally')