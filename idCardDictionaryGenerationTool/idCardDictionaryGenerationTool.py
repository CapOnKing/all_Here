import sys
import re
import calendar
import time
import os
import math
import hashlib
from checkIdCard import finaList

def isLeapYear(a_year,a_month):   #判断是否闰年，返回相应月份的天数
    Mday_R = [31,29,31,30,31,30,31,31,30,31,30,31]                #闰年
    Mday_P = [31,28,31,30,31,30,31,31,30,31,30,31]                #平年
    a_month_pox = []
    Mday_temp = []
    for i in range(len(a_month)):                               #记录月份对应天数的下标
        a_month_pox.append(int(a_month[i]) - 1)        
    for i in range(len(a_year)):        
        a_year[i] = int(a_year[i])
        if calendar.isleap(a_year[i]):
            for j in range(len(a_month_pox)):
                Mday_temp.append(Mday_R[a_month_pox[j]])
            
        else:
            for j in range(len(a_month_pox)):
                Mday_temp.append(Mday_P[a_month_pox[j]])
        a_monthDay.append(Mday_temp[:len(a_month)])             #循环会多给Mday_temp值，所以用这个截取掉多给的值
        a_year[i] = str(a_year[i]).zfill(4)        
    return a_monthDay                                           #二维列表[[1,2],[3,4]]
 
#对逗号，横杠组合输入的处理，第二个参数是补零位数,第三个参数用来判断是不是月份的传参 
def inputCue(inputResult,zfillNum,num):         
    if inputResult == "a" and num == 0 or len(inputResult) == 0 and num == 0:
        inputResult = "1,2,3,4,5,6,7,8,9,10,11,12"
    a_temp_input = []                                                #长度肯定为2
    a_temp2_input = []                                               #保存-的形式的年份
    a_temp3_input = []
    inputResult = list(filter(None, re.split(r'[;,\s]\s*',inputResult)))      #先以逗号进行分割，并过滤空值
    for s in range(len(inputResult)):
        if "-" in inputResult[s]:                              #再以"-"分割处理类似1974-1980的格式
            a_temp_input = inputResult[s].split("-")
            tempAbsNum = abs(int(a_temp_input[1]) - int(a_temp_input[0])) + 1
            for i in range(tempAbsNum):   #绝对值，以防输反
                if int(a_temp_input[1]) >= int(a_temp_input[0]):
                    a_temp2_input.append(str(int(a_temp_input[0]) + i))
                if int(a_temp_input[1]) <= int(a_temp_input[0]):
                    a_temp2_input.append(str(int(a_temp_input[1]) + i))    
        else:
            a_temp3_input.append(inputResult[s])
    inputResult = a_temp2_input + a_temp3_input
    for s in range(len(inputResult)):                                   #补零操作
        inputResult[s] = inputResult[s].zfill(zfillNum)
    return inputResult
    
def explainFunction():   
    print("\n-----------------------功能简介-----------------------\n\n1.必须知道用户省份城市县区，这样可确认前6位，前6位可多个输入，如：610221,320521")
    print("2.年份可多个输入，如：1850,1949-1951")
    print("3.月份可多个输入，日子同理，如：1,5,10-12")
    print("4.以防结果生成太多，能少输入就少输入\n")
    print("------------------------------------------------------")
    print("本程序未对用户输入做太多过滤，请自行检查输入！\n")
def publicVariable():                                                   #定义一些全局变量
    global oneToSix,a_year,a_month,a_monthDay,sTwo,allSex,lastOne,randomStr

    randomStr = "qm"        #用来判断输入的日子是一个固定数还是需要遍历的数（12月30日，12月1-30日）
    oneToSix = input("请输入省份城市区县（六位）：")
    if len(oneToSix) < 6:
        oneToSix = "320100"
    oneToSix = inputCue(oneToSix,6,1)
    #过滤身份证前六位列表的空值
    for i in range(len(oneToSix)):                                      #只取6位
        oneToSix[i] = oneToSix[i][0:6]
        
    a_year = input("请输入出生年份：")
    a_year = inputCue(a_year,4,1)
  
    a_month = input("请输入出生月份(不清楚则请回车保持默认)：")
    a_month = inputCue(a_month,2,0)
    a_month.sort()
    
    a_monthDay=[]
    a_temp_monthDay = input("请输入准确日子(不清楚则请回车保持默认)：")   
    if len(a_temp_monthDay) == 0 or a_temp_monthDay == "a":    
        a_monthDay = isLeapYear(a_year,a_month)                                              #二维列表[[1,2],[3,4]]  
    else:        
        a_monthDay.append(randomStr)
        a_temp_monthDay = inputCue(a_temp_monthDay,2,1)    
        a_monthDay.append(a_temp_monthDay)
        
    sTwo=[]                                                                          #身份证最后四位的前两位
    for i in range(0,100):        
        tmp=str(i).zfill(2)                                      
        sTwo.append(tmp)    
       
    seX=input("请输入性别（女[0] 男[1] 不清楚则请回车保持默认）：")                  #性别
    if seX == "1":
        allSex=["1","3","5","7","9"]
    elif seX == "0":
        allSex=["0","2","4","6","8"]
    else: 
        allSex=["0","1","2","3","4","5","6","7","8","9"]  
          
    lastOne=['0','1','2','3','4','5','6','7','8','9','x','X']                        #身份证最后一位

