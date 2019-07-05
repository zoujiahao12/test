
import urllib.request
import urllib.parse
import string
def main():
   # url="http://www.baidu.com/s?wd="
    #url +="大数据"
    url = "http://y.qq.com/"
    print(url)
    url =urllib.parse.quote(url,safe=string.printable)
    print(url)

    resp =urllib.request.urlopen(url)

    data =resp.read().decode("utf-8")

    print(resp)
    print(data)

    with open("01.html","w") as f:
        f.write(data)


if __name__=="__main__":
    main()