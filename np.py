import urllib.request
def main():
    url="https://github.com/humstarman/bigdata-04/blob/master/proxy.py"
    header={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    request =urllib.request.Request(url,headers=header)
    proxy={
        "http":"http://163.204.242.234:9999"
    }
    handler=urllib.request.ProxyHandler(proxy)
    opener =urllib.request.build_opener(handler)
    data=opener.open(request).read().decode("utf-8")
    with open("07.html","w") as f:
        f.write(data)

if __name__=="__main__":
    main()