from bs4 import BeautifulSoup
import requests
import os
import urllib.request,urllib.error
import pprint
import copy
from tkinter import *
from PIL import Image, ImageTk


headers = {
			'Referer': 'https://www.bilibili.com/?spm_id_from=333.999.0.0',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
            'accept':'application/json, text/plain', 
            'accept-encoding': 'utf-8',
            'accept-language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7',
            'cookie':"i-wanna-go-back=-1; _uuid=2D10461AA-4F7B-A821-38A2-3C348818E10C745014infoc; buvid4=D48DA0D7-6AB3-1FD0-12B2-05969D23A11153353-022061310-dWliG5BMrUYxKlic3N6aCQ%3D%3D; CURRENT_BLACKGAP=0; blackside_state=0; buvid_fp_plain=undefined; nostalgia_conf=-1; LIVE_BUVID=AUTO6916553482251014; hit-dyn-v2=1; buvid3=7A10962F-4E21-4A2E-89DD-3EAFD6023BE2167646infoc; b_nut=100; fingerprint3=789d9ac98cc57570875d46834645f582; go_old_video=-1; rpdid=|(umkYYm|Y)J0J'uYY)lmum)Y; SESSDATA=2a7da8bf%2C1686231175%2Cad5e8%2Ac2; bili_jct=d5a71862bcb497c79635bcc4c78f458e; DedeUserID=98621683; DedeUserID__ckMd5=6ea2e96cab511054; b_ut=5; is-2022-channel=1; header_theme_version=CLOSE; CURRENT_QUALITY=116; hit-new-style-dyn=1; go-back-dyn=0; CURRENT_PID=5f2342e0-cef1-11ed-8d31-d9b6ec1d5c93; FEED_LIVE_VERSION=V_TOPSWITCH_FLEX; sid=5v4fsnq6; bsource=search_baidu; fingerprint=7b3360f7109bbe249918def7a01a4bf7; CURRENT_FNVAL=4048; bp_video_offset_98621683=791037636445733000; home_feed_column=5; browser_resolution=1707-849; innersign=1; buvid_fp=67cbe6759a70980471d8629cbab6b103; PVID=11; b_lsid=124AABEC_187DBE796FE",
            'origin':'https://space.bilibili.com',
            'referer': 'https://space.bilibili.com/1340190821/video',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
        }
link='https://api.bilibili.com/x/space/wbi/arc/search'
global params
params={
    'mid': 5,
    'ps': 30,
    'tid': 0,
    'pn': 1,
    'keyword':'',
    'order':'pubdate',
    'platform': 'web',
    'web_location': 1550101,
    'order_avoided': 'true',
    'w_rid': '3c81e6c1043493919f573429f7897345',
    'wts': 1683028490,
    }

def download(num,href):
    html = requests.get(url=href, headers=headers).content
    file = 'E:\Spider\img\\'
    filename = file + str(num) + '.jpg'
    if not os.path.exists(file):
        os.mkdir(file)
    with open(filename, 'wb') as f:
        f.write(html)

def imgdownload(allvideo,count):
    for i in range (0,count):
        download(i,allvideo[i]['pic'])

def getdata(enter):
    params['mid']=enter
    params['pn']=1
    response_1=requests.get(url=link,params=params,headers=headers)
    data=response_1.json()['data']['list']['vlist']
    #pprint.pprint(data)
    video={}
    allvideo=[]
    count=response_1.json()['data']['page']['count']
    count_=count
    
    for n in range(1,1000):
        if count<30:
            for i in range(0,count):
                video['num']=30*(n-1)+i+1
                video['bvid']=data[i]['bvid']
                video['play']=data[i]['play']
                video['length']=data[i]['length']
                video['comment']=data[i]['comment']
                video['pic']=data[i]['pic']
                video['title']=data[i]['title']
                allvideo.append(video)
                allvideo=copy.deepcopy(allvideo)
                video.clear()
            break
        else:
            for i in range(0,30):
                video['num']=30*(n-1)+i+1
                video['bvid']=data[i]['bvid']
                video['play']=data[i]['play']
                video['length']=data[i]['length']
                video['comment']=data[i]['comment']
                video['pic']=data[i]['pic']
                video['title']=data[i]['title']
                allvideo.append(video)
                allvideo=copy.deepcopy(allvideo)
                video.clear()
            count=count-30
            #print(count)
            params['pn']=params['pn']+1
            response_1=requests.get(url=link,params=params,headers=headers)
            data=response_1.json()['data']['list']['vlist']
    
    return [allvideo,count_]

class Media:
    def __init__ (self,comment,pic,title):
        self.title=title
        self.pic=pic
        self.comment=comment
    pass
class Video(Media):
    def __init__ (self,bvid,play,length,comment,pic,title):
        super().__init__(comment,pic,title)
        self.bvid=bvid
        self.paly=play
        self.length=length
    pass
