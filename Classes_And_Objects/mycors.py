from Class_Carrs import *
import time


car1 = Cars("BMW", 200, "Red")
car2 = Cars("OlWA", 100, "Blue")
car3 = Cars("Tata", 300, "White")

print(f"{car1.main()}\n{car2.main()}\n{car3.main()}")

time.sleep(1)
print(f"\n{car1.CarName()} prise: ${car1.prise}")

print(id(car1.CarName()))
print(id(car2.CarName()))
