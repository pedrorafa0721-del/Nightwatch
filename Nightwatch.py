def introducao():
    print("\nJames Baxter, 33 anos, é um guarda florestal noturno da reserva da pinha vermelha.")
    print("Sua rotina é sempre quieta, mas em uma noite houve uma mudança abrupta:")
    print("um pedido desesperado de socorro ecoou no rádio — 'Socorro... acho que alguém está nos perseguindo!'")
    print("O pedido vem de 1 km de distância, perto das pedras amarelas. James sente que a floresta não é só árvores, algo a controla.\n")
    inicio()

def inicio():
    print("1. Início")
    print("James chega ao local do pedido de socorro, nenhum vestígio, nada além de silêncio absoluto. Dois caminhos surgem à frente:")
    print("1) Atalho escuro e escorregadio")
    print("2) Trilha da colina, longa e com neblina")
    escolha = input("Escolha: ")
    if escolha == "1":
        atalho_escuro()
    else:
        trilha_colina()

def atalho_escuro():
    print("\n2. Atalho escuro")
    print("James escorrega e sente dor no tornozelo. O rádio chia com ruídos estranhos.")
    print("A escuridão parece se mover.\n")
    print("1) Continuar mesmo com dor")
    print("2) Se esconder e esperar")
    escolha = input("Escolha: ")
    if escolha == "1":
        persistindo_com_dor()
    else:
        abrigo_temporario()

def trilha_colina():
    print("\n3. Trilha da colina")
    print("A neblina cobre tudo, porém começa a se desfazer. James vê uma figura não humana andando em círculos.\n")
    print("1) Enfrentar a criatura")
    print("2) Ignorar e seguir pela trilha")
    escolha = input("Escolha: ")
    if escolha == "1":
        confronto_criatura()
    else:
        trilha_neblina()

def persistindo_com_dor():
    print("\n4. Persistindo com dor")
    print("O tornozelo dói, mas James continua. O rádio murmura palavras estranhas.\n")
    print("1) Avançar cuidadosamente")
    print("2) Procurar abrigo")
    escolha = input("Escolha: ")
    if escolha == "1":
        obstaculo_floresta()
    else:
        abrigo_temporario()

def abrigo_temporario():
    print("\n5. Abrigo temporário")
    print("James se esconde entre árvores. Sons e sombras lembram erros do passado.\n")
    print("1) Explorar a floresta")
    print("2) Permanecer escondido")
    escolha = input("Escolha: ")
    if escolha == "1":
        luzes_enganosas()
    else:
        observacao_silenciosa()

def confronto_criatura():
    print("\n6. Confronto com a criatura")
    print("A criatura contorce-se na neblina, sussurrando varias escolhas erradas que James fez no passado.\n")
    print("1) Encarar a criatura")
    print("2) Fugir para o abrigo")
    escolha = input("Escolha: ")
    if escolha == "1":
        visoes_criatura()
    else:
        abrigo_temporario()

def trilha_neblina():
    print("\n7. Trilha e neblina")
    print("James tenta ignorar a figura, mas a neblina revela sombras de falhas antigas.\n")
    print("1) Continuar")
    print("2) Voltar e enfrentar a criatura")
    escolha = input("Escolha: ")
    if escolha == "1":
        obstaculo_floresta()
    else:
        confronto_criatura()

def obstaculo_floresta():
    print("\n8. Obstáculo da floresta")
    print("O caminho se divide: pedras escorregadias ou raízes que se movem.\n")
    print("1) Seguir pelas pedras")
    print("2) Seguir pelas raízes")
    escolha = input("Escolha: ")
    if escolha == "1":
        passagem_traiçoeira()
    else:
        raizes_sombras()

def luzes_enganosas():
    print("\n9. Luzes enganosas")
    print("Pequenas luzes flutuam revelando atalhos misteriosos, elas ficam paradas como se estivessem a espera de James.\n")
    print("1) Seguir as luzes")
    print("2) Ignorar e continuar")
    escolha = input("Escolha: ")
    if escolha == "1":
        caminho_iluminado()
    else:
        passagem_traiçoeira()

