from pay import Pay

class Cash(Pay):
  def __init__(self):
    pass
  
  def make_pay(self, cantidadpagar):
    cash_object = super().make_pay(cantidadpagar)
    return cash_object
  
