# mod1.py
def add(a, b):
   # print(a+b)
    return a + b
    
def sub(a, b): 
    return a-b

if __name__=="__main__": #참인경우: 파이선의 mod1수행시 프린트 수행 #거짓인 경우: 함수만 호출 
    print(add(1, 4))
    print(sub(4, 2))