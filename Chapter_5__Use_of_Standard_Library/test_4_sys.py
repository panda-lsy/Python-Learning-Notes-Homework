import sys
print("命令行参数有：", str(sys.argv))
for i in range(len(sys.argv)):
    print("第", i, "个参数：", sys.argv[i])