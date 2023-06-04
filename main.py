from entities import Vendedor, Cliente, Compra
from datetime import datetime
from time import sleep

print('=-' * 30)
print('Programado por JulianoMarthins')
print('=-' * 30)

nome = input('Digite o nome do cliente: ')
idade = int(input('Qual a idade do cliente: '))
vendedor = input('Digite o nome do vendedor: ')
idadeVen = int(input('Digite a idade do vendedor: '))
valor = float(input('Valor da compra: '))
sleep(1)

print('=-' * 30)

cliente = Cliente(nome=nome, idade=idade)
vendedor = Vendedor(nome=vendedor, idade=idadeVen, salario=3200)

compra1 = Compra(cliente, datetime.now(), valor=valor)
compra2 = Compra(cliente, datetime(year=2018, month=6, day=4), valor=256)

cliente.registroCompra(compra1)
cliente.registroCompra(compra2)

print(f'Cliente: {cliente}', '(adulto)' if cliente.isAdulto() else '')
print(f'Vendedor: {vendedor}')

valorTotal = cliente.totalCompras()
quanCompra = len(cliente.compras)

print(f'Total: R${valorTotal:.2f} em {quanCompra} compras')
print(f'Última compra: {cliente.getUltimaCompra()}')

print('=-' * 30)
