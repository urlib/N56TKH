#coding=utf-8
import json
import requests
from lxml import etree

bing_url = "https://bing.ioliu.cn/ranking"
ourl = "https://bing.ioliu.cn"
def fir(bing_url):
	r = requests.get(bing_url)
	r.encoding = "UTF-8"
	soup = etree.HTML(r.text)
	a_soup = soup.xpath("/html/body/div[3]/div/div/a")
	for b_soup in a_soup:
		c_soup = ourl + b_soup.get('href')
		fx(c_soup)
def fx(url):
	dic = {
	'id':'',
	'title':'',
	'sub':'',
	'time':'',
	'place':''
	}
	r = requests.get(url)
	soup = etree.HTML(r.text)
	id = soup.xpath("/html/body/div[1]/div[3]/a[3]")[0].get('href')[-31:-15].lstrip("_")
	dic['id'] = id
	durl = ourl+soup.xpath("/html/body/div[1]/div[3]/a[3]")[0].get('href')
	title = soup.xpath("/html/body/div[1]/div[4]/p[1]")[0].text
	dic['title'] = title
	sub = soup.xpath("/html/body/div[1]/div[4]/p[2]")[0].text
	dic['sub'] = sub
	time = soup.xpath("/html/body/div[1]/div[4]/p[3]/em")[0].text
	dic['time'] = time
	place = soup.xpath("/html/body/div[1]/div[4]/p[4]/em")[0].text
	dic['place'] = place
	json_data = json.dumps(dic,ensure_ascii=False)
	fname = "bing_data.json"
	with open(fname,"a+",encoding="utf-8") as f:
		f.write(json_data+"\n")
	res = requests.get(durl)
	f2name= id+'.jpg'
	with open(f2name,"wb") as f:
		f.write(res.content)	

url = "https://bing.ioliu.cn/ranking?p={}"
for i in range(0,100):
	fir(url.format(i))















