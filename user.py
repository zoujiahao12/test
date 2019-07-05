import urllib.request
import urllib.parse
import string

def main():
    url ="https://www.baidu.com/s?wd="
    url +="大数据"
    url =urllib.parse.quote(url,safe=string.printable)
    header ={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=header)
    resp =urllib.request.urlopen(request)
    data=resp.read().decode("utf-8")
    with open("02.html","w") as f:
        f.write(data)
if __name__=="__main__":
    main()