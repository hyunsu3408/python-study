# 상속 하는 클래스: 부모 클래스
# 상속 받는 클래스: 자식 클래스

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self,location):
        print("{0}: {1} 방향으로 적군을 공격중입니다.[공격력 {2}]"\
            .format(self.name,location,self.damage))
    
    def damaged(self,damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 다중 상속 해보기

# 드랍쉽 : 공중, 수송기.

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed= flying_speed
        
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)

# 발키리 : 공중 유닛. 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
