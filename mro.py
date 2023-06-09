class A():
    def foo(self):
        print("A")

class B():
    def foo(self):
        print("B")
class C(A,B):
    def foo(self):
        print("C")
    pass

class D(C,A):
    pass

d = D()
d.foo()
print(D.__mro__)
