from pay import Pay

class PayPal(Pay):
  # Tu código aquí 👇

  def __init__(self, email):
    self.email = email 

  def make_pay(self, cantidadpagar):
    paypal_object = super().make_pay(cantidadpagar)  
    paypal_object['platform'] = "PayPal"
    paypal_object['email'] = self.email
    return paypal_object

# paypal = PayPal("andresmr955@gmail.com")
# print(paypal.mak_pay(1000))
