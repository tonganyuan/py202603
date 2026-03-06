from pathlib import Path
file_path = Path('file_test/pi_digits.txt')
content = file_path.read_text()
print(content)
lines = content.splitlines()
index= 1
result = ''
for line in lines:
    print(f"第{index}行为{line}")
    index+=1
    result+=line
print(result)
birthday = input("请输入你的生日")
if(birthday in result):
    print("你的生日在圆周率中")
else:
    print("抱歉 你的生日不在圆周率中")