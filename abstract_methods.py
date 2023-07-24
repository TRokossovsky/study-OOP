#  OOP and abstract methods practicing
from abc import ABC, abstractmethod


class BasicDevice(ABC):
    def __init__(self, label, production_year):
        self.label = label
        self.production_year = production_year

    @abstractmethod
    def get_info(self):
        ...


class BasicCallingDevice(ABC):
    @abstractmethod
    def call(self):
        ...


class BasicSMSDevice(ABC):
    @abstractmethod
    def send_sms(self):
        ...


class BasicInternetDevice(ABC):
    @abstractmethod
    def internet_connect(self):
        ...


class Smartphone(BasicDevice, BasicCallingDevice, BasicSMSDevice, BasicInternetDevice):
    def get_info(self):
        print(f'Label is {self.label}. Production year is {self.production_year}')

    def call(self):
        print('Calling...')

    def send_sms(self):
        print('Sending SMS')

    def internet_connect(self):
        print('Connecting to the Internet')


phone1 = Smartphone('Samsung', 2007)
phone1.get_info()
phone1.call()
phone1.internet_connect()
phone1.send_sms()
