import os

# path = input('请输入文件路径(结尾加上/)：')
path = "dataset/valid/front"

# 获取该目录下所有文件，存入列表中
files = os.listdir(path)

n = 0
for i in files:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + files[n]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = path + os.sep + 'f-' + str(n + 1) + '.jpg'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    n += 1
