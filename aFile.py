class A:
    def foo(self):
        print("Foo method called")


print(__name__)
if __name__ == "__main__":
    a = A()
    a.foo()


