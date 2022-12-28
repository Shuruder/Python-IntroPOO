class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a Instancia da Classe...")
        
    def falar(self):
        print("AUAU")
        
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto", False)
    print(c.nome)
    
c = Cachorro("Chappie", "Amarelo")
c.falar()

print("-------")
del c
print("-------")
print("-------")
print("-------")

criar_cachorro()