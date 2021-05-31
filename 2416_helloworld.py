print("hello world")
print("-----------------------------")


def solution(characters):
	result = ""
	result += characters[0]
	for i in range(1, len(characters)):
		if characters[i - 1] != characters[i]:
			result += characters[i]
	return result


characters = "pcjikimi"
ret = solution(characters)

print(ret)