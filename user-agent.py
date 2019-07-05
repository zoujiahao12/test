import random
import urllib.request
import urllib.parse
import string

def main():
    url ="https://www.baidu.com/s?wd="
    url +="User-Agent"
    url =urllib.parse.quote(url,safe=string.printable)
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
    user_agent =random.choice(user_agents)
    header ={
        "User-Agent":random.choice(user_agents),
    }
    resquest = urllib.request.Request(url,headers=header)
    resp = urllib.request.urlopen(resquest)
    data=resp.read().decode("utf-8")
    with open("04.html","w") as f:
        f.write(data)
if __name__=="__main__":
    main()
