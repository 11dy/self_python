# # # animal ="강아지"
# # # name = "연탄이"
# # # age =4 
# # # hobby = "산책"
# # # is_adult = age >=3 

# # # print("우리집 "+ animal +"의 이름은"+ name)  # + 말고도 , 컴마로도 문장을 합칠 수 있다. 컴마를 사용한 경우는 str 없이도 출력이 가능하다 
# # # print(name,"는",age,"살이며,",hobby, "을 아주 좋아해요")  # 정수, boolean 형태는 str() 추가 
# # # print("연탄이는 어른인가?" + str(is_adult))

# # # # 컴마가 들어가면 띄어쓰기가 하나 포함된 것 
# # # # 주석처리 #은 한 줄 또 
# # # ''' 이건 여러 문장 처리 할 때 
# # # 알겠니 기억해 ''' 
# # # #여러 문장을 일괄적으로 주석처리 하고 싶을 땐 드래그 후 ctrl+/ , 해제는 이 역순으로 하면된다. 

# # # station1 = "사당"
# # # station2 = "신도림"
# # # station3 = "인천공항"

# # # print(station1,"행 열차가 들어오고 있습니다.")
# # # print(station2,"행 열차가 들어오고 있습니다.")
# # # print(station3,"행 열차가 들어오고 있습니다.")

# # print(2**3)  # 2의 3승이 된다. 
# # print(5%3) # 나머지 구하기 
# # print(10//4) # 몫 구하기 
# # print(4 >=7) # 아니니까 False가 나온다. 

# # print(5 >3>2) # 연속되는 값은 True False로 나온다. 
# # print(4 >2 > 9) # False 

# # ============= 수식===================

# print(2+ 3*4) #14 
# print((2*4)-6) #2

num = 2*5-6 
print(num)  # 변수 삽입 연산 

num = num +2 # 4+ 2 = 6
print(num)

num+=2  # 6 + 2 = 8
print(num)

num*=5 # 8*5=40 
print(num)


# ==========숫자 처리 함수==================== 

print(abs(-5))
print(pow(4,6))  # 제곱값 
print(round(2423.3920))  # 반올림 
print(round(4.9283)) #5 

from math import * # math 라이브러리 안에 있는 모든걸 사용하겠다 
print(floor(4.99)) # 내림 

print(ceil(4.99)) # 올림 
print(sqrt(16)) # 제곱근 

print('-random library-')
from random import * 
print(random())  # 0.0 ~1.0 미만의 임의의 값 생성 
print(random()*10)
print(int(random()*10)) # 랜덤함수 사용하되, 소수점을 보기 싫을 때 0~10 미만의 임의의 값 생성 
print(int(random()*10)+1) #1~10 이하의 임의의 값 생성 


print(int(random()*45)+1)  # 로또 값 출력 1~45 의 랜덤 숫자 출력 
print(randrange(1,46)) # 1부터 46 미만의 임의의 값 출력 
print(randint(1,45)) # 1 부터 45 사이의 수 출력, 양 끝을 포함하는 함수다. 


print('========quiz========')
'''당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
아래 조건에 맞는 오프라인 모임 날짜를 정해 주는 프로그램을 작성하시오. 

조건1: 랜덤으로 날짜를 뽑아야 함 
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함 
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외 
(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. '''

# from random import * > 앞에 선언해서 안써도 작동 됨. 
x = randint(4,28) 
print("오프라인 스터디 모임 날짜는 매월", x,"일로 선정되었습니다.")

print("================문자열==================")
sentence = '나는 소년입니다.' # ""가 와도 똑같이 출력된다. 
print(sentence)  
sentence3 = '''나는 소년이고, 파이썬은 
쉬워요'''
print(sentence3)

print('============슬라이싱=============')
jumin = '981010-1234567'
print('성별:' + jumin[7]) # 1 
print('연:' + jumin[0:2]) # 1 0부터 2번째 직전 값 까지 출력 또는 [:2]로 적어줘도 된다. 
print('월:' + jumin[2:4]) # 10
print('뒤7자리:' + jumin[7:14]) # [7:] 7부터 끝까지 
print('뒤7자리:' + jumin[7:14]) # [-7:] 맨 뒤에서 7번째부터 끝까지 

