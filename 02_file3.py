#함수 만들기
def filetostr(filename) :
    #파일 열기
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    #파일 종료
    f.close()
    
    #return으로 함수를 끝내며 뒤의 정보를 갖고 옴.
    return data

fname = input("파일명을 입력하세요 : ")
data = filetostr(fname)
print(data)







