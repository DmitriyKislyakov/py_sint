from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def __init__(self, eng_status=False):
        self.__engine_status = eng_status

    def start_engine(self):
        print('Заводится двигатель авто')
        self.__engine_status = True

    def stop_engine(self):
        print('Двигатель авто заглушен')
        self.__engine_status = False

    def move(self):
        if self.__engine_status:
            print('Автомобиль поехал')
        else:
            print('Авто не может двигаться с заглушенными двигателем')


class Boat(Transport):
    def __init__(self, eng_status=False):
        self.__engine_status = eng_status

    def start_engine(self):
        print('Лодка завела мотор')
        self.__engine_status = True

    def stop_engine(self):
        print('Лодка заглушила мотор')
        self.__engine_status = False

    def move(self):
        if self.__engine_status:
            print('Лодка плывет с заведенным мотором')
        else:
            print('Лодка плывет по течению')


car = Car()
car.start_engine()
car.move()
car.stop_engine()
car.move()
print()
boat = Boat()
boat.start_engine()
boat.move()
boat.stop_engine()
boat.move()
