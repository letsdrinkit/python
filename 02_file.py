f = open("01_html.html", "r", encoding="utf-8")
data = f.readline()
f.close()
print(data)
print("-"*30)


f = open("01_html.html", "r", encoding="utf-8")
datalines = f.readlines()
f.close()
print(datalines[30])
print("-"*30)


f = open("01_html.html", "r", encoding="utf-8")
dataread = f.read()
f.close()
print(dataread)
print("-"*30)