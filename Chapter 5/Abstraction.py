from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(ElectronicDevice):
    def turn_on(self):
        print("TV is now on")

    def turn_off(self):
        print("TV is now off")


class Radio(ElectronicDevice):
    def turn_on(self):
        print("Radio is now on")

    def turn_off(self):
        print("Radio is now off")


def operate_device(device):
    device.turn_on()
    device.turn_off()


my_device = TV()
my_radio = Radio()

operate_device(my_device)
operate_device(my_radio)