def idCardRound1(lenth):
    resultList = []   
    for i in range(lenth):
        s1 = oneToSix[i]
        idCardRound2(len(a_year),s1,resultList) 
    return resultList      
def idCardRound2(lenth,s1,resultList):
    temCount = 0   
    for i in range(lenth):
        s2 = a_year[i]
        idCardRound3(len(a_month),s1,s2,resultList,temCount)
def idCardRound3(lenth,s1,s2,resultList,temCount):
    if a_monthDay[0] == randomStr:
        for i in range(lenth):
            s3 = a_month[i] 
            for j in range(len(a_monthDay[1])):                   #a_monthDay ['qm',[31,29,31]]
                s4 = a_monthDay[1][j]
                idCardRound4(len(sTwo),s1,s2,s3,s4,resultList)
    else:             
        for i in range(lenth):               #输入的月份
            s3 = a_month[i]                                                             #a_monthDay [[31,29,31],[31,28,31]
            for j in range(1,a_monthDay[temCount][i] + 1):       #k:1-31,1-29,1-31 
                s4 = str(j).zfill(2)
                idCardRound4(len(sTwo),s1,s2,s3,s4,resultList)
        temCount += 1        
def idCardRound4(lenth,s1,s2,s3,s4,resultList):
    for i in range(lenth):
        s5 = str(sTwo[i]).zfill(2)
        idCardRound5(len(allSex),s1,s2,s3,s4,s5,resultList)
def idCardRound5(lenth,s1,s2,s3,s4,s5,resultList):   
    for i in range(lenth):       
        s6 = allSex[i]
        idCardRound6(len(lastOne),s1,s2,s3,s4,s5,s6,resultList)
def idCardRound6(lenth,s1,s2,s3,s4,s5,s6,resultList):
    for i in range(lenth):
        s7 = lastOne[i]
        #print(s1+s2+s3+s4+s5+s6+s7)
        resultList.append(s1+s2+s3+s4+s5+s6+s7)
        if len(resultList) % 100000 == 1:
            print("已完成{:.0f}%".format(len(resultList)/guessCount*100),end="\r")        
def idCardSplit():
    global guessCount
    guessCount = 0
    if a_monthDay[0] == randomStr:                      #["qm",[31,20]]
        g = len(a_monthDay[1])
        guessCount = len(oneToSix) * len(a_year) * g * len(sTwo) * len(allSex) * len(lastOne)
    else:
        g = 0
        for i in range(len(a_monthDay)):                #[[31,29],[31,28]]
            for j in range(len(a_monthDay[i])):
                g += int(a_monthDay[i][j])
        guessCount = len(oneToSix) * g * len(sTwo) * len(allSex) * len(lastOne)        
    print("[+]预计产生{}种可能性".format(guessCount))    
    resultList = idCardRound1(len(oneToSix))                         #将每层循环写成方法，共6个循环
    return resultList

def printList():
    resultList = idCardSplit()  
    if len(resultList)==len(set(resultList)):
        print("[+]没有重复值")
    else:
        print("[!]重复（调试用）")            
    resultList = finaList(resultList)        #校验下身份证合法性
    print("[+]正在进行身份证校验")
    print("[+]经过校验后共计{}个身份证生成结果".format(len(resultList)))
    print("[+]正在写入...")  
    m5_1 = hashlib.md5(str(time.time()).encode(encoding='UTF-8')).hexdigest()
    fileName = "IdCard_18_" + m5_1 + ".txt"
    with open(fileName,'w') as f:
        for i in range(len(resultList)):
            f.write(resultList[i])
            if i==len(resultList)-1:
                break
            f.write("\n")
    m5_2 = hashlib.md5(str(time.time()).encode(encoding='UTF-8')).hexdigest()
    fileName2= "IdCard_6_" + m5_2 + ".txt"
    with open(fileName2,'w') as f:
        for i in range(len(resultList)):
            f.write(resultList[i][-6:])
            if i==len(resultList)-1:
                break
            f.write("\n")        
    print("[+]身份证18位已存入：{}".format(os.getcwd()+"\\"+fileName)) 
    print("[+]身份证最后6位存入：{}中".format(os.getcwd()+"\\"+fileName2))        
    
if __name__ == "__main__":
    explainFunction()
    publicVariable()
    printList()