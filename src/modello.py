class Cliente:
    def __init__(self, cf, nome):
        self.cf = cf
        self.nome = nome

class Prodotto:
    def __init__(self, id, nome, prezzo):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo

class Ordine:
    def __init__(self, cliente, prodotto):
        self.cliente = cliente
        self.prodotto = prodotto
        self.totale = prodotto.prezzo
