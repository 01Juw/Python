import csv  
import requests  
import re
from lxml import etree
from time import sleep
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}  
def GetPhone(url):
	with open('E:/infomation.csv', 'wt', encoding='utf8',newline='') as f: 
		new_url ='http://bj.ganji.com'+url
		#print(new_url)
		content = requests.get(new_url,headers=headers).text
		#print(content)
		html = etree.HTML(content)
		result = html.xpath("//div[@class='c_phone f-clear']/@data-phone")
		resultn = html.xpath("//p[@class='name']")
		resultd = html.xpath("//span[@clas='company']")
		try:
			print(result[0])
			print(resultn[0].text.replace(' ', ''))
			print(resultd[0].text.replace(' ', ''))
			requests.get("http://localhost:57845/main.aspx?a="+resultn[0].text.replace(' ', '')+"&b="+resultd[0].text.replace(' ', '')+"&c="+result[0],headers=headers)
		except:
			print('-----TT')
url = 'http://bj.ganji.com/fang5/fengtai/o1/'  
with open('E:/infomation.csv', 'wt', encoding='utf8',newline='') as f:  
    csv_writer = csv.writer(f, dialect='excel')#这里打开csv文件开始写入    
    for i in range(1,40):  
        new_url = 'http://bj.ganji.com/fang5/fengtai/o' + str(i) +'/'  
        content = requests.get(new_url,headers=headers).text
        #print(content)
        html = etree.HTML(content)
        result = html.xpath("//a[@class='js-title value title-font']/@href")
        print(len(result))
        for ai in range(1,len(result)):
            GetPhone(result[ai])
        sleep(5)
