class Conta:
    # método construtor
    def __init__(self, titular, agencia, numero):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = 0
    
    #encapsulamento (getters e setters)
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, novo_nome):
        self.__titular = novo_nome
    @property
    def agencia(self):
        return self.__agencia
    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo

    # métodos da classe
    def extrato(self):
        print(f"O saldo da {self.__titular} é {self.__saldo}")

    def deposito(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
            print("Depósito efetuado com sucesso!")
        else:
            print("Não foi possível depositar!")

    def saque(self, valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo = self.__saldo - valor
            print("Saque efetuado com sucesso!")
        else:
            print("Erro ao efetuar saque")

    def transferir(self, valor, conta_destino):
        self.saque(valor)
        conta_destino.deposito(valor)
