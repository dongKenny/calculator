class Calculator():
    def __init__(self, initial_calculation=0):
        if type(initial_calculation) != int and type(initial_calculation) != float:
            raise ValueError("INVALID INPUT")
        self.__last_calculation = initial_calculation

    def get_last_calculation(self):
        return self.__last_calculation

    def add(self, addend1, addend2=0):
        try:
            value = addend1 + addend2
            return self.set_last_calculation(value)
        except TypeError:
            return "INVALID INPUT"

    def subtract(self, subtrahend1, subtrahend2=0):
        try:
            value = subtrahend1 - subtrahend2
            return self.set_last_calculation(value)
        except TypeError:
            return "INVALID INPUT"

    def set_last_calculation(self, value):
        if type(value) != int and type(value) != float:
            return "INVALID INPUT"
        self.__last_calculation = value
        return value
