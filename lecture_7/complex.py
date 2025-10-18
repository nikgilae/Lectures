from abc import abstractmethod


class BaseDuck:
  wings: int = 2
  
  
  @abstractmethod
  def make_noise(self,valume.db: int) -> None:
    raise NotImplemented