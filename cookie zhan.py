import requests
def main():
    session = requests.session()
    url="https://www.yaozh.com/login/"

    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    form = {
      "username": "zoujiahao",
      "pwd": "zoujiahao12",
      "formhash": "96E3583F3E",
      "backurl": "https%3A%2F%2Fwww.yaozh.com%2F",
    }
    login_resp = session.post(url,headers=header,data=form)
    m_url = "https://www.yaozh.com/member/"
    data = session.get(m_url,headers=header).content.decode("utf-8")
    with open("09.html","w",encoding="utf-8") as f:
        f.write(data)
if __name__=='__main__':
    main()