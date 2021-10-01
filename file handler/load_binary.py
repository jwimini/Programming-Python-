with open('binary.bin', 'rb') as f:
    data = f.read()
print(data)     # b'\xff\x00\x7f' 2진수를 16진수로 표현하였다.