import requests
import numpy as np

url = 'https://qt.gtimg.cn/q='

resp = requests.get(url + 'sh600036').text
raw = resp.split("~")
print(raw)