def observacao_silenciosa():
    print("\n10. Observação silenciosa")
    print("James observa em silêncio. Sons distantes ecoam, mas nada acontece.\n")
    print("1) Ir até os sons")
    print("2) Continuar esperando")
    escolha = input("Escolha: ")
    if escolha == "1":
        passagem_traiçoeira()
    else:
        persistencia_espera()

def visoes_criatura():
    print("\n11. Visões da criatura")
    print("A criatura projeta visões do passado: erros e medos.\n")
    print("1) Encarar a verdade")
    print("2) Fugir")
    escolha = input("Escolha: ")
    if escolha == "1":
        encarando_verdade()
    else:
        fuga_ilusoria()

def passagem_traiçoeira():
    print("\n12. Passagem traiçoeira")
    print("James encontra uma ponte antiga e perigosa.\n")
    print("1) Avançar cautelosamente")
    print("2) Correr apressado")
    escolha = input("Escolha: ")
    if escolha == "1":
        encarando_verdade()
    else:
        fuga_ilusoria()

def raizes_sombras():
    print("\n13. Raízes e sombras")
    print("As raízes se movem como se tivessem vida.\n")
    print("1) Enfrentar")
    print("2) Retroceder")
    escolha = input("Escolha: ")
    if escolha == "1":
        encarando_verdade()
    else:
        abrigo_temporario()

def caminho_iluminado():
    print("\n14. Caminho iluminado")
    print("As luzes levam James a uma clareira misteriosa.\n")
    print("1) Explorar a clareira")
    print("2) Retornar ao caminho anterior")
    escolha = input("Escolha: ")
    if escolha == "1":
        clareira_misteriosa()
    else:
        passagem_traiçoeira()

def persistencia_espera():
    print("\n15. Persistência da espera")
    print("Nada acontece. O rádio chia, ecoando lembranças antigas.\n")
    print("1) Avançar sozinho")
    print("2) Continuar esperando")
    escolha = input("Escolha: ")
    if escolha == "1":
        passagem_traiçoeira()
    else:
        observacao_silenciosa()

def encarando_verdade():
    print("\n16. Encarando a verdade")
    print("James percebe que a floresta reflete sua mente e culpa.\n")
    print("1) Aceitar o ciclo")
    print("2) Tentar quebrar o ciclo")
    escolha = input("Escolha: ")
    if escolha == "1":
        final1()
    else:
        final2()

def fuga_ilusoria():
    print("\n17. Fuga ilusória")
    print("James tenta escapar, mas cada caminho o leva de volta às memórias.\n")
    print("1) Aceitar a situação")
    print("2) Persistir tentando fugir")
    escolha = input("Escolha: ")
    if escolha == "1":
        final1()
    else:
        final2()

def clareira_misteriosa():
    print("\n18. Clareira misteriosa")
    print("Símbolos estranhos gravados no chão parecem falar de redenção.\n")
    print("1) Investigar os símbolos")
    print("2) Ignorar e seguir")
    escolha = input("Escolha: ")
    if escolha == "1":
        redenção_parcial()
    else:
        encarando_verdade()

def redenção_parcial():
    print("\n21. Descoberta de redenção parcial")
    print("Os símbolos mostram um caminho que pode quebrar o ciclo.\n")
    print("1) Seguir o caminho da redenção")
    print("2) Ignorar e seguir sozinho")
    escolha = input("Escolha: ")
    if escolha == "1":
        final3()
    else:
        final2()

# Finais
def final1():
    print("\nFINAL 1 – Loop da Culpa")
    print("James está preso em um ciclo eterno, revivendo erros infinitamente.")
    exit()

def final2():
    print("\nFINAL 2 – Descoberta da Verdade")
    print("James descobre que tudo era projeção de sua própria culpa. Ele nunca escapa.")
    exit()

def final3():
    print("\nFINAL 3 – Redenção parcial")
    print("James consegue enfrentar parte de sua culpa e caminha em direção à luz.")
    exit()

# Início do jogo
introducao()
