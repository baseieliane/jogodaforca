PALAVRAS_POR_TAMANHO = [
    ["sol", "mar", "rio", "luz", "sal", "mel", "paz", "lar"],
    ["casa", "bola", "gato", "rato", "leve", "doce", "azul", "vida"],
    ["carro", "amiga", "praia", "sonho", "pedra", "carta", "verde", "chuva"],
    ["escola", "brasil", "janela", "leitor", "animal", "planeta", "nuvens", "amigos"],
    ["laranja", "foguete", "palavra", "estudar", "destino", "passeio", "cerejas", "montado"],
    ["banheiro", "computar", "montanha", "elefante", "planetas", "amizades", "estrelas", "cadernos"]
]


def sorteia_palavra():
    quantidadeDeLetras = int(input("Escolha a quantidade de letras que deseja: "))

    if quantidadeDeLetras == 3:
        import random
        linha_selecionada = PALAVRAS_POR_TAMANHO[0]
        palavra_sorteada = random.choice(linha_selecionada)
    
    elif quantidadeDeLetras == 4:
        import random
        linha_selecionada = PALAVRAS_POR_TAMANHO[1]
        palavra_sorteada = random.choice(linha_selecionada)
    
    elif quantidadeDeLetras == 5:
        import random
        linha_selecionada = PALAVRAS_POR_TAMANHO[2]
        palavra_sorteada = random.choice(linha_selecionada)
    
    elif quantidadeDeLetras == 6:
        import random
        linha_selecionada = PALAVRAS_POR_TAMANHO[3]
        palavra_sorteada = random.choice(linha_selecionada)

    elif quantidadeDeLetras == 7:
        import random
        linha_selecionada = PALAVRAS_POR_TAMANHO[4]
        palavra_sorteada = random.choice(linha_selecionada)
    
    elif quantidadeDeLetras == 8:
        import random
        linha_selecionada = PALAVRAS_POR_TAMANHO[5]
        palavra_sorteada = random.choice(linha_selecionada)
    
    else:
        print("OpÃ§Ã£o invÃ¡lida")
    
    return(palavra_sorteada)


palavra_forca = sorteia_palavra()


def criar_mascara():
    letras_ocultas = ["_"] * len(palavra_forca)
    return letras_ocultas
    
letras_ocultas = criar_mascara()
letras_tentadas = []
def advinhar_palavra():
    sair = 0
    tentativas = 6
    
    while sair == 0:
        print("O jogo comeÃ§ou!")
        print(f"Palavra: {letras_ocultas}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras tentadas: {letras_tentadas}")
        letra_escolhida = input("Digite uma letra: ")
        letras_tentadas.append(letra_escolhida)
        
       
        if letra_escolhida in palavra_forca:
            
            for i in range(len(palavra_forca)):
                if  palavra_forca[i] == letra_escolhida:
                        letras_ocultas[i] = letra_escolhida
                        break
        else:
            tentativas = tentativas -1
            if tentativas == 0:
                print("VocÃª perdeu!")
                sair = 1
     
        if not "_" in letras_ocultas:
            print(f"ParabÃ©ns! VocÃª acertou! A palavra era : {palavra_forca} ")
            sair = 1
    
    
advinhar_palavra()