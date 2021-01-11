import base64
import binascii
import sys
import re

def base64T():
    print("1.base64编码\n2.base64解码\n-----------------------------\n")
    a=input("[+]请输入选项：")
    try:
        if a=="1":
            b=input("[+]请输入要编码的字符：")
            b=b.encode(encoding = "utf-8")  #转bytes
            b=base64.b64encode(b)
            print(str(b)[2:-1])
        elif a=="2":
            b=input("[+]请输入要解码的字符：")
            print(str(base64.b64decode(b),'utf-8'))
            
        else:
            sys.exit("[!]请检查输入，已退出!")
    except Exception as e:
        sys.exit("[!]编码格式似乎不是base64，请更换其他编码解码。")
        
def hexT():
    print("1.hex编码\n2.hex解码\n-----------------------------\n")
    a=input("[+]请输入选项：")
    try:
        if a=="1":
            try:
                b=input("[+]请输入要编码的字符：")
                print(str(binascii.b2a_hex(b.encode('utf-8')))[2:-1]) 
            except Exception as e1:    
                s=binascii.hexlify(b)
                print(s.decode('utf-8'))  #bytes类型，转化为str类型
        elif a=="2":
            try:
                b=input("[+]请输入要解码的字符：")
                s=binascii.unhexlify(b)  #unhexlify()传入的参数也可以是b'xxxx'(xxxx要符合16进制特征)
                print(s.decode('utf-8')) #s的类型是bytes类型，用encode()方法转化为str类型
            except Exception as e1:
                print("".join([chr(i) for i in [int(j,16) for j in b.split(' ')]]))  
        else:
            sys.exit("[!]请检查输入，已退出!")
    except Exception as e:
        print(e)
        sys.exit("[!]编码格式似乎不是hex，请更换其他编码解码。")

def asciiT():
    print("1.ascii编码\n2.ascii解码\n-----------------------------\n")
    a=input("[+]请输入选项：")
    try:
        if a=="1":
            b=input("[+]请输入要编码的字符：")
            s = ''
            for i in b:
                s += 'chr(' + str(ord(i)) + '),'
            print(s[:-1])
        elif a=="2":
            b=input("[+]请输入要解码的字符(只要有数字，以某符号分割就行，如97,98)：")
            pattern = re.compile("\d+")
            b = pattern.findall(b)
            for i in b:               
                exec("print(chr(" + i +"),end = '')")
        else:
            sys.exit("[!]请检查输入，已退出!")
    except Exception as e:
        sys.exit(e)

def unicoedT():
    print("1.unicode编码\n2.unicode解码\n-----------------------------\n")
    a=input("[+]请输入选项：")
    try:
        if a=="1":
            b=input("[+]请输入要编码的字符：")
            print(b.encode('unicode_escape').decode("utf-8"))
        elif a=="2":
            b=input("[+]请输入要解码的字符：")
            print(b.encode('utf-8').decode("unicode_escape"))
        else:
            sys.exit("[!]请检查输入，已退出!")
    except Exception as e:
        sys.exit(e)

if __name__ == "__main__":
    print("\n1.base64\n2.hex\n3.Ascii\n4.unicode\n-----------------------------\n")
    a=input("[+]请输入选项：")
    try:
        if a=="1":
            base64T()
        elif a=="2":
            hexT()
        elif a=="3":
            asciiT()
        elif a == "4":
            unicoedT()        
        else:
            sys.exit("[!]请检查输入，已退出!")
    except Exception as e:
        sys.exit("[!]输入错误！")    