class Glass:
    def __init__(self, material: str):
        self.material = material

    def get_material(self):
        return self.material

if __name__ == "__main__":
    ...







# from typing import Union
#
# class Glass:
#     def __init__(self, material: Union[str]):
#         self.material = material
#
#     def get_material(self, material: Union[str]) -> None:
#         if not isinstance(material, (str)):
#             raise TypeError
#
# if __name__ == "__main__":
#     glass = Glass("Рог виверны")
#     print(glass.material)
