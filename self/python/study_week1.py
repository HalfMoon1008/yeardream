import numpy as np

# print("naver;kakao;sk;samsung")

# print("naver", "kakao", "samsung", sep=";")

# sep을 사용하면 같은 프린트 내부의 글자들 사이에 구분자로 sep=""안의 내용을 넣을 수 있다.


# print("first", end="");print("second")

# license_plate = "24가 2210"
# print(license_plate[-4:])

# string = "홀짝홀짝홀짝"
# print(string[::2])
# [:::]에는 각각 [시작 인덱스:끝 인덱스:오프셋]을 지정할 수 있다.
# 오프셋은 특정 조건으로 리스트를 저장한다. 위 코드에서는 시작 인덱스에서부터
# 2번째 뒤 인덱스까지 지정해서 출력해준다.

# string = "PYTHON"
# print(string[::-1])
# 오프셋을 지정할 때, -1로 조건을 지정하면 뒤에서부터
# 인덱스를 출력한다. 그렇기에 문자열을 뒤집는 효과가 있다.

# phone_number = "010-1111-2222"
# a = phone_number.replace("-"," ")
# print(a)
# replace 함수를 이용하면 특정 문자열을 변경할 수 있다.
# 대신 다 바뀌니까... 일부만 바꾸고 싶으면 인덱싱으로 특정 범위만 끌어온 뒤에
# replace하는 방법으로 하던가.. 해야할듯?

# url = "http://sharebook.kr"
# a = url.split('.')
# print(a)
# print(a[-1::])

# a[x]의 방법으로는 a안에있는 x번째 인덱스를 바꿀 수 없다.
# 그러면 어떻게 해야됨??
# QQQQQQQQQQQQQ

# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# 출력 결과 : abcd
# .replace를 할 경우, 메모리에 새로운 구역이 생김
# 기존의 string -> 'abcd'를 가르키고
# string.replace으로 새롭게 만들어진 메모리 구역에 'aBcd'가 들어간다.
# 하지만 a = string.replace('b','B')의 형태로 어떠한 변수에 해당 값을
# 바인딩한 것이 아닌, print(string)을 했기 때문에
# 해당 코드의 출력값은 기존의 string값인 abcd가 된다.

# letters = 'python'
# print(letters[0:3:2])
# 요 코드는 좀 억지로 끼워맞춘 느낌..?
# print(lang[0], lang[2])


# a = np.arange(1,4)
# b = np.arange(4,7)
# ab = a+b
# print(type(a))
# print(type(b))
# print(type(ab))
# print(a + b)

# c = [1,2,3]
# d = [4,5,6]
# cd = c + d
# print(type(c))
# print(type(d))
# print(type(cd))
# print(cd)


# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름 : %s 나이 : %d" % (name1, age1))
# print("이름 : %s 나이 : %d" % (name2, age2))

# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# fomanting은 두 가지 방법으로 가능하다.
# 첫 번째 방법은 첫 문제와 JAVA처럼 %를 이용한 formating방법
# 두 번째 방법은 .format함수를 이용한 .format(name1,age1)의 방법
# 세 번째 방법은 {}를 이용한 방법. {}안에 변수를 넣어주면 된다.


# 상장주식수 = "5,969,782,550"
# a = int(상장주식수.replace(",",""))
# print(a)


# 분기 = "2020/03(E) (IFRS연결)"
# b = 분기.split(" ")[0].split("(")
# print(b[0])


# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)
# .strip()을 통해서 String문자열 안에 있는 공백을 제거할 수 있다.


# ticker = "btc_krw"
# a = ticker.upper()
# print(a)
# .upper()를 통해 Stirng안에 있는 영문자를 대문자로 변환할 수 있다.

# ticker = "BTC_KRW"
# a = ticker.lower()
# print(a)
# .lower()를 통해 Stirng안에 있는 영문자를 소문자로 변환할 수 있다.

# a = "hello"
# b = a.capitalize()
# print(a)
# .capitalize() 함수는 String 문자열 안에 있는 글자의 첫 글짜를 대문자로 변경한다.

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))
# .endswith()을 통해서 (" ~ ")의 ~내용을 확장자를 참, 거짓 값으로 확인할 수 있다.

# file_name = "보고서.xlsx"
# a = file_name.endswith(("xlsx","xls"))
# print(a)
# .endswith()는 복수의 조건으로 확장자 검색이 가능하다.
# 이때, 복수의 확장자를 사용할 경우, ()로 내부를 묶어줘야한다.
# .endswith( ("a","b") ) 처럼

