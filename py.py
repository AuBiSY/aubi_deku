print('hello world!')
print('hello', 'world!')  # 逗号自动添加空格
print('hello' + 'world!')  # 加号表示字符拼接
print('hello', 'world', sep='***')  # 单词间用***分隔
print('#' * 50)  # *号表示重复50遍
print('how are you?', end='') # 默认print会打印回车，end=''表示不要回车


username = input('username: ')
print('welcome', username)
print('welcome ' + username)

number = input("请输入数字: ")  # input用于获取键盘输入
print(number)  # input获得的数据全是字符

print(number + 10)  # 报错，不能把字符和数字做运算

print('hello world!')

if 3 > 0:
    print('OK')
    print('yes')

x = 3; y = 4   # 不推荐，还是应该写成两行
print(x + y)

print(5 / 2)  # 2.5
print(5 // 2)  # 丢弃余数，只保留商
print(5 % 2)  # 求余数
print(5 ** 3)  # 5的3次方
print(5 > 3)  # 返回True
print(3 > 5)  # 返回False
print(20 > 10 > 5)  # python支持连续比较
print(20 > 10 and 10 > 5)  # 与上面相同含义
print(not 20 > 10)  # False




