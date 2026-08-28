import random
energia_inicial = 100
total_itens = 5
passos_minimos = 1
passos_maximos = 20
chance_de_achar_item = 30
def pedir_passos():
    entrada = input(f"digite a quantidade de passos que deseja andar ({passos_minimos}-{passos_maximos}): ")
    try:
        return int(entrada)
    except ValueError:
        print("isso nao e um numero valido tente novamente")
        return None
def main():
    energia = energia_inicial
    itens_coletados = 0
    passos_totais = 0
    print(f"voce esta na caverna da pit e precisa coletar {total_itens} itens para escapar")
    print(f"voce comeca com {energia} de energia. cada passo que voce anda consome energia")
    while energia > 0 and itens_coletados < total_itens:
        passos = pedir_passos()
        if passos is None:
            continue
        if passos < passos_minimos:
            print("voce nao pode ficar sem andar ou voltar")
            continue
        if passos > passos_maximos:
            print("voce nao enxerga longe o suficiente para caminhar")
            continue
        energia -= passos
        passos_totais += passos
        print(f"voce gastou {passos} de energia e agora tem {energia} de energia")
        if random.randint(0, 100) <= chance_de_achar_item:
            itens_coletados += 1
            print(f"voce encontrou um item. itens coletados: {itens_coletados} de {total_itens}")
        else:
            print("voce nao encontrou itens desta vez")
    print("\n--- fim de jogo ---")
    print(f"passos totais andados: {passos_totais}")
    print(f"itens coletados: {itens_coletados} de {total_itens}")
    if energia <= 0:
        print("voce morreu de fome")
    elif itens_coletados == total_itens:
        print("parabens voce encontrou todos os itens e saiu da caverna")
if __name__ == "__main__":
    main()