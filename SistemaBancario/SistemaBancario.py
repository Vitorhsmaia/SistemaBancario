class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        self.transacoes.append(descricao)

    def exibir_transacoes(self):
        for transacao in self.transacoes:
            print(transacao)


class Cliente:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome:
            self._nome = novo_nome
        else:
            raise ValueError("Nome não pode ser vazio.")

    @property
    def cpf(self):
        return self._cpf


class Conta:
    _numero_conta_sequencial = 1  

    def __init__(self, cliente):
        self._saldo = 0
        self._numero = Conta._numero_conta_sequencial
        Conta._numero_conta_sequencial += 1
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
            self._historico.adicionar_transacao(f"Saldo atualizado para R$ {valor}")
        else:
            raise ValueError("O saldo não pode ser negativo.")

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, novo_cliente):
        if novo_cliente:
            self._cliente = novo_cliente
        else:
            raise ValueError("O cliente não pode ser vazio.")

    @classmethod
    def proxima_conta(cls):
        return cls._numero_conta_sequencial

    def exibir_historico(self):
        print(f"Histórico da conta {self.numero}:")
        self._historico.exibir_transacoes()


class ContaCorrente(Conta):
    def __init__(self, cliente, limite):
        super().__init__(cliente)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        if novo_limite >= 0:
            self._limite = novo_limite
        else:
            raise ValueError("O limite não pode ser negativo.")

    def sacar(self, valor):
        if valor <= (self.saldo + self._limite):
            self.saldo -= valor
            self._historico.adicionar_transacao(f"Saque de R$ {valor}")
        else:
            raise ValueError("Saldo insuficiente com o limite.")


class ContaPoupanca(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)

    def render_juros(self, taxa):
        if taxa > 0:
            rendimento = self.saldo * taxa
            self.saldo += rendimento
            self._historico.adicionar_transacao(f"Juros de R$ {rendimento} aplicados")
        else:
            raise ValueError("A taxa de juros deve ser positiva.")



cliente1 = Cliente("Cliente 1", "123.456.789-00")
conta_corrente1 = ContaCorrente(cliente1, limite=500)
print(f"Conta Corrente criada com número: {conta_corrente1.numero} para {conta_corrente1.cliente.nome}")


conta_corrente1.saldo = 1000.00
print(f"Saldo atual: R$ {conta_corrente1.saldo}")


conta_corrente1.sacar(1300.00)
print(f"Saldo após saque: R$ {conta_corrente1.saldo}")


conta_corrente1.exibir_historico()


cliente2 = Cliente("Cliente 2", "987.654.321-00")
conta_poupanca1 = ContaPoupanca(cliente2)
conta_poupanca1.saldo = 2000.00
conta_poupanca1.render_juros(0.05)  


conta_poupanca1.exibir_historico()

