from PIL import Image, ImageDraw,ImageFont
from screeninfo import get_monitors
from datetime import date
import time
today = date.today()
timeData = time.localtime()
minutes = timeData.tm_min
hour = timeData.tm_hour%12
# print(hour,minutes)

#------------------------
minutes  = minutes if minutes>9 else str(0)+str(minutes)
hour  = hour if hour>9 else str(0)+str(hour)
#------------------------------
s = f"{hour}:{minutes}"
# today.

v = get_monitors()
a = v[1]
# print(a.height,a.width)
img = Image.new('RGB', (a.height, a.width), color = 'black')
font = ImageFont.truetype('Cascadia.ttf', 300) 
d = ImageDraw.Draw(img)

d.text((800,200), s, font=font,fill=(58,58,58))
img.show()
