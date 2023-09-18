import requests
import time
import execjs

with open('encrypt.js', 'r', encoding='UTF-8') as f:
    js_code = f.read()
context = execjs.compile(js_code)

payload = {
    "act_id": "164047",
    "buy_ticket_type": "PC",
    "time": int(time.time()),
}

url = "http://gdjt.tongji.edu.cn/Swoole/push.json"

encrypted_data = context.call("encrypt", payload)
token = context.call("encrypt", str(int(time.time())) + '@tj')
payload = f"act_str={encrypted_data}"

headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Agent-Type': 'pc',
  'Cache-Control': 'no-cache',
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'Cookie': 'Hm_cv_7543ad4d5aca565a9ba0da0cc74c4eb7=1*visitor*PC; pwapp_unbs=10227954; pwapp_ext_sid=2333078; pwapp_uname=%E5%AE%89%E6%B1%9F%E6%B6%9B; tokens=4d7647498933388f06add012dc473f19; connection_id=ef141cff8e4d3fadd39ebc357dd85394; YXMC=%E8%BD%AF%E4%BB%B6%E5%AD%A6%E9%99%A2; IS_YXMC=10227954; PHPSESSID=of7g43ra8nke4ka4590b1i7lit; Hm_lvt_7543ad4d5aca565a9ba0da0cc74c4eb7=1694566473,1694750545,1694935063,1694997586; think_language=zh-CN; Hm_lpvt_7543ad4d5aca565a9ba0da0cc74c4eb7=1695011267',
  'Origin': 'http://gdjt.tongji.edu.cn',
  'Pragma': 'no-cache',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://gdjt.tongji.edu.cn/PC/',
  'Token': token,
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'
}

session = requests.session()

resp = session.post(url, headers=headers, data=payload)

data = resp.json()
print(data)

