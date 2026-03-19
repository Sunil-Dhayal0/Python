class A:
    def __init__(self):
        self.__x = 10

    def get(self):
        return self.__x

obj = A()
obj.__x = 50   #python think user want to create new public attribute

print(obj.get(), obj.__x)
