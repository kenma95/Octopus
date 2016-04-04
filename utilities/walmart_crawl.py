import urllib
import urllib2
import random
import re
import uuid
import os

localPath = 'c:\\users\\ruiqi\\dropbox\\octopus\\\static\\img\\item' 
def getAndSaveImg(imgUrl): 
  if( len(imgUrl)!= 0 ): 
    img_filename=generateFileName()+'.jpg' 
    urllib.urlretrieve(imgUrl,createFileWithFileName(localPath,img_filename))
    return img_filename
 
def generateFileName(): 
  return str(uuid.uuid1()) 

def createFileWithFileName(localPathParam,fileName): 
  totalPath=localPathParam+'\\'+fileName 
  if not os.path.exists(totalPath): 
    file=open(totalPath,'a+') 
    file.close() 
    return totalPath 





start_with = 1
now_with =start_with

istr = open('walmart.txt','r')
url_addr = istr.readline()
ostr = open('dump2.sql', 'w')

for url in istr:
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	#print response.reassd()

	content = response.read().decode('utf-8')

	pattern = re.compile('<title>(.*?)</title>',re.S)
	items = re.findall(pattern,content)
	title = items[0]

	p = re.compile(' Price--large hide-content display-inline-m price-display"> <span class=Price-sup>\$</span>(.*?)<span class=Price-mark>(.*?)</span><span class=Price-sup>(.*?)</span>')
	items = re.findall(p,content)
	print items
	if items:
		price = items[0][0] + items[0][1] + items[0][2] 
	else:
		continue
	#skip if no price
	p = re.compile('about-item-preview-text js-about-item-preview-text">(.*?)</div> </div> <div class="arrange-fit hide-content-m"> <i class="paginator-hairline-btn paginator-hairline-btn-next trigger-arrow"></i> </div>')
	items = re.findall(p,content)
	des = items[0]
	des.replace("'","\'")
	des.replace("&#39","\'")

	#image
	p = re.compile('<img itemprop=image src="(.*?)" class="product-image js-product-image js-product-primary-image" data')
	items = re.findall(p,content)
	img_url = items[0]
	img_filename = getAndSaveImg(img_url)
	print title

	randd = str(random.randint(0,50) )

	sql_code = "INSERT INTO item(item_id,store_id,item_name,price,description,photo,remain) VALUES ("
	sql_code += "'i"+str(now_with) +"','s1','" + title.encode('utf-8') + "'," + price.encode('utf-8')\
	 + ",'" + des.encode('utf-8') +"','"+img_filename.encode('utf-8')+"',"+randd+");\n"
	#print sql_code


	now_with +=1
	ostr.write(sql_code)
istr.close()
ostr.close()