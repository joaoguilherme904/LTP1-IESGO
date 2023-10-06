itens_menu = {"hamburger": 12.50, "batata frita": 8.50, "refrigerante": 5.00}
pedidos = {}

def adicionar_pedido(numero_pedido, itens):
    pedidos[numero_pedido] = itens

def adicionar_item_pedido(numero_pedido, item, quantidade):
    if numero_pedido in pedidos:
        if item in itens_menu:
            pedidos[numero_pedido][item] = quantidade
        else:
            print("Este item não está no menu.")
    else:
        print("Pedido não encontrado.")

def calcular_total(numero_pedido):
    total = 0
    for item, quantidade in pedidos[numero_pedido].items():
        total += itens_menu[item] * quantidade
    return total

adicionar_pedido(1, {"hamburger": 3})
adicionar_item_pedido(1, "batata frita", 2)
adicionar_item_pedido(1, "refrigerante", 2)
print(calcular_total(1))
