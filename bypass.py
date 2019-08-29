from bs4 import BeautifulSoup as bs
import requests as req
from os import system as os

ses = req.Session()
def banner():
	os('clear')
	print ("""[ Bypass Shortlink & Check Shortlink ]""")

def shtme():
	try:
		erl = input('\n{*} Bypass > ')
	except:
		exit()
	if 'https://shtme.co' in erl:
		try:
			p = ses.get(erl)
			u = bs(p.content, "html.parser")
			for q in u.find_all("div", style="margin-top:5px;text-align:center;"):
				for d in q.findChildren('a', rel='nofollow'):
					we = d.get('href')
					ew = ses.get('https://shtme.co'+we)
					ui = bs(ew.content, "html.parser")
					for re in ui.find_all("meta"):
						er = re.get('content')
						open('t.txt','a').write(er)
						ze = open('t.txt').read().splitlines()
						for ez in ze:
							pe=ez.split('=')
							print ('{*} Result > '+pe[1])
		except:
			exit()
	else:
		exit('{*} Error | Check your link!')

def linkduit():
	try:
		url = input('\n{*} Bypass > ')
	except:
		exit()
	if 'https://linkduit.net' in url:
		try:
			cr = ses.get(url)
			pr = bs(cr.content, "html.parser")
			for sr in pr.find_all('div', id='download'):
				for ir in sr.findChildren('a', rel='nofollow'):
					wr = ir.get('href')
					lr = ses.get('https://linkduit.net'+wr)
					hr = bs(lr.content, "html.parser")
					for vr in hr.find_all('meta'):
						ur = vr.get('content')
						open('e.txt','a').write(ur)
						jr = open('e.txt').read().splitlines()
						for kr in jr:
							mr=kr.split('=')
							print ('{*} Result > '+mr[1])
		except:
			exit()
	else:
		exit('{*} Error | Check your link!')

def shortid():
	try:
		entr = input('\n{*} Bypass > ')
		if 'https://mytreep.icu' in entr:
			url = ses.get(entr)
			sop = bs(url.content, "html.parser")
			for i in sop.find_all("div", id="download"):
				for x in i.findChildren('a', rel="nofollow"):
					link = x.get('href')
					yrl = ses.get('https://mytreep.icu'+link)
					yop = bs(yrl.content, "html.parser")
					for y in yop.find_all("meta"):
						ras = y.get('content')
						open('i.txt', 'a').write(ras)
						zr = open('i.txt').read().splitlines()
						for p in zr:
							x=p.split("=")
							print ('{*} Result > '+x[1])
		else:
			exit()
	except:
		exit('{!} Error | Check your link!')

banner()
print ('\n{1} Shtme.co')
print ('{2} Shortid.co')
print ('{3} Linkduit.net')
print ('{4} Bit.ly')
print ('{5} Git.io + Check Url')
print ('{5} Exit')
try:
	men = input('\n{*} Select number > ')
except:
	exit()
if '1' in men:
	shtme()
	os('rm t.txt')
elif '2' in men:
	shortid()
	os('rm i.txt')
elif '3' in men:
	linkduit()
	os('rm e.txt')
elif '4' in men:
        os('bash t')
elif '5' in men:
        os('bash short')
elif '6' in men:
        exit()

else:
	exit('{!} Error | Wrong number!')
