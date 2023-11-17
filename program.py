from converter_letter import conversor
import os


def verificador(codigos):
    nova_variavel = ''
    for caractere in codigos:
        if caractere == ' ':
            pass
        else:
            nova_variavel += caractere
    # print(nova_variavel, len(nova_variavel))
    codigos_len = len(nova_variavel)
    if codigos_len % 8 == 0:
        print('A Quantidade de caracteres está certa!')
        # nova_variavel = int(nova_variavel)
        return nova_variavel
    else:
        print('ERROR: O código binario que você enviou não é multiplo de 8')
        return False

def separador():
    pass

def conversor_um_por_um(*codigos):
    for codigo in codigos:
        codigo = conversor('codigo')

print(' ')
user_input = input('insira seu codigo binario -')
codigo_verificado = verificador(user_input)
print(' ')
if codigo_verificado == False:
    os.system('cls')
    exit()
codigo_verificado_len = len(codigo_verificado)
if len(codigo_verificado) > 8:
    separador(codigo_verificado)
