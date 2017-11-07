''' Class '''
# 建立一個class


class People:
    ''' class people '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    '''  '''
    def say(self, msg):
        print(msg)


# 套用class
john = People('John Smith', 132)

print(john.name)
john.say('hello World')
