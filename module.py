# 모듈 만들기

# 일반_ 가격
def price(people):
    print(f"{people}명 가격은 {people*10000}원 입니다")

# 조조할인
def price_morning(people):
    print(f"{people}명 조조 할인 가격은 {people*6000}원 입니다.")

# 군인 할인
def price_soldier(people):
    print(f"{people}명 군인 할인 가격은 {people*4000}원 입니다.")
    