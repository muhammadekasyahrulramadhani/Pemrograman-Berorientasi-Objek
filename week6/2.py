from abc import ABC, abstractmethod

class Mesin(ABC):
    @abstractmethod
    def calculate_power(self):
        pass

class MesinBensin(Mesin):
    def __init__(self, horsepower, efficiency):
        self.horsepower = horsepower  # Daya mesin dalam tenaga kuda
        self.efficiency = efficiency    # Efisiensi mesin dalam persen

    def calculate_power(self):
        return self.horsepower * (self.efficiency / 100)

class MesinDiesel(Mesin):
    def __init__(self, horsepower, efficiency):
        self.horsepower = horsepower
        self.efficiency = efficiency

    def calculate_power(self):
        return self.horsepower * (self.efficiency / 100)


# Membuat objek dari setiap jenis mesin
petrol_engine = MesinBensin(150, 85)
print(f"Power of {type(petrol_engine).__name__}: {petrol_engine.calculate_power()}")

diesel_engine = MesinDiesel(200, 90)
print(f"Power of {type(diesel_engine).__name__}: {diesel_engine.calculate_power()}")