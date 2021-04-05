class Engine:
    engine_name = "4-stroke"
class Car(Engine):
    pass

#single inheritance
c = Car()
print(c.engine_name)
