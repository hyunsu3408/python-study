class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# super를 사용하면 맨 마지막에 사용하는 
# 클래스의 init이 호출된다
class FlyableUnit(Unit,Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
        
# 드랍쉽
dropship = FlyableUnit()