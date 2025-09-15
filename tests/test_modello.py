from src.modello import Cliente, Prodotto, Ordine

def test_creazione_cliente():
    c = Cliente("ABC123", "Mario")
    assert c.cf == "ABC123"
    assert c.nome == "Mario"

def test_creazione_prodotto():
    p = Prodotto(1, "Laptop", 1000)
    assert p.nome == "Laptop"
    assert p.prezzo == 1000

def test_creazione_ordine():
    c = Cliente("ABC123", "Mario")
    p = Prodotto(1, "Laptop", 1000)
    o = Ordine(c, p)
    assert o.totale == 1000