print('==========문자열 처리 함수==========')
# 소문자, 대문자 변환 함수 
python = "Python is AMazing"
print(python.lower()) # 소문자 변환 함수 
print(python.upper()) # 대문자 '' 
print(python[0].islower())  # 변수의 0번째 값이 소문자인지 대문자인지도 적용이 됨. False, True로 표시됨 

print(len(python)) # 변수 문자열 전체 길이 반환 

print(python.replace("Python", "Java"))#문자열에서 Python 찾아서 Java로 변경 

index = python.index("n") # 문자열 내 n의 위치 반환 
print(index) # 5 > 115라인으로 변경해도 변수에 담긴 값이 바뀌지 않음. 

index = python.index("n", index+1) # 앞에서 찾은 위치 다음 부터 찾기 = 위치 5 다음은 6번째 위치 부터 n 찾기 (두 번째 n 찾기)
print(index)

print(python.find("Java")) # 원하는 문자가 포함된 위치 반환 > Java가 없다. 이때는 -1 출력 

# print(python.index("Java")) # 오류 발생. python변수에 Java가 없기 때문에 에러를 발생.> 프로그램 종료> 뒤에 어떤 명령을 입력해도 출력이 안됨. 

print(python.count("n")) # 변수에서 n이 총 몇번 등장하는지 출력 

print("=============문자열 포맷=============")
# 일반적으로는 print("a"+"b") 처럼 +와' ,'를 사용해서 문자열을 합쳤음. 

# 방법1 % 이용 
print("나는 %d살입니다." % 25) # % 뒤에 있는 값을 d 위치에 넣겠다. d는 항상 정수 

print("나는 %s을 좋아해요." %"파이썬") #문자열도 넣을 수 있다. 문자는 %c , s자리에 정수를 써도 출력 된다. 
print("나는 %s색과 %s색을 좋아해요." % ("검은색", "그래파이트")) # 여러 문장 입력시 

#방법2 > 중괄호 이용방법 
print("나는 {}살입니다.".format(25)) # .format() > 괄호 안에 있는 값을 중괄호에 넣는다. 

print("나는 {}색과 {}색을 좋아해요." .format("검은색", "그래파이트")) # 여러 문자열 입력 
print("나는 {1}색과 {0}색을 좋아해요." .format("검은색", "그래파이트")) # 순서 지정해서 입력 

#방법3 
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color='빨간'))  # 위에 거랑 똑같이 순서 변경 가능. 

#방법4 3.6이상 

age = 20 
color = '그래파이트'
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 앞에 f로 시작 실제 저장된 변수의 값을 가져다 사용함.

print("==========탈출문자=========")

print("백문이 불여일견\n백견이 불여일타")  # \n: 문장 내에서 줄바꿈 문자 

print("저는 '이동열'입니다.")  
print('저는 "이동열"입니다.')  # 이것도 큰따옴표로 출력되긴 함 
print("저는 \"이동열\"입니다.")  # \"는 문장 내에서 큰따옴표 출력 작은따옴표도 마찬가지임. 

#\\ < 역슬래시 두 번 > 문장 내에서 하나의 역슬래쉬로 변경됨. 
# \r: 커서를 맨 앞으로 이동 
print("Red Apple\rPine") # 커서를 맨 앞으로 이동해서 Pine문자 작성 > PineApple 출력 
# \b: 백스페이스 > 한 글자 지움. 
print("Redd\bApple")
 
# \t: 탭 
print("Red\tApple")  # 4칸 띄움 

print("quiz===========사이트별 비밀번호 생성=========")

#URL = "http://naver.com" 
URL = "http://google.com" 
pw = URL.replace("http://", "") # replace를 공백으로 하면 삭제의 역할을 할 수 있다. 
pw = pw[:pw.index(".")] # pw문자열 중에서 처음 나오는 "." 위치 직전까지 저장 naver 저장됨. 
pw = pw[:3]+ str(len(pw)) + str(pw.count("e"))+"!" # 정수, 불리언은 모두 str()로 감싸줘야한다. ,인 경우는 제외 
print("{0}의 비밀번호는 {1}입니다.".format(URL, pw))


# URL2 = URL[index: ]  # 두번째'/'까지 제외한 나머지 주소 저장 
# index = URL2.index(".")  # . 위치 반환 /안되면 find 사용하기 
# URL3 = URL2[ :index]# . 위치 이후 문장 삭제 , index2 직전까지 출력 
# lenth = len(URL3)
# print(URL3[ :3],len(URL3),URL3.count("e"),"!")  # 띄어쓰기 안되면 \b사용하기 

