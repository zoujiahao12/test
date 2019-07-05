import requests
import re


def main():
    url = "https://www.sina.com.cn/"
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    resp = requests.get(url, headers=header)
    data = resp.content.decode("utf-8")

    pattern = re.compile("""<a target="_blank" href="(.*)">(.*)</a>""")
    ret = pattern.findall(data)
    lst = []
    for i in ret:
        x = (i[0], i[-1])
        lst.append(x)


    html = """<html>
<head>
  <title>this is my world</title>
    <meta name = "keyword" content = "">
    <meta name = "description" content ="nuibi"> 

</head>
  
<body>
<ul>
"""
    for i in lst:
        html += """<li><a target="_blank" href="""
        html += i[0]
        html += """">"""
        html += i[1]
        html += """</a>"""

    with open("12.html", "w", encoding="utf-8") as f:
        f.write(html)



if __name__ == "__main__":
    main()