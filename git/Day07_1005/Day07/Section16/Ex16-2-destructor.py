'''
    소멸자
        인스턴스(객체)가 소멸될 때 자동으로 호출된다.

'''

class Service:
    def __init__(self, service):
        self.service = service
        print('{} Sercive가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{} Sercive가 종료되었습니다'.format(self.service))

s = Service('길 안내')
del s