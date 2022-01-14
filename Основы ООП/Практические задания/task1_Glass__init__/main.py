from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("...error...")
        if capacity_volume <= 0:
            raise TypeError("....eerrroorr...")
        self.capacity_volume = capacity_volume   #  TODO инициализировать объект "Стакан"
        self.occupied_volume = capacity_volume

if __name__ == "__main__":
    glass_1 = Glass(200, 100)  # TODO инициализировать два объекта типа Glass
    glass_2 = Glass(250, 50)

    print(glass_1)
    print(glass_2)

    glass_3 = Glass(0, 11)
    print(glass_3)
    # TODO попробовать инициализировать не корректные объекты
