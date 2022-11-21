'''
    객체(object)란
        현실 세계에 존재하는 물리적, 추상적인 모든 것들을 프로그램으로 표현한 것
        ex. 학생, 자동차, 컴퓨터, 주문, 배송 등

    [객체 구성]
        속성값 - 변수
        기능 - 메서드(함수)


'''

# Computer 클래스 정의 / class명의 첫 글자는 대문자로 하는게 굿
class Computer:
    # 첫번째 매개변수가 self 이므로 인스턴스 메서드이다.
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달된다.
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd
    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer()    # Computer 객체생성
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
print(desktop.cpu)
desktop.hardware_info()
print()

macbook = Computer()
macbook.set_spec('M2', '16GB', 'intel', '512GB')
print(macbook.cpu)    
macbook.hardware_info()


'''
# 객체 생성 하지 않고 함수로만 하면
cpu = ''
ram = ''
vga = ''
ssd = ''
def set_spec1(cpu, ram, vga, ssd):
    cpu = cpu
    ram = ram
    vga = vga
    ssd = ssd

set_spec1('i7', '16GB', 'GTX3060', '512GB')
print(cpu)
'''