class Car:
  def __init__(self, brand, name, price, year, damage, last_seen, id=None):
    self.id = id
    self.brand = brand
    self.name = name
    self.price = price
    self.year = year
    self.damage = damage
    self.last_seen = last_seen

  @staticmethod
  def from_dict(data_dict):
    return Car(**data_dict)
  
  def to_dict(self):
    return {
      'id': self.id,
      'brand': self.brand,
      'name': self.name,
      'price': self.price,
      'year': self.year,
      'damage': self.damage,
      'last_seen': self.last_seen,
    }
    