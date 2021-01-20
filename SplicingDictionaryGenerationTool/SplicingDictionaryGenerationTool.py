import sys
import optparse
import sys
import os

print(''' __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/
                             by capOnKing
=====================================================''')

def cmdParam():
    global options,args
    parse = optparse.OptionParser(usage = "%prog A.txt B.txt C.txt\n",version = "v1.0")   #实例化命令行参数    
    options,args = parse.parse_args()
    if len(sys.argv) != 4:
        sys.exit("[!]传入参数不完整，请检查！或运行 -h 指令")
    
def readFiles(fileName):
    listTemp = []
    with open("targets\\" + fileName) as f:
        listTemp = f.read().splitlines()      
    listTemp = set(listTemp)
    listTemp = list(listTemp)    
    return listTemp
    
def allKindsOfCombination():
    strTemp = ''
    global f
    print("[+]正在读取文件")
    print("[+]同时为目标去重")
    try:    
        for i in range(len(sys.argv) - 1):
            globals()['list'+str(i + 1)] = readFiles(sys.argv[i + 1])       #动态创建全局变量,传入3个字典就是3个变量
    except Exception as e:
        sys.exit("[!]检查需读取的文件是否存在！")
    print("[+]读取文件完成")
    print("[+]目标去重已结束")
    len1 = len(list1)
    len2 = len(list2)
    len3 = len(list3)
    if len1 == 0:
        len1 = 1
        list1.append('')
    if len2 == 0:
        len2 = 1
        list2.append('')
    if len3 == 0:
        len3 = 1
        list3.append('')    
    print("[+]预计产生{}种结果".format(len1*len2*len3))
    print("[+]正在写入文件")
        
    for i in list1:                                                     #ABC
        for j in list2:
            for k in list3:
                strTemp += i + j + k + '\n'
    try:            
        f = open("results\\allKindsOfCombination.txt",'w')
    except Exception as e:
        os.system('mkdir results')    
    finally:
        f.write(strTemp)
        f.close()
        print("[+]字典已保存至:" + os.getcwd() + "\\results\\allKindsOfCombination.txt")    
def main():
    cmdParam()
    allKindsOfCombination()
    
if __name__ == "__main__":
    main()    