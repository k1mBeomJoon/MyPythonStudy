'''
    
'''

# 다이아몬드 상속 - 좋지 않은 상속 구조임.
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass    # 내부동작 필요없고, 빈 껍데기만 개념적으로 필요할 때 pass를 사용


# x.greeting() 하면 어떤 클래스의 greeting() 메서드가 호출될까?
x = D()
x.greeting()

# 상속 관계가 복잡해서 자식클래스에서 메서드를 호출했을 때 어떤 부모클래스의 메서드가 호출될지 모르면 mro() 를 찍어서 확인.
print(D.mro())