print("============리스트============")
# 여러 공간에 저장된 변수를 하나로 묶어 주는 것 
subway = [10, 20, 30]
print(subway)

subway = ["이동열", "조세호", "유재석"]
print(subway)
print("조세호 위치:" + str(subway.index("조세호")))

#리스트 추가 
subway.append("하하") # 항상 맨 뒤에 붙는다. 
print(subway)

#리스트 중간에 추가 
subway.insert(1, "정형돈") # subway.insert(넣을 위치, 0과1 사이라면 1을 써주면 된다., 객체 값 )
print(subway)

#리스트 뒤에서 추출 
print(subway.pop()) #subway.pop() 
print(subway.pop())
print(subway.pop())
print(subway.pop())
print(subway)

# 리스트의 같은 객체 출력 
subway.append("유나")
subway.append("아이사")
subway.append("유나")
subway.append("이새롬")

print(subway.count("유나")) # 2번 들어있음 

#정렬도 가능함 
lis = [10,34,63,23,11,4,6,23,7]
lis.sort()
print(lis)

#리스트 뒤집기 
lis.reverse()
print(lis)

#모두 지우기 
lis.clear()
print(lis)

#리스트는 자료형에 구애받지 않고 섞어서 사용 가능하다 
mixlis= ["조세호", 10, True]
lis = [10,34,63,23,11,4,6,23,7]
print(mixlis)

#리스트 확장(합치기)
lis.extend(mixlis)
print(lis)

print("=============사전=============")
# {key : value} 형태로 구성 
cabinet = {3:"유재석", 100:"유나"} # key를 호출하면 value가 출력된다. 
print(cabinet[3]) #유재석
print(cabinet.get(3)) #유재석 get을 쓸 때는 소괄호를 사용한다. 

#print(cabinet[5]) # cabinet에 5라는 key가 없어서 프로그램을 바로 종료시킴 

print(cabinet.get(5)) # none 출력 후 프로그램 계속 진행 
print("keepgoing")

print(cabinet.get(5, "사용 가능")) # none 대신 메시지를 출력하거나 다른 값을 출력하고 싶으면 옆에 적어주면 된다.

# 어떤 값이 사전에 존재하는 지 출력 > true or false 
print(3 in cabinet) 
print(5 in cabinet)

# 문자열 형태의 key도 선언 가능하다. 
cabinet = {"A-3":"유재석", "B-100":"유나"}
print(cabinet["A-3"])

# 사전에 새로운 항목 추가 
cabinet["C-20"] = "아이사" # [key] = value 
print(cabinet)

cabinet["A-3"] = "하원" # 원래있던 유재석 삭제 후 하원 입력 

# 값을 그냥 지우기 
del cabinet["A-3"]
print(cabinet)

#key들만 출력 
print(cabinet.keys())
#value들만 출력 
print(cabinet.values())

#key, value 쌍으로 출력 
print(cabinet.items())

#사전 종료 
cabinet.clear() 
print(cabinet) # 빈 값 출력 

print("=========튜플=========")
# 튜플은 리스트와 달리 내용 변경, 추가를 못한다. 다만 리스트 보다 속도가 빠른게 장점이다. 그래서 내용 변경이 없는 목록 작성 시 유리하다 
# 튜플은 (), 리스트는 [], 사전은 {}

menu = ("돈까스", "치즈까스")
#사전의 출력과 동일 
print(menu[0]) 
print(menu[1])

# 튜플 추가, 변경 불가 
name = "김종국"
hobby = "운동"
age = 40 
print(name, age, hobby)

#바로 값을 넣을 수 있음  
(name, age, hobby) = ("아이사", 21, "dance")
print(name, age, hobby)

print("=======세트(집합)========")
# 중복이 안되고 순서가 없음. 

myset = {1,2,4,5,2,4} # 값만 쭉 나열하면 된다. 
print(myset) # 중복 무시 후 출력 

java = {"이동열", "아이사", "권은비"}
# set([]) 형태도 세트가 될 수 있다. 
python = set(["이동열","박명수"])  

#자바와 파이썬을 모두 할 수 있는 사람 출력 > 교집합 
print(java & python)
print(java.intersection(python))

#합집합 
print(java | python) 
print(java.union(python))

