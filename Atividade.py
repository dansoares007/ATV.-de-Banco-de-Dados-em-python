from dataclasses import dataclass
import json
import os
from unittest import case

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
    if any(c.codigo == carro.codigo for c in carros):
        print(f"Erro: Já existe um carro com o código {carro.codigo}.")
        return
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
    print('\n1 - inserir')
    print('2 - atualizar')
    print('3 - deletar')
    print('4 - mostrar todos')
    print('5 - consultar placa')
    print('6 - consultar codigo')
    print('0 - SAIR\n')
    return input('Digite qual função deseja: ')

#executando

carregar()

if __name__ == "__main__" :
    carregar()

while True:

    resposta = menu()
    print("\n")

    match resposta:
        case '1':
            carro_codigo = int(input("Digite o código do carro: "))
            carro_placa = input("Digite a placa do carro: ")
            carro_velocidade = int(input("Digite a quilometragem percorrida pelo carro: "))
            carro_cor = input("Digite a cor do carro: ")
            carro_ano = int(input("Digite o ano do carro: "))
            carro = Carro(carro_codigo, carro_placa, carro_velocidade, carro_cor, carro_ano)
            inserir(carro)
            print("Inserido, papai!!!!!!!\n")

        case '2':
            print("1 - Atualizar placa\n2 - Atualizar quilometragem\n3 - Atualizar cor\n4 - Atualizar ano\n")
            op = input("Escolha: ")

            lista_carros = mostrar_todos()
            if not lista_carros:
                print("Nenhum carro cadastrado.")
            else:
                print("Escolha um dos seguinte códigos para atualizar:\n")
                for c in lista_carros:
                    print(f"Código: {c.codigo}")
            
            codigo_alvo = int(input("Digite o código do carro que deseja atualizar: "))
            if not any(c.codigo == codigo_alvo for c in carros):
                print("Carro não encontrado.")
                continue
            
            match op:
                case '1':
                    nova_placa = input("Digite a nova placa: ")
                    if atualizar(codigo_alvo, novo_placa=nova_placa):
                        print("Placa atualizada com sucesso, papai!")
                    else:  
                        print("Carro não encontrado.")
                        
                case '2':
                    nova_velocidade = int(input("Digite a nova quilometragem: "))
                    if atualizar(codigo_alvo, novo_velocidade=nova_velocidade):
                        print("Km atualizada com sucesso!")
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
            lista_carros = mostrar_todos()
            if not lista_carros:
                print("Nenhum carro cadastrado.")
            else:
                for c in lista_carros:
                    print(f"Código: {c.codigo}, Placa: {c.placa}, Quilometragem: {c.velocidade}, Cor: {c.cor}, Ano: {c.ano}")
            ctemp = int(input("Digite o codigo do carro que você quer deletar: "))
            deletar(ctemp)

        case '4':
            lista_carros = mostrar_todos()
            if not lista_carros:
                print("Nenhum carro cadastrado.")
            else:
                for c in lista_carros:
                    print(f"Código: {c.codigo}, Placa: {c.placa}, Quilometragem: {c.velocidade}, Cor: {c.cor}, Ano: {c.ano}")

        case '5':
            lista_carros = mostrar_todos()
            if not lista_carros:
                print("Nenhum carro cadastrado.")
            else:
                for c in lista_carros:
                    print(f"Placa: {c.placa}")

            placa = input("Digite a placa que deseja consultar: ")
            resultados = consultar_placa(placa)
            if resultados:
                for c in resultados:
                    print(f"Código: {c.codigo}, Placa: {c.placa}, Quilometragem: {c.velocidade}, Cor: {c.cor}, Ano: {c.ano}")
            else:
                print("Nenhum carro encontrado com essa placa.")   

        case '6':
            lista_carros = mostrar_todos()
            if not lista_carros:
                print("Nenhum carro cadastrado.")
            else:
                for c in lista_carros:
                    print(f"Código: {c.codigo}")
                        
            ctemp = int(input("\nDigite o código exato que quer consultar: "))
            carro_encontrado = consulta(ctemp)
            
            if carro_encontrado:
                print(f"Código: {carro_encontrado.codigo}, Placa: {carro_encontrado.placa}, Quilometragem: {carro_encontrado.velocidade}, Cor: {carro_encontrado.cor}, Ano: {carro_encontrado.ano}")
            else:
                print("Nenhum carro encontrado com esse código.")

        case '0': 
            print("SaInDo...")
            break

        case _:
            print("Numero digitado não está na sequência. Tente novamente, fi!!!!!!!!!")

