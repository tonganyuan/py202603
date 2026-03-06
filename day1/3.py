# message = ''
# while (message != 'exit'):
#     message = input("请输入数字 输入exit将推出")
#     print(message)
# print("安全退出")
pets = ['cat','cat','pig','tiger','cat','dog']
while 'cat' in pets:
    print(pets.pop())
print(pets)
def getUser(username,age = 12):
    print(f"用户名称：{username} 年纪：{age}")
getUser(age=11)