# -*- coding: utf-8 -*- 
for waiting_no in range(4):
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(2,6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0} , 커피나왔습니다".format(customer))

customer = "토르"
index = 5
while index > 0 :
    print("{0} , 커피가 준비되었습니다, {1}번 남았어요.".format(customer,index))
    if(index == 1):
        print("마지막입니다")
    index-=1

absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book :
        print("수업끝 {0} 따라와".format(student))
        break
    print("{0},출석".format(student))

student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

def hello() :
    print("hello22")

hello()

def hello2(num) :
    print("hello" * num)

hello2(3) 

def profile(name,age,*language) :
    print("이름 : {0}, 나이 : {1} \t".format(name,age))
    for lang in language:
        print(lang,end="")
    

profile("유재석",20,"python","java","c","c++","swift","javascript","react")