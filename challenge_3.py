a = input('何か数字を入力してください：')
b = input('何か数字を入力してください：')
c = input('何か数字を入力してください：')

a = int(a)
b = int(b)
c = int(c)

def keisan(a, b, c, y = 1, z = 2):
    return a * b + c * (y + z)

result = keisan(a, b, c, y = 1, z = 2)
print(result)
