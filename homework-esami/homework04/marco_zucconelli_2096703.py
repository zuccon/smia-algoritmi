# Homework 04: coin change due la vendetta
    
def vendetta_vera(coins=[],target=0):
    """ ritorna il numero di combinazioni di una o piu' coins la cui somma raggiunge target """
    # niente da fare
    if not coins:
        return 0
    # somma troppo alta
    if target < 0:
        return 0
    # somma esatta
    if target == 0:
        return 1
    # ricorri a forma di albero binario, da un lato togli l'elemento di coins usato nell'altro
    return vendetta_vera(target=target-coins[0], coins=coins) \
         + vendetta_vera(target=target,          coins=coins[1:])

def coin_change_due(coins=[],target=0):
    """ wrappa la chiamata ricorsiva, utile solo per gestire il caso limite target=0 nella prima chiamata """
    if target == 0:
        return 0
    return vendetta_vera(coins=coins,target=target)

def main(coins=[],target=0):
    return coin_change_due(coins=coins,target=target)