#차집합 
print(java-python)
print(java.difference(python))

# 특정 집합의 원소 추가 
python.add("한소희")
print(python)

# 특정 원소 삭제 
python.remove("박명수")
print(python)

print("============자료구조의 변경=============")

menu= {"아아","라떼", "녹차"}
print(menu, type(menu)) # <class, 'set'> 클래스 타입이 set 

menu = list(menu)  # <class, 'list'> 클래스 타입이 list
print(menu, type(menu)) 

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

print("==========퀴즈==========")

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)  # 리스트 내부의 순서가 섞임 
# print(lst)
# print(sample(lst, 1) )  # lst에서 몇 개 뽑겠다.  
#==========================================================
from random import * 
users = range(1, 21) # 1부터 20까지 숫자를 생성 
users = list(users)

shuffle(users) # 섞은 이유> 순위 정해버림 

winners = sample(users, 4) # 4명 선택 후 치킨, 커피 당첨자 구분한다. 

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))  #0번째 1등
print("커피 당첨자 : {0}".format(winners[1:]))  # 1등 선택 후 순서대로 출력 
print(" -- 축하합니다 -- ") 

#=============================================================

from random import * 
lst = range(1, 21) # 1부터 20까지 리스트 생성 range() 단, 이렇게 생성하면 list 타입이 아니라 range 타입이 된다. 자료구조 변환이 필요함. 
# 자료구조 변환 
lst = list(lst)
shuffle(lst) # 리스트 내부 값 섞음 
# 치킨 당첨자 
first = sample(lst, 1)
#집합으로 변경 
lst = set(lst)
first = set(first)
# 치킨 당첨자 제외
secound = lst - first 
# 집합상태 풀기 
first = list(first)
# 커피 당첨자 3명 
secound = sample(secound, 3) 

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : " + str(first.pop()))
print("커피 당첨자 : " + str(secound))
print(" -- 축하합니다 -- ") 

# (차이점)난 첫 리스트에서 1등을 선택 한 후 차집합을 통해 나머지 순위를 구함. 나도코딩은 1등부터 꼴등까지 모든 순위를 sample로 추출한 후 format으로 순위 추출.  

#=========================================================

print("=============if문============")

# # if 조건: 
#     #실행 명령문 

# weather = '비'
# if weather =='비' :
#     print("오늘은 비가 내립니다.")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요.")
# else :
#     print("준비물 필요 없어요.")   


# weather = input("오늘 날씨는 어때요? ") 
# '''input()은 사용자 입력 받는 문장, 어때요? 다음에 커서가 위치하고 사용자의 입력을 기다린다. 
# 사용자의 입력을 받으면 weather변수에 저장한다.''' 

# if weather =='비' or weather == '눈' :  # or로 조건을 추가할 수 있다. 
#     print("우산을 챙기세요.")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요.")
# else :
#     print("준비물 필요 없어요.")   


# # 기온 입력 > 숫자, 정수 입력 
# temp = int(input("현재 기온: "))  # 사용자가 입력한 값을 정수 형태로 현환 후 temp 변수에 저장 
# if temp >= 30 : 
#     print("외출 자제")
# elif 10 <= temp and temp >30 :
#     print("날이 좋네요. 밖에서 봐요")
# else:
#     print("적절한 의복을 갖춘 후 외출하세요.")

print("==============for==============")

for waiting_no in [0,1,2,3,4,5]: # 순차적으로 커질 때는 range()를 사용하면 된다./ range(5)> 0부터 5미만 까지 범위가 주어짐. range(~부터, ~전까지)
    print ("대기번호: {0}".format(waiting_no))

for waiting_no in range(1,10): 
    print ("대기번호: {0}".format(waiting_no))

# 리스트에서 원소 추출 후 for문 실행 
starbucks = ['이동열', '하원', '아이사', '사나']
for customer in starbucks: 
    print("\"{0}\"고객님 커피가 준비되었습니다.".format(customer))

print("=============while============")
customer = "아이사"
index =5 
while index >=1:  # while (조건): > 조건 이 만족할 때 까지 반복하라 / 인덱스가 1보다 같거나 클 때 까지 반복하라 
 print("\"{0}\"고객님 커피가 준비되었습니다. {1}번 남았습니다. ".format(customer, index))
 index -= 1 
if index == 0 :
    print("커피 재고가 모두 소진됐습니다.") 

