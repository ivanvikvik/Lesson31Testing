from manager import Manager
from car import Car
from plane import Plane

car1 = Car(100)
car2 = Car(50)
car3 = Car(60)
plane1 = Plane(1050)
plane2 = Plane(840)

Manager.run((car1, car2, car3, plane1, plane2))
