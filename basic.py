# coding:utf-8

print "hello world!"

a = 1
a = 3.14

print type(a)
print "%s is %f" % ("PI", a)

# 条件语句
b = 9.8
if a > b:
    print "a>b"
else:
    print "a<=b"

if a != b:
    print "a!=b"

if a <> b:
    print "a<>b"

if not a > b:
    print "not a>b"

# 逻辑或
c = 123

if a <> b or a <> c:
    print "yes"

if a == b:
    pass
elif a == c:
    pass
else:
    print "in else"

### 文件读写
# 方法一
file = open("input.txt")
line = file.readline()
index = 0
while line:
    index += 1
    print index, " ", line,  # ,去掉换行
    line = file.readline()
file.close()

# 方法二
for index, line in enumerate(open("input.txt")):
    print index, ":", line,

# 方法三
with open("input.txt") as file:
    while line:
        print line,
        line = file.readline()
print

# 写文件方法
with open("output.txt", "w") as file:
    pass
    # name = raw_input('请输入你的名字')
    # output_str = "你的名字是 " + name

    # print output_str,

    # file.writelines(output_str)

a_byte_str = "你好"
a_unicode_str = a_byte_str.decode("UTF-8")

print a_byte_str.decode("UTF-8")[0]

a_byte_str = "abcdef"

print "#" * 20
print a_byte_str[0:1]

# 字符串拼接
print "#" * 20

a_str = "hello"
b_str = "world"

print a_str + b_str

print int("12345") + 0.1222

x = 3.4515926
print repr(x)

print type(repr(x))
