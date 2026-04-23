class Foo:
    def __init__(self, x=None):
        self._x =x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = -10
    
foo = Foo(10)

# Sem adicionar '@property' é como um método, ou seja, precisa usar '.x()'
# print(foo.x())

# Usando a notação '@property' vira um "atributo", são se usa '()'
print(foo.x)

# Exemplo usando o Setter:
foo.x = 20
print(foo.x)

# Exemplo usando o Deleter:
del foo.x
print(foo.x)