class usuario:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def hacer_deposito(self, amount):
        self.balance += amount
    def hacer_retiro(self, amount):
        self.balance -= amount
    def mostrar_balance_usuario(self):
        print(f"Nombre de usuario: {self.name}, Balance: {self.balance}")
    def transferir_dinero(self, destiny, amount):
        self.balance -= amount
        destiny.hacer_deposito(amount)

usuario1 = usuario("Juan", 0)
usuario2 = usuario("Francisco", 0)
usuario3 = usuario("Alexis", 0)

usuario1.hacer_deposito(50)
usuario1.hacer_deposito(50)
usuario1.hacer_deposito(50)
usuario1.hacer_retiro(50)

usuario2.hacer_deposito(70)
usuario2.hacer_deposito(70)
usuario2.hacer_retiro(40)
usuario2.hacer_retiro(40)

usuario3.hacer_deposito(200)
usuario3.hacer_retiro(50)
usuario3.hacer_retiro(50)
usuario3.hacer_retiro(50)

usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()

usuario1.transferir_dinero(usuario3, 100)

usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()