import qrcode
import random 
import os
import datetime
from PIL import Image,ImageDraw,ImageFont

image=Image.new('RGB',(1000,900),(255,255,255))
draw=ImageDraw.Draw(image)

font=ImageFont.truetype('arial.ttf',size=45)
os.system("ID CARD GENERATOR")

date=datetime.datetime.now()
reg_format_date=date.strftime("%d-%m-%y\tID CARD GENERATOR \t %I:%M:%S:%p")
print(reg_format_date)

print("\n\nAll Fields are Mandatory")
print("Avoid any kind of Spelling Mistakes")
print("Write Everything in Upper case letters")
(x,y)=(50,50)
message=input("Enter Your Company Name :")
company=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=50)
draw.text((x,y),message,fill=color,font=font)

(x,y)=(600,75)
idno=random.randint(1000000,9000000)
message=str('ID'+str(idno))
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)

(x,y)=(50,250)
message=input("Enter Full Name :")
name=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=45)
draw.text((x,y),message,fill=color,font=font)

(x,y)=(50,350)
message=input("Enter Your Gender")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y)=(250,350)
message=input("Enter Your Age :")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y)=(50,450)
message=input("Enter Your Date of Birth :")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y)=(50,550)
message=input("Enter Blood Group ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y)=(50,650)
message=input("Enter Mobile Number ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y)=(50,750)
message=input("Enter Your Address ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

image.save(str(name)+'.png')
img=qrcode.make(str(company)+str(idno))
img.save(str(idno)+'.bmp')

print(("\n\nYour ID Card Succesfully Created in PNG File"+name+".png"))
eval(input("\n\nPress any key to close program..."))  