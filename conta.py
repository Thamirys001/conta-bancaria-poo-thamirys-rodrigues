#ContaBancária
class Titular:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def apresentar(self):
        print(f"Olá, {self.titular}! seu saldo é {self.saldo}")

        
cliente1 = Titular("Thamirys", 100)
cliente1.apresentar()
