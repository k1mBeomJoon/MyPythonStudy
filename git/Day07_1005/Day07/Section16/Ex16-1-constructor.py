'''
    생성자
        인스턴스(객체)를 생성할 때, 생성자가 자동으로 호출된다.
        객체 초기화용으로 사용한다.
'''

class USB:
    # 생성자 - 객체가 생성될 때 무조건 실행됨.
    def __init__(self, capacity):
        self.capacity = capacity
        print('USB 생성자가 호출되었습니다.')

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)   # 생성자에 파라미터가 있으므로 객체 생성시에도 파라미터값을 넣어줘야함.
usb.info()

