import imaplib
import email
import base64
import urllib2
from lxml import etree
from io import StringIO, BytesIO

try: 
	from BeautifulSoup import BeautifulSoup
except ImportError:
	from bs4 import BeautifulSoup

login="USERNAME@gmail.com"
pwd="PASSWORD"


def finddriver(htmlload):

	parsed_html = BeautifulSoup(htmlload, "lxml")
	#print(parsed_html.prettify())

	try:
		if(parsed_html.body.find('table', attrs={'class':'driverPicture'})):
			return parsed_html.body.find('table', attrs={'class':'driverPicture'}).img['src']
		if (parsed_html.body.find('td', attrs={'class':'driver-photo'})):
			return parsed_html.body.find('td', attrs={'class':'driver-photo'}).img['src']
		else:
			# print(parsed_html.prettify())
			# print "------------------------------------------------------------------------------\n\n\n\n\n"
			# input("Press Enter to continue..."
			return
	except:
		return
		#print "no hits"



mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(login, pwd)
mail.list()
mail.select("[Gmail]/All Mail") # connect to all messages inbox

result, data = mail.search(None, '(SUBJECT "trip with Uber")') #search query to surface emails
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string

for messageid in id_list:
	#print messageid
	result, data = mail.fetch(messageid, "(RFC822)") # fetch the email body (RFC822) for the given ID
	 
	raw_email = data[0][1] # here's the body, which is raw text of the whole email

	print raw_email

	# including headers and alternate payloads

	b = email.message_from_string(raw_email)
	if b.is_multipart():
	    for payload in b.get_payload():
	        # if payload.is_multipart(): ...
	        #print payload.get_payload()
			#print "is multipart"
			htmlpayload64 = payload.get_payload()
			htmlpayload = base64.b64decode(str(htmlpayload64))
			imgurl = finddriver(htmlpayload)
			if (imgurl):
				print imgurl
	else:
		htmlpayload64 = b.get_payload()
		htmlpayload = base64.b64decode(str(htmlpayload64))
		imgurl = finddriver(htmlpayload)
		if (imgurl):
			print imgurl
		#print "not multipart"




	# htmlpayload64 = email.message_from_string(raw_email).get_payload()[1]


	# print email_message['To']
	# print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>
	#print email_message.items() # print all headers
