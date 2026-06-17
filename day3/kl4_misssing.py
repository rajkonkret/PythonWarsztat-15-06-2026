# słownik
# gdy nie ma klucza w słowniku: KeyError
# __missing__ - wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d1 = DefaultDict()
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1)  # {} - pusty słownik
print(d1['name'])  # default


# d2 = {}
# print(d2['name'])  # KeyError: 'name'

# słowink, który gdy nie ma klucza tworzy taki klucz z wartością domyslną np.: 0
class AutoDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key

a1 = AutoDict()
print(a1)
print(a1['name']) # name
print(a1) # {'name': 0}
