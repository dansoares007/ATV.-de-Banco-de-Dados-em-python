from dataclasses import dataclass
import json
import os

class Carro :
    codigo:int
    placa: str
    velocidade: int
    cor: str
    
carros = []
def salvar():
    with open("carro.txt", "w") as f:
        json.dump([c.__dict__ for c in carros], f, indent=4)

def inserir(carro):
    carros.append(carro)
    salvar()

def atualizar(codigo, novo_placa=None, novo_velocidade=None, novo_cor=None):
    for c in carros:
        if c.codigo == codigo:
            if novo_placa: c.marca = novo_placa
            if novo_cor: c.cor
            if novo_velocidade is not None: c.velocidade = novo_velocidade
            salvar()
            return
    print("Carro não encontrado.")
    
def deletar(codigo):
    global carros
    carros = [c for c in carros if c.carros if c.codigo != codigo]
    salvar()
    
def consulta(codigo):
    for c in carros:
        if c.codigo == codigo:
            return c
    return None

def mostrar_todos():
    return carros

def consultar_marca(placa):
    return[c for c in carros if placa.lower() in c.placa.lower()]

def carregar ():
    global carros
    if os.path.exists("carro.txt"):
        with open("carro.txt", "r") as f:
            dados = json.load(f)
            carros = [Carro(**d) for d in dados]
            
