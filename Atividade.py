class Carro :

    def __init__(self, marca, velocidade, placa, cor) :
        self.marca = marca
        self.velocidade = velocidade
        self.placa = placa
        self.cor = cor

    def get_marca(self) :
        return self.marca
    
    def get_velocidade(self) :
        return self.velocidade

    def get_placa(self) :
        return self.placa

    def get_cor(self) :
        return self.cor
    