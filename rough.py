from PIL import Image, ImageDraw,ImageFont
from screeninfo import get_monitors
from datetime import date

today = date.today()
# print(today)
year = today.year%100
day = today.day
month = today.month;
#------------------------
day  = day if day>9 else str(0)+str(day)
month  = month if month>9 else str(0)+str(month)
#------------------------------
s = f"{day}:{month}:{year}"
# today.

v = get_monitors()
a = v[1]
# print(a.height,a.width)
img = Image.new('RGB', (a.height, a.width), color = 'black')
font = ImageFont.truetype('Cascadia.ttf', 200) 
d = ImageDraw.Draw(img)

d.text((800,200), s, font=font,fill=(58,58,58))
img.show()