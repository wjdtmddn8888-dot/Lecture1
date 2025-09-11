class Temperature:
    # TODO: Class attribute
    unit = "Celsius"

    def __init__(self, value):
        # TODO: Instance attribute
        self.value = value

    # TODO: Instance method
    def display(self):
        print(f"{self.value}° {self.unit}")

    # TODO: Class method with relevant decorator
    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit

    # TODO: Static method with relevant decorator
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# Step 2
# A
temp_obj = Temperature(100)
print("A. 초기 온도:")
temp_obj.display()

# B
fahrenheit_temp = Temperature.to_fahrenheit(100)
print(f"\nB. 100°C를 화씨로 변환: {fahrenheit_temp}°F")

# C
print("\nC. 단위를 Kelvin으로 변경 후:")
Temperature.change_unit("Kelvin")
temp_obj.display()

# D
#
# unit은 class attribute로 이 클래스의 모든 인스턴스가
# 공유하는 값이다 따라서 change_unit을 통해 값을
# 변경하면해당 클래스로부터 생성된 모든 객체에 그 변경 사항이
# 반영된다