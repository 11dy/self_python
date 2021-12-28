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




































