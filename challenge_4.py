def division(num):
    return num / 2

num = input('何か数字を入力してください：')
num = int(num)
result = int(division(num))
print(result)

def kakezan(num2):
    return num2 * 4

num2 = 123
result2 = kakezan(num2)
print(result2)

num2 = result
result = kakezan(num2)
print(result)