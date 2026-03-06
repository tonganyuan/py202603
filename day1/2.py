message = input("输入些文字，我会打印出来:\n")
print(message)
message = int(message)
print(message > 12)
if message > 12:
    print("大于12")
elif message < 12 :
    print("小于12")
else:
    print("等于12")