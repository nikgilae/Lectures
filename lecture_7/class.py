class HumanInLaw: 
  name: str = "Ilya"
  eyes: int = 2
  hands: int = 2
  legs: int = 2
  hair_colot: str = "brown"
  

  
  
  
  def blink(self):
    name = 'Vova'
    print(f"{self.name} blinked")
    
  def walk(self):
    print(f"{self.name} walked")
  
  
class SmartHuman(HumanInLaw):
  glasses: bool = True
  iq: int = 130

  
  
if __name__ == '__main__':
  human1 = HumanInLaw()
  human1.walk()
  human1.blink()
  smart_human = SmartHuman()
  smart_human.blink()
