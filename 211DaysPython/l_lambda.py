messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

print(messages[0]['sender'])
user = 'Alice'

def filter_user_messages(messages, user):
  # Tu código aquí 👈
     return list(filter(lambda x: x['sender'] == user, messages))

print(filter_user_messages(messages, user))