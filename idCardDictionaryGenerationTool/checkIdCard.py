import sys
# t代表身份证号码的位数，w表示每一位的加权因子
t = []
w = []
for i in range(0,18):
    t1 = i + 1
    t.append(t1)
    w1 = (2 ** (t1-1)) % 11
    w.append(w1)
#队列w要做一个反序
w = w[::-1]  

# 根据前17位的余数，计算第18位校验位的值
def for_check(n):
    # t = 0
    for i in range(0,12):
        if (n + i) % 11 == 1:
            t = i % 11
    if t == 10:
        t = 'X'
    return t
    
# 根据身份证的前17位，求和取余，返回余数
def for_mod(id):
    sum = 0
    for i in range(0,17):
        sum += int(id[i]) * int(w[i])
        # print(int(id[i]),int(w[i]),sum)
    sum = sum % 11
    # print(sum)
    return sum

# 验证身份证有效性
def check_true(id):
    # print(for_check(for_mod(id[:-1])))
    if id[-1] == 'X' or id[-1] == 'x':
        if for_check(for_mod(id[:-1])) == 'X' or for_check(for_mod(id[:-1])) == 'x':
            return True
        else:
            return False
    else:
        if for_check(for_mod(id[:-1])) == int(id[-1]):
            return True
        else:
           return False
           
def finaList(resultList):
    temList=[]
    try:
        for i in range(len(resultList)):
            if check_true(resultList[i]) and len(resultList[i]) == 18:
                temList.append(resultList[i])
            else:
                pass  
    except Exception as e:
        sys.exit("出现异常，请检查输入，程序退出")    
    return temList