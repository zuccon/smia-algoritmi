# Homework 1: Insertion Sort

def insertion_sort_zucconico(lista=[],n=None):
    """
    - usa una return list vuota, non modifica quella originale.
    - ogni iterazione aggiunge un elemento della lista di input 
      all'indice giusto dell'array da ritornare.
    
    lista: lista da sortare
    n: indice fino al quale sortare, oppure sorta tutta la lista
    """
    if len(lista) == 0:
        return []
    ret_list = [lista[0]]
    
    # senza N lo sortiamo tutto
    if n==None:
        n=len(lista)
    # gestiamo altri N sbagliati
    if n>len(lista) or n<0:
        n=len(lista)

    # scorro tutto l'input
    for i in range(1,n):
        valore_attuale = lista[i]
        # scorro la lista da ritornare per capire a che indice mettere il valore
        for ret_i,val in enumerate(ret_list):
            if valore_attuale <= val:
                break
        else:
            ret_i=ret_i+1
        # inserisco il valore all'indice corretto
        ret_list.insert(ret_i,valore_attuale)
    # popola il resto di ret_list coi valori originali se non era tutta da sortare
    if n != len(lista):
        ret_list+=lista[len(ret_list):]
    return ret_list

def main(lista=[]):
    return insertion_sort_zucconico(lista)

# print(main([]),main([7,3,3,3,5,7,2,3,4,2,5,78,36,6,0]),main([7,6,5,4,3,2,1]),main([1,2,3,4,5,6,7]))
