import urllib.request
def main():
    url="https://www.yaozh.com/member/"
    header ={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Cookie": "acw_tc=2f624a2b15613579132751512e26beb378ae0e864b06fbdff95a9c6b0a6d82; PHPSESSID=4qssrvm7fg0hdmsq6tcdm664i4; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1561357914; _ga=GA1.2.132073277.1561357914; _gid=GA1.2.897522284.1561357914; MEIQIA_VISIT_ID=1N5534IzO5IUBk6ZxcnWRTBPMQ9; MEIQIA_EXTRA_TRACK_ID=1N5530e5NFp3Pei0VxeYoEvMMZI; yaozh_logintime=1561358176; yaozh_user=774633%09zoujiahao; yaozh_userId=774633; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1561358179; yaozh_uidhas=1; yaozh_mylogin=1561358181; acw_tc=2f624a2b15613579132751512e26beb378ae0e864b06fbdff95a9c6b0a6d82; MEIQIA_VISIT_ID=1N5534IzO5IUBk6ZxcnWRTBPMQ9; MEIQIA_EXTRA_TRACK_ID=1N5530e5NFp3Pei0VxeYoEvMMZI"

     }
    request = urllib.request.Request(url, headers=header)
    proxy = {
        "http": "http://163.204.242.234:9999"
    }
    data=urllib.request.urlopen(request).read().decode("utf-8")
    with open("08.html","w") as f:
        f.write(data)
if __name__=="__main()__":
    main()