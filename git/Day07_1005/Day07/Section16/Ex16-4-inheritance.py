'''
    상속
        어떤 클래스가 가지고 있는 기능을 그대로 물려받아 사용할 수 있는 클래스

    -사용방법

     class 슈퍼클래스
        본문
     class 서브클래스(슈퍼클래스)
'''

# 슈퍼클래스(부모클래스)
class Coffee:

    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))

# 서브클래스(자식클래스)
class Espresso(Coffee):

    def __init__(self, bean, water):
        super().__init__(bean)      # 슈퍼클래스의 bean을 끌고와서 사용
        self.water = water

    def espresso_info(self):
        super().coffee_info()       # 슈퍼클래스의 coffee_info() 메서드를 끌고와서 사용
        print('물 : {}ml'.format(self.water))

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

coffee.coffee_info()    # 서브클래스 객체로부터 슈퍼클래스의 메서드를 호출할 수 있음.