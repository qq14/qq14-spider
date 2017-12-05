#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
def request():
    url = "http://i.jandan.net/ooxx/page-{}"
    for page in range(1,999):
        yield requests.get(url.format(page))

def parser():
    partten = '<div class="commenttext">.*?[查看原图].*?<br />.*?<img src="(.*?)".*?/>.*?</div>' 
    partten_ = '<div class="commenttext">.*?[查看原图].*?<br />.*?<img src="(.*?)".*?/>.*?</div>' 


    for result in request():
        imageUrls = re.findall (partten,result.text,re.S)
        imageNames = re.findall (partten_,result.text,re.S)
        for imageUrl,imageName in zip (imageUrls,imageNames):
            a = imageName
            imageSource=requests.get("http:"+imageUrl)  
            
            with open('/storage/emulated/0/3/'+"%s"%a[46:55]+'.jpg', 'wb')as f:
                
                
                f.write (imageSource.content)
                
                print("正在下载%s"% imageName)           
    f.close()
if __name__ == '__main__':
    parser()

