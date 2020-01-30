#import를 통해 함수 가져옴
from filetostr import filetostr
from datetime import datetime

data = filetostr("01_html.html")
print(data)

print(datetime.now())
