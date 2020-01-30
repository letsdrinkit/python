f = open("01_html.html", "r", encoding="utf-8")
data = f.readline()
f.close()

#첫줄
print(data)
print("-"*30)

#불필요한 요소 제거
data = data.replace("\n", "").replace("<", "").replace(">", "").replace("!", "")
print(data)
print("-"*30)

#반복문을 이용한 문자열 분리
words = data.split(" ")
for word in words :
    print(word)
print("-"*30)

#문자열 분리 중 공백 변경(제거)
data = data.replace("\n", "").replace("<", "").replace(">", "").replace("!", "")
for c in data :
    if c != " " :
        print(c)
    else : print("*"*20)
print("-"*30)

#
print("문자열길이 :", str(len(data)))

#
idx = data.find("xml")
if idx != -1 :
    print("html찾기 :", idx)
else : print("xml단어가 없습니다.")
print("-"*30)





