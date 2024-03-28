class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round(celsius * 1.80 + 32.0, 5)
        return [kelvin, fahrenheit]

temperature = Solution()
print(temperature.convertTemperature(36.50))
