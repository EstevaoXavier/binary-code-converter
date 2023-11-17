
def conversor(codigo):
    letras = {'01000001':'A', '01000010':'B'}
    for chave, valor in letras.items():
        if chave == codigo:
            return valor