# while 문 무한루프 생성 > while True : 
# 무한루프 탈출 > ctrl + c : 강제종료 

print("==========continue and break===========")
#반복문 내에서 사용가능. 
absent = [2, 5] # 결석 
for student in range(1, 11) :  # 10명의 인원 
    if student==2 or student ==5 :          # if student in absent: > student 중 absent에 있는 결석자가 있다면, continue 
        print("{0}번 결석".format(student))
    else :
        continue 

for student in range(1, 11) :  # 10명의 인원    
    if student in absent: 
        continue
    else :
        print("{0}야 책을 읽어줘".format(student))

# 한줄 for문 
# 출석번호가 1,2,3,4 이고, 아펭 100을 붙이기로 함 -> 101, 102,103,104 
students = [1,2,3,4]
students = [i+100 for i in students]  # student에서 값을 불러와 i에 저장하고 +100한 값을 students리스트에 저장. 
print(students)

#학생 이름을 길이로 변환 , 문자열 정수형태 변환 
student = ["이동열","피크닉애플","아이패드", "경제기사 궁금증"]
student = [len(i) for i in student] # student에 들어있는 i의 값의 길이를 파악한 후 student에 저장 
print(student)

# 학생 이름을 대문자로 변환 
student = ["leedongyeol","picnic_apple","ipad", "the question of economic article"]
student = [i.upper() for i in student]
print(student)

print("============퀴즈=============")
# 총 탑승 승객 수를 구하는 프로그램 
# 조건1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다. 
# 조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다. 

# cnt = 0 # 총 탑승 인원 
# from random import * 

# for customer in range(1, 51): # 50명 탑승 조건 
#     use_time = randint(5, 51) # 조건1
#     if use_time >=5 and use_time <= 15 :  # 5<= time <= 15 로 표현해도 가능
#         print ("[0] {0}번째 손님 (소요시간 : {1})".format(customer, use_time))
#         cnt += 1 
#     else : 
#         print ("[ ] {0}번째 손님 (소요시간 : {1})".format(customer, use_time))

# print("총 탑승 승객 : " + str(cnt) +"분")

print("============함수============")

def open_account(): # def + 함수이름(): 
    print("새로운 계좌가 생성되었습니다.")  # 함수 내용 정의 

open_account()  # 함수 호출은 함수의 이름과 괄호를 적어주면 된다. 

# 입금 함수 
def deposit(balance, money): # 괄호 내부에 매개변수를 넣어준다. 
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money # 반환값 적어줘야됨 

# 출금 함수 
def withdraw(balance, money): 
    if balance < money :    # 잔액보다 많은 양을 출금하려는 경우 
        print("잔액이 부족합니다.")
        return 0
    else :
        print("출금이 완료되었습니다. 출금 금액 : {0} , 잔액 {1}".format(money, balance-money))
        return balance - money 

# 야간 출금 함수 
def withdraw_night(balance, money) : 
    commission = 100 # 수수료 100원 
    return commission, balance - money - commission # 수수료가 얼마이고, 잔액이 얼마가 남았는지 > 튜플 형식으로 반환 (컴마를 이용해서)> 여러개의 값을 반환하는데 도움이 된다. 


balance = 0 # 계속 더해줄 잔액을 변수로 표현 
balance = deposit(balance, 100000)
#balance = withdraw(balance, 20000)
commission, balance = withdraw_night(balance, 200) # commission과 balance를 동시에 받고 현재 금액인 balance와 수수료의 정수값을 받는다. 
print("수수료는 {0}원이고, 잔액은 {1}원 입니다. ".format(commission, balance))# 잔액에서 출금과 수수료를 더한 값이 빠진다. 


print("========함수의 기본값========")

# def profile(name, age, main_lang):
#     print("이름: {0}, 나이: {1}, 주 사용 언어: {2}"\
#         .format(name, age, main_lang))                  # 줄바꿈은 역슬래시 후 엔터 (두 문장은 실제로 한 문장이다.)

#profile 호출 
#profile("이동열", 26, "Python") 

# 만약 괄호 안에 들어가는 값들이 겹치는 부분이 있는 호출들을 나열해야 한다면, 기본값을 사용한다. 

def profile(name, age = 26, main_lang = "Python"): # 해당 항목에 값이 주어지지않는다면 설정된 기본값들을 사용하겠다. 
   print("이름: {0}, 나이: {1}, 주 사용 언어: {2}"\
         .format(name, age, main_lang))
