#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,json,datetime,os; os.system("clear")
"""
Build Date: Sun Dec 12 16:31:22 WIB 2021

Author: xolvadev

Join us!

t.me/paddirdp - t.me/channel_justinfo
"""

BOLD = "\033[1m"
print(BOLD)

def mail(line):
	r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
	x = r.text.strip("[").strip("]").strip('"'
	).strip("'")
	now = datetime.datetime.now()
	print(f"""
[Email] >>> {x}

[Date] >>> {now}

[Waiting For Messages..]

Use CTRL+Z To Cancel!\n""")
	print(line)
	user = x.split("@")[0]
	dom = x.split("@")[1]
	z = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={dom}").text
	c = 0
	while True:
		z = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={dom}").json()
		if z != "[]":
			try:
				z = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={dom}&id={z[c]['id']}").json()
				print(f"""New Message!

From: {z['from']}

Subject: {z['subject']}
Date: {z['date']}
ID: {z['id']}

Body: {z['body']}

{line}""")
				c += 1
			except KeyboardInterrupt:
				break
				print("[+] Cancelled.")
			except IndexError:
				pass
		else:
			pass
banner = """
           _
Just type 0 and press enter.
Just type 0 and press enter.
Just type 0 and press enter.
Just type 0 and press enter.
Just type 0 and press enter.
Just type 0 and press enter.
       By xolvadev
   Just type 0 and press enter.
   Just type 0 and press enter.
   Just type 0 and press enter.
   Just type 0 and press enter.
   Just type 0 and press enter.
"""

def main():
	line = "="*35
	print(banner)
	print(line)
	print("[00] Just type 0 and press enter.")
	print("[01] Just type 0 and press enter.")
	print("[02] Just type 0 and press enter.")
	print("[03] Just type 0 and press enter.")
	print("[04] Just type 0 and press enter.")
	print(line)
	inp = input("xv@tempmail >>> ")
	while inp == "":
		mail(line)
	if inp in ("00","0"):
		mail(line)
	else:
		print(line)
		print("Invalid Options : "+inp)

if __name__=="__main__":
	main()
