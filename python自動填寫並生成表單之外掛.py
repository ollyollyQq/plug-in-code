import re
import time
import random
import numpy as np
import requests as rq

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSc6JyO1uxqtbs306zBVidz026ftrTXYTXYE1zsQvP7g3lo0Sw/formResponse'
params1 = ['男性', '女性', '其他']
params2 = ['國中(含)以下', '高中(職)', '大學(專)', '研究所(含)以上']
params3 = ['0~20', '21~30', '31~40','41~50','51~60','61~70','71以上']
params4 = ['自由業', '工', '商','服務業','學生','家管','退休','軍公教','科技業']
params5 = ['1', '2', '3', '4', '5']
params6 = ['熱心程度', '講話語氣', '出餐速度','服務態度']
params7 = ['1', '2', '3', '4', '5']
params8 = ['用餐時間', '出餐速度', '餐點價格','氣氛氛圍','知名度','餐點特色','餐點新鮮度']
params9 = ['第 1 次', '2 - 3次', '4 - 6 次', '6 次以上', '來過，但忘記次數']
params10 = ['親友介紹', '宣傳傳單', '網路資訊','經過看到','其他管道']
payload = {
    'entry.153422456': '',
    'entry.1585855828': '',
    'entry.515399826': '',
    'entry.1426910999': '',
    'entry.2093759101': '',
    'entry.1238736199': '',
    'entry.2117956366': '',
    'entry.773854276': '',
    'entry.1890425713':'',
    'entry.519952701':'',
    'fvv' : '0',
    'draftResponse' : '[]',
    'pageHistory' : '0',
    'fbzx' : '-882713142179927034'
}
num = 100  # 執行次數
period = np.arange(0.5, 5.0, 0.1)
delay = 0  # 延遲時間
while num > 0:
    try:
        payload['entry.153422456'] = random.choice(params1)
        payload['entry.1585855828'] = random.choice(params2)
        payload['entry.515399826'] = random.choice(params3)
        payload['entry.1426910999'] = random.choice(params4)
        payload['entry.2093759101'] = random.choice(params5)
        payload['entry.1238736199'] = random.choice(params6)
        payload['entry.2117956366'] = random.choice(params7)
        payload['entry.773854276'] = random.choice(params8)
        payload['entry.1890425713'] = random.choice(params9)
        payload['entry.519952701'] = random.choice(params10)
        res = rq.post(url, data=payload)
        res.raise_for_status()
        if res.status_code == 200 :
            delay = round(random.choice(period), 2)  # round off to the 2nd decimal place
            print('Fill Out : ' + payload['entry.153422456'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.1585855828'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.515399826'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.1426910999'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.2093759101'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.1238736199'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.2117956366'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.773854276'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.1890425713'] + ' delay : ' + str(delay) + ' sec')
            print('Fill Out : ' + payload['entry.519952701'] + ' delay : ' + str(delay) + ' sec')
            time.sleep(delay)
    except rq.HTTPError:
        print('HTTP Error!')
    
    num -= 1
