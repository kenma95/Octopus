import requests
import csv
import getpass


username = raw_input("Login: Your email address:")
password = getpass.getpass('Login: Your password:')
file_name = raw_input("Your spreadsheet to upload:")


with open(file_name, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',',doublequote=True)
	for row  in reader:
		item_name = row[0]
		item_price = row[1]
		item_desc = row[2]
		img_src = row[3]
		locx = row[4]
		locy = row[5]
		payload = {'username': username, 
			'password':password,
			'item_name':item_name, 
			'item_desc':item_desc, 
			'item_price': item_price,}
		files = {'item_img': open(img_src, 'rb')}  
		r = requests.post("http://162.243.203.93:5000/add_item",
			 data=payload,files =files)

		print item_name +"\t" + r.text





