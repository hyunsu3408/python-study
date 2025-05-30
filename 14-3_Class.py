# 메소드 응용
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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

# 파이어뱃 : 공격 유닛
firebat= AttackUnit("파이어뱃",50,16)
firebat.attack("5시")

# 공격 2번 받는다고 가정
firebat.damaged(25)
firebat.damaged(25)