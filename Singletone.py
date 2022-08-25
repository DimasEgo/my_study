class Singletone:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance

    def __init__(self, value):
        self.value = value


class Singletone_v2:
    instance_dict = {
        'name': 'Dimas',
        'age': '32',
        'weight': '71'
    }

    def __init__(self):
        self.__dict__ = self.instance_dict


s1_1 = Singletone(10)
s1_2 = Singletone(20)

print(s1_1.value, s1_2.value)

s2_1 = Singletone_v2
s2_2 = Singletone_v2
s2_1.instance_dict['name'] = 'Olga'
print(s2_2.instance_dict['name'])
