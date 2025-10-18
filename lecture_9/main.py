from enum import StrEnum
from typing import Self
import random
class Names(StrEnum):
    JOHN = "John Lenon"
    PAUL = "Paul McCartney"
    GEORGE  = "George Harrison"
    RINGO ="Ringo Starr"



class Beetle: 
    health_point = 100
    name = Names.JOHN
    def styling(self) -> str:
        if self.name is Names.JOHN:
            return "in Johny style"
        elif self.name is Names.PAUL:
            return "in MacCartney style"
        elif self.name is Names.GEORGE:
            return "George Harrison"
        return ("without name")
    
    def __init__(self, health_point = 100, name = Names.JOHN) -> None:
        
     self.health_point = health_point
     self.name = name  
    
    def __eq__(self, other: Self) -> bool:
        return self.health_point == other.health_point    
    
    def __lt__ (self, other: Self) -> bool:
        return self.health_point < other.health_point
    
    def __le__(self, other: Self) -> bool:
        return self.health_point <= other.health_point
    
    def __str__(self) -> str :
        return(f"Beetle(name =\"{self.name}\", health_point = {self.health_point})")
        
    def attack(self: Self, other: Self) -> None:
        print(f" {self.name} attacked other {other.name} {self.styling()} ")
        other.health_point -= 10
        
class BeetlesAemy:
    beetles_list: list[Beetle] = []
    beetles_names: Names
    beetles_max_health_point = 100
    beetles_army_size = 20
    
    def __init__(self, beetles_name: Names, beetles_max_health_points = 100) -> None:
        self.beetles_names = beetles_name
        self.beetles_max_health_point = beetles_max_health_points
        self.beetles_list = []
        
        for i in range(beetles_army_size):
            _beetle: Any = Beetle(
                health_point= random.randint(a = 1, b = self.beetles_max_health_point),
                name=self.beetles_names
                
            )
        self.beetles_list.append(_beetle)
    def print_army_listing()
if __name__ == "__main__":
      m1: Beetle= Beetle(health_point=100, name = Names.JOHN)
      m2: Beetle = Beetle(health_point=90, name = Names.PAUL)
      
print(m1==m2)
print (m1 != m2)
print (m2 >= m1)
print (m1, m2)
