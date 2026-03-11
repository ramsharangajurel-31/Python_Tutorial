# Important=======================Ducktyping in Inheritance & Polymorphism
class Bird:
    def fly(self):
        print("Bird can fly")
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies fast")
class Airplane:
    def fly(self):
        print("Airplane flies in the sky")
def make_it_fly(obj):
    obj.fly()
b=Bird()
s=Sparrow()
a=Airplane()
make_it_fly(b)
make_it_fly(s)
make_it_fly(a)