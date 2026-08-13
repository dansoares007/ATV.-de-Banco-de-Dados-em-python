from dataclasses import dataclass
import json
import os

@dataclass
class Carro:
    codigo: int
    placa: str
    velocidade: int
    cor: str
    ano: int

carros = []

def salvar():
    with open("carro.txt", "w", encoding="utf-8") as f:
        json.dump([c.__dict__ for c in carros], f, indent=4)

def carregar():
    global carros
    if os.path.exists("carro.txt"):
        with open("carro.txt", "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                carros = [Carro(**d) for d in dados]
            except json.JSONDecodeError:
                carros = []

def inserir(carro):
    carros.append(carro)
    salvar()

def atualizar(codigo, novo_placa=None, novo_velocidade=None, novo_cor=None, novo_ano=None):
    for c in carros:
        if c.codigo == codigo:
            if novo_placa: c.placa = novo_placa    
            if novo_cor: c.cor = novo_cor        
            if novo_velocidade is not None: c.velocidade = novo_velocidade
            if novo_ano is not None: c.ano = novo_ano  
            salvar()
            return True
    return False

def deletar(codigo):
    global carros
    carros = [c for c in carros if c.codigo != codigo]
    salvar()

def consulta(codigo):
    for c in carros:
        if c.codigo == codigo:
            return c
    return None

def mostrar_todos():
    return carros

def consultar_placa(placa):
    return [c for c in carros if placa.lower() in c.placa.lower()]

def menu():
    print('1 - inserir')
    print('2 - atualizar')
    print('3 - deletar')
    print('4 - mostrar todos')
    print('5 - consultar placa')
    print('6 - consultar codigo')
    print('0 - SAIR')
    return input('Digite qual função deseja: ')

#executando

carregar()

if __name__ == "__main__" :
    carregar()

while True:

    resposta = menu()

    match resposta:
        case '1':
            carro_codigo = int(input("Digite o código do carro: "))
            carro_placa = input("Digite a placa do carro: ")
            carro_velocidade = int(input("Digite a velocidade do carro: "))
            carro_cor = input("Digite a cor do carro: ")
            carro_ano = int(input("Digite o ano do carro: "))
            carro = Carro(carro_codigo, carro_placa, carro_velocidade, carro_cor, carro_ano)
            inserir(carro)
            print("Inserido, papai!!!!!!!")

        case '2':
            print("1 - Atualizar placa\n2 - Atualizar velocidade\n3 - Atualizar cor\n4 - Atualizar ano\n")
            op = input("Escolha: ")
            match op:
                case '2':
            # Primeiro, pegamos o código do carro que vai sofrer a alteração
                    codigo_alvo = int(input("Digite o código do carro que deseja atualizar: "))
                    
                    print("1 - Atualizar placa\n2 - Atualizar velocidade\n3 - Atualizar cor\n4 - Atualizar ano\n")
                    op = input("Escolha: ")
                    
                    match op:
                        case '1':
                            nova_placa = input("Digite a nova placa: ")
                            if atualizar(codigo_alvo, novo_placa=nova_placa):
                                print("Placa atualizada com sucesso, papai!")
                            else:  
                                print("Carro não encontrado.")
                                
                        case '2':
                            nova_velocidade = int(input("Digite a nova velocidade: "))
                            if atualizar(codigo_alvo, novo_velocidade=nova_velocidade):
                                print("Velocidade atualizada com sucesso!")
                            else:
                                print("Carro não encontrado.")
                                
                        case '3':
                            nova_cor = input("Digite a nova cor: ")
                            if atualizar(codigo_alvo, novo_cor=nova_cor):
                                print("Cor atualizada com sucesso!")
                            else:
                                print("Carro não encontrado.")
                                
                        case '4':
                            novo_ano = int(input("Digite o novo ano: "))
                            if atualizar(codigo_alvo, novo_ano=novo_ano):
                                print("Ano atualizado com sucesso!")
                            else:
                                print("Carro não encontrado.")
                                
                        case _:
                            print("Opção de atualização inválida.")

                case '3': 

                    ctemp = input("Digite o codigo do carro que você quer deletar: ")
                    deletar(ctemp)

                case '4':
                    for c in motrar_todos():
                        print(c)

                case '5':

                    placa = input("Digite a placa que deseja consultar: ")
                    consultar_placa(placa)

                case '6':

                    ctemp = input("Digite um trecho do codigo que quer consultar: ")
                    consulta(ctemp)

                case '0': 
                    print("SaInDo...")
                    break

                case _:
                    print("Numero digitado não está na sequência. Tente novamente, fi!!!!!!!!!")

