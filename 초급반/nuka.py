class charater:
    def __init__(self):
        self.level = 1
        self.exp = 0      
        

    def level_up(self):
        pritnt("level up")
        self.level += 1
      

    def kill_monster(self):
        print("kill monster")
        self.exp += 10
        # 만약 경험치가 100 되면 level_up 함수를 호출해서 level up을 시키자
    
        if self.exp == 100:
            self.level_up()
        
        
nuka = charater()
print(nuka.exp)
nuka.kill_monster()
print(nuka.exp)

# #a랑 b 를 함수 def sum(a,b)에 넣었을 때 더한 값을 return 하는 함수

#계산 클래스 예시
class Calculator:

def sum(self,a,b):
    return a+b

def minus(self,a,b):
    return a-b

#함수호출할떄는 함수이름 + 괄호 + 함수 괄호 안에 들어가는 값

#클래스 안에 들어가는 함수 괄호안 첫번쨰에는 self를 써준다.

calculator = Calculator()

a = 3
b = 5
calculator.sum(a,b)

#코딩 잘 하는 법 -> 엄청 많이 하자