profile("이동열")
profile("아이사", 20) # 항목의 값을 변경할 수 있다. 
profile("카리나")

print("=============키워드 값=============")
# 키워드를 이용해서 함수에서 받는 매개변수를 순서에 상관없이 정상출력할 수 있다. 
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(main_lang = "Python", age = 26, name = "이동열") 

print("========가변인자========")
#end =" " : print문이 끝날 때 줄바꿈을 하지않고 출력을 끝낸다. 

def profile(name, age, lang1, lang2, lang3, lang4): # lang 부분들을 없애고 *lang 형태로 통일하는 것을 가변인자라고 한다. 
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4) # 두 print문이 하나의 줄에 출력된다. 

def profile(name, age,*language): 
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("이동열", 20, "python", "java", "c", "c++")  # 서로 다른 개수의 값을 넣어줄 때는 가변인자를 사용한다. "*매개변수"를 의미. 
profile("아이사", 20, "Kotlin", "Swift")

print("=======지역변수, 전역변수========")

gun =20

def checkpoint(soldiers): 
    global gun 
    gun -= soldiers           # 여기서 gun은 지역변수이기 때문에 새로 선언을 해줘야 한다. 다시 선언하기 싫다면 "global 전역변수" 형태로 사용하면 된다. 
    print("함수 내에 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(5) # 5명이 총들고 나감 
print("남은 총 : {0}".format(gun))

print("==========quiz===========")
# 표준 체중 구하기 프로그램 

def std_weight(height, gender):  # 매개변수로 키와 성별을 받음 
    weight = 0        # 지역변수 선언 
    if gender == "male":                     # male: h*h*22, woman: h*h*21 
        weight=height*height*22 
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height,weight/10000))
    elif gender == "woman":
        weight=height*height*21
        print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height,weight/10000))


std_weight(175,"male") 

#=================================================
def std_weight(height, gender): # 키는 미터 단위(실수), 성별은 문자열 형태로 받는다. 
    if gender == "남자" :
        return height*height*22 
    else :
        return height*height*21 

height = 175 # cm단위 
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 미터변환 , round(~, 2) > 소수점 둘째 자리까지 체크해줘 
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight) ) 

print("========표준입출력=======")  

# sep를 통해 지정 
print("python", "java", sep=" , ")
print("python", "java", "http", sep=" vs ") # 문장 사이사이에 뭐가 들어갈지 정한다. python vs java vs http  /  seperate 

print("python", "java", "http", end="?") # end="?"는 문장의 끝 부분을 물음표로 바꾸라는 의미다. python java http무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

#
import sys 
print("python", "java", file=sys.stdout) # 표준 출력으로 문장이 찍힌다. 
print("python", "java", file =sys.stderr) # 표준 에러로 처리 (로깅을 따로 해서 에러처리 하기 위한 용도) 둘다 출력은 같다. python java 


# 시험 성적 
scores= {"수학": 100, "영어" : 95, "국어": 100}

for subject, score in scores.items(): # .items() > 키, 값이 쌍으로 출력됨 
    print(subject.ljust(3), str(score).rjust(4), sep=":") # 4칸 공간 확보 후 왼쪽 정렬 / .rjust(4) > 오른쪽 정렬 후 4번 정렬 

#은행 대기순번표 
# 001, 002, 003 ,...
for num in range(1, 21):  # 1부터 20까지의 수 출력 
    print("대기번호 :" + str(num).zfill(3)) # .zfill(3) > 3개 만큼의 공간을 확보하고 남는 공간은 0으로 채워주는 함수 


# 표준입력 
# answer = input("값을 입력하세요: ")
# print("입력값은 " + answer + "입니다. ")
# print(type(answer)) # 정수를 입력해도, 문자열을 입력해도 string 타입이 나온다. 

num = 10
print(type(num)) # 이때는 int 타입으로 나온다. 
# 따라서 사용자입력 형태로 값을 받게 되면 항상 문자열 형태로 저장된다. 

print("========다양한 출력 포맷=========")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보 
print("{0: >10}".format(500))

