from pay import Pay

class Card(Pay):
  # Tu código aquí 👇
  def __init__(self, numerocard):
    self.numerocard = numerocard
  
  def make_pay(self, cantidadpagar):
    if len(self.numerocard) >= 16:
        card_object = super().make_pay(cantidadpagar)
        card_object['last_card_numbers'] = self.numerocard[12:]
        return card_object
    else:
       raise Exception("The card number is not valid")
    
# card = Card("123456789122356")
# print(card.make_pay(200))