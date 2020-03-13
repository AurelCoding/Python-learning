class Car:
    def __init__(self):
        print('the __init__ is called')


ford = Car()
honda = Car()
audi = Car()

ford.speed = 200
honda.speed = 220
audi.speed = 250

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'

print(ford.speed)
print(ford.color)

ford.speed = 300
ford.color = 'blue'

print(ford.speed)
print(ford.color)