# 양수일 때는 +로 표시, 음수일 땐 -로 표시. 정수 앞에 +를 붙여주면 음수표현도 가능함. 위의 상태에서는 음수를 대입해도 양수가 출력된다. 
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 언더바를 채운다. 
print("{0:/<10}".format(100))  # 100/////// 
print("{0:_<+10}".format(-100)) # +100______ , :과 < 사이에 빈공간이 하나 이상 있으면 안된다. 

# 3자리 마다 콤마를 찍어주기 
print("{0:,}".format(123456789))  # 123,456,789
print("{0:+,}".format(1000000000000))  # -1,000,000,000,000 컴마 앞에 +를 붙이면 음수표현도 가능하다. 
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기, 빈 자리는 ^로 
print("{0:^<+50,}".format(-1000000000000000)) # 1. 빈자리 뭘로 채울지 /  2. 오른쪽 정렬 / 3. +로 부호 붙이기 / 4. 몇 자리 공간을 확보할 것인지(공간이 들어가는 정수 보다 작다면 ^가 출력이 안될 수 있다. )
# -1,000,000,000,000,000^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# 소수점 출력 
print("{0:f}".format(5/3))  # 1.666667 
print("{0:.2f}".format(5/3))  # 1.67 
print("{0:.3f}".format(5/3))  #1.667 

print("=======파일 입출력=======")
# 파일을 열었으면 항상 닫는 것 까지 해야됨 
# score_file = open("score.txt", "w", encoding="utf8")  # open( 파일 이름, 파일을 사용할 형식, 인코딩 방식) encoding = "utf8"은 한글이 원활하게 표현하기 위해 사용한다. 
# print("수학 : 100", file = score_file) # w는 파일 쓰기 형식으로 오픈 / 파일 이름 적을 때 항상 문자열 형식 준수! 
# print("영어 : 100", file = score_file)
# print("국어 : 100", file = score_file)
# score_file.close() # 파일 닫음 
# 좌측 explorer열어 보면, score.txt 파일이 생성된 걸 알 수 있다.  

# 파일 이어쓰기 
# score_file = open("score.txt", "a", encoding="utf8") # a형식으로 파일열기 apend: 기존에 생성된 파일에 계속 쓰고싶을 때 사용한다. 
# score_file.write("과학 : 100")
# score_file.write("\n코딩 : 100") # print를 사용했을 때는 자동을 줄바꿈이 되지만 write를 사용할 때는 자동으로 안된다. \n으로 명시적인 정의가 필요하다. 
# score_file.close() 

# 파일 읽기 
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # 파일의 모든 내용을 읽어와 출력한다. 
# # print(score_file.read() + "\n") > 다 불러오고 한칸 띄고 마무리 
# score_file.close()

# 파일을 한 줄씩 읽어오고 싶을 때 
# score_file = open("score.txt", "r", encoding="utf8") 
# print(score_file.readline()) # 한 줄만 읽어오고 커서를 다음 줄로 이동시킨다. # print에서는 자동으로 줄바꿈을 해줘서 한 줄씩 더 출력된다. 
# print(score_file.readline(), end="")  # 줄바꿈을 하기 싫을 때는 이렇게 표시하면 된다. 
# print(score_file.readline())
# print(score_file.readline())

#몇줄인지 모를 때 줄처리 
# score_file = open("score.txt", "r", encoding="utf8")  
# while True: # 무한루프인 경우 
#     line = score_file.readline() #score_file을 한 줄씩 읽어오고 
#     if not line :  # line이 없다면 
#         break  # 반복문 탈출 
#     print(line, end="") # 한칸 띄우기 안하려면 end="" 입력
# score_file.close()

# print("\n") # 줄 띄우기 

# #리스트에 값을 넣어서 처리 
# score_file = open("score.txt", "r", encoding="utf8")  
# lines = score_file.readlines() # 모든 라인을 가지고 와서 list 형태로 저장한다. 
# for line in lines:  # 리스트에서 한 줄 씩 읽어와 line변수에 넣어주고 출력 (줄 추가 없이)
#     print(line, end="")
# score_file.close()
# print("\n")


print("=========pickle========")
# 프로그램상에서 사용하는 데이터를 파일 형태로 저장하는 것 
import pickle  # pickle 모듈 import 
profile_file = open("profile.pickle", "wb") # wb는 쓰기형태, 바이너리를 의미한다. 피클을 사용하려면 반드시 바이너리 타입을 정의해줘야한다. 그리고 피클에서 따로 인코딩을 설정할 필요가 없다. 
