# file_name = "2020_보고서.xlsx"
# a = file_name.startswith("2020")
# print(a)
# .startswith()의 형태로 endswith()처럼 사용할 수 있다.
# endswith와는 다르게 startswith는 첫 글자부터 시작해서 참 거짓을 구분한다.

# date = "2020-05-01"
# a = date.split("-")
# print(a)
# b = a[0]
# c = a[1]
# d = a[2]
# print(b+"년 "+c+"월 "+d+"일")


# data = "039490     "
# a = data.strip()
# print(a)

# data = "039490     "
# a = data.rstrip()
# print(a)
# rstrip을 통해서 오른쪽의 공백만 제거할 수 있다.


# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# movie_rank.insert(1, "슈퍼맨")
# del movie_rank[3]
# del movie_rank[2]
# del movie_rank[2]

# 리스트의 이름 뒤에 .apend를 추가해주는 것을 통해서 리스트에 항목 추가가 가능
# insert를 통해 1번 인덱스 자리에 원하는 값을 넣을 수 있다. 1번 인덱스에 위치하던 항목은 2번 인덱스로 밀려난다.
# del을 이용하여 특정 인덱스 삭제 가능

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# 합연산을 통해 인덱스 뒤에 인덱스를 이어붙이는 것이 가능하다.

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max : ", max(nums))
# print("min : ", min(nums))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# average = sum(nums) / len(nums)
# print(average)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])
# 날짜만 제외한 설정이 아닌, 1번 인덱스부터 출력하게 하는 인덱싱

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])
# num[ x : y : z ]
# x = 출력할 인덱스의 시작 지점
# y = 출력할 인덱스의 마지막 지점
# z = 출력할 인덱싱의 조건
# ex) [::2] = 시작지점부터 2번째 인덱스를 출력하겠다. (퐁당퐁당하겠다)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))
# .join() 메소드를 통해서 출력 될 값 사이사이의 텍스트를 지정할 수 있다

# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# my_variable = ()
# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# 리스트는 [], 튜플은 ()로 정의한다.

# a = (1, )

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# data = list(interest)
# list()를 통해 튜플을 리스트화 할 수 있다.

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# a, b, c = 'apple', 'banana', 'cake'

# data = tuple(range(2, 100, 2))

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _ = scores
# print(valid_score)


# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = scores
# print(valid_score)


# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *valid_score, b = scores
# print(valid_score)


# temp = {}

# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(ice)


# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)

# print("메로나 가격: ", ice["메로나"])

# ice["메로나"] = 1300

# del ice["메로나"]

# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}

# print(inventory["메로나"][0], "원")

# print(inventory["메로나"][1], "개")

# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}
# inventory["월드콘"] = [500, 7]
# 딕셔너리는 위와 같이 값 추가가 가능하다.

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.keys())
# print(ice)
# 변수명.key()를 통해서 키값만 가져오는 것이 가능
# ice = list(icecream.values())
# 역 또한 같다.

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(sum(icecream.values()))
# value값 sum

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)
# 변수명.update(추가할 딕셔너리명) 으로 값 추가 가능

# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)
# zip으로 keys와 vals를 묶고, dict로 변환
# Q) 인덱스의 수가 맞지 않는다면?

# time = input("현재시간: ")
# if time[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
# 신박한 인덱싱 방법

# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은?")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")
# if문 헷갈릴 때 볼 수 있는 if 예제

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 과일은?")
# if user in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")
# if와 딕셔너리를 이용한 문제


# 환율 = {"달러": 1167,
#         "엔": 1.096,
#         "유로": 1268,
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")
# 효율적인 계산 반복문

# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")
# split과 if문

# 주민번호 = input("주민등록번호: ")
# 주민번호 = 주민번호.split("-")[1]
# if 주민번호[0] == "1" or 주민번호[0] == "3":
#     print("남자")
# else:
#     print("여자")

# num = input("주민등록번호: ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)

# if num[-1] == 계산3[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])

# if (시가+변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")

# 리스트 = ["가", "나", "다", "라"]
# for 변수 in 리스트[: :2]:
#   print(변수)
# 인덱싱

# 리스트 = ["가", "나", "다", "라"]
# for 변수 in 리스트[: :-1]:
#   print(변수)
# 역순 인덱싱