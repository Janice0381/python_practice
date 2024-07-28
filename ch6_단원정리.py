'''
#1
name=input('당신의 이름은 무엇인가요? ')
print('하이',name,'씨 만나서 반가워요.')

#2
city=input('당신의 고향은 어디인가요? ')
print('당신은 아름다운',city,'에서 왔군요.')

#3
number=int(input('당신의 좋아하는 숫자는? '))
addTen=number+10
print('아하 당신이 좋아하는 숫자에 10을 더하면',addTen,'이군요.')

#4
print('환전 계산 프로그램입니다.')
koreanMoney=int(input('한국 돈 입력: '))
americanMoney=koreanMoney//1175
print(koreanMoney,'원을 환전하면',americanMoney,'달러입니다.')

#5
height=int(input('키를 입력하세요: '))
weight=(height-100)*0.9
print('당신의 키',height,'cm에 대한 적정몸무게:',int(weight),'kg')

#6
radius=int(input('반지름 입력: '))
area=radius**2*3.141592
print('원의 넓이는',area,'입니다.')
circumference=radius*2*3.141592
print('원의 둘레는',circumference,'입니다.')

#7
x=int(input('X를 입력하세요 > '))
y=int(input('Y를 입력하세요 > '))
product=x*y
print(x,'과',y,'를 곱한 값은',product,'입니다.')

#8
print('=== 인치->센티미터 변환 프로그램 ===')
inch=int(input('인치 입력: '))
centimeter=inch*2.54
print(inch,'inch는',centimeter,'cm 입니다.')

#9
print('=== 센티미터->인치 변환 프로그램 ===')
centimeter=float(input('센티미터 입력: '))
inch=centimeter/2.54
print(centimeter,'cm',inch,'inch 입니다.')
'''
#10
import calendar
year=int(input('출생연도를 입력하세요 > '))
month=int(input('출생월을 입력하세요 > '))
calendar.prmonth(year,month)

