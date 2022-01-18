import os

def re_fileName(path):
    fileList = os.listdir(path)
    num=1
    for file in fileList:
        used_fileName,extension = os.path.splitext(file)
        new_file = '轨迹捕获0'+str(num+8)+extension;#加一个零的文件num要加8
        os.rename(file, new_file)
        print("文件%s重命名成功，新的文件名为：%s" %(path+file, path+new_file))
        num += 1
    
if __name__=='__main__':
    path = os.getcwd()   # 获取当前目录
    re_fileName(path)
