from pay import Pay
from paypal import PayPal
from card import Card
from cash import Cash

def process_pay(payment_method, amount):
  return payment_method.make_pay(amount)

# def process_pay(payment_method, amount):
#   # Tu código aquí 👇
#     method = payment_method.lower()
#     if method == "card":
#         pay = Card("4913478952471122")
#         return pay.make_pay(amount)
#     elif method == "paypal":
#         paypal = PayPal("test@mail.com")
#         return paypal.make_pay(amount)
#     elif method == "cash":
#         cash = Cash()
#         return cash.make_pay(amount)
#     else:
#         raise ValueError("Método de pago no válido")
    
print(process_pay(card, 100))
print(process_pay(paypal, 240))
print(process_pay(cash, 400))