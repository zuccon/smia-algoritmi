# Homework 02: Isomorphic Strings

import random
def gen_isomorphic_strings(str_1_len=10,str_2_len=10):
    """
    genera stringhe isomorfe
    """
    alphabet=[ chr(i) for i in range(ord("a"),ord("a")+26) ]
    alphabet_shuffled = alphabet.copy()
    random.shuffle(alphabet_shuffled)
    # generate match map
    matches=dict(zip(alphabet,alphabet_shuffled))
    ret_1=[]
    ret_2=[]
    
    if str_1_len >= str_2_len:
        longer = str_1_len
    else:
        longer = str_2_len
        
    for i in range(longer):
        c=random.choice(alphabet)
        ret_1.append(c)
        ret_2.append(matches[c])

    return "".join(ret_1[0:str_1_len]), "".join(ret_2[0:str_2_len])

def isomorphic_strings(str_1="",str_2=""):
    """
    ritorna True se le due stringhe sono isomorfe, False altrimenti.

    se le stringhe sono di lunghezza diversa, 
      verifica che la sottostringa della stringa piu' lunga, 
      lunga quanto quella piu' corta, 
      sia isomorfa con la stringa piu' corta.
      
    due stringhe vuote rispettano la definizione di isomorfismo,
      quindi seguendo il modo in cui gestiamo stringhe di lunghezza diversa,
      una stringa vuota e' sempre isomorfa con una stringa non vuota.
    """
    # non serve validare input, casi limite gia' gestiti.
    
    # init match map dict
    matches={}

    # scegliamo stringa piu' corta, sulla quale basare il loop.
    if len(str_1) <= len(str_2):
        # lower() qui usera' piu' memoria. aggiungere un nome a una variabile no, sara' solo un puntatore in piu'.
        # lower() nel loop verra' chiamato a ogni iterazione e rallentera' il processing.
        shorter_str = str_1.lower()
        longer_str = str_2.lower()
    else:
        shorter_str = str_2.lower()
        longer_str = str_1.lower()

    # iteriamo sulla stringa corta
    for i,c in enumerate(shorter_str):
        # carattere gia' mappato
        if c in matches.keys():
            # mappatura non rispettata
            if matches[c] != longer_str[i]:
                return False
        # carattere non mappato
        else:
            # valore presente sotto un'altra chiave
            if longer_str[i] in matches.values():
                return False
            else:
                matches[c] = longer_str[i]
    # loop completato
    else:
        return True

def main(str_1="",str_2=""):
    return isomorphic_strings(str_1,str_2)
