import os


def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
        for chave, valor in kwargs.items():
            f.write(f"{chave}: {valor}\n")

# Carregar variáveis de um arquivo
def carregar_variaveis(path_file):
    variaveis = {}
    with open(path_file, 'r') as f:
        for line in f:
            chave, valor = line.strip().split(': ')
            variaveis[chave] = valor
    return variaveis

def verifica_primeira_vez():
    match os.path.exists("variaveis.txt"):

        case True:
            variaveis_carregadas = carregar_variaveis('variaveis.txt')

            if len(variaveis_carregadas) > 0:
                print(f"seja bem vindo novamente {variaveis_carregadas["nome"]}")
            else:
                nome_v =  input("por favor digite seu nome: ")

                salvar_variaveis('variaveis.txt',nome = nome_v )
        case False:
                nome_v =  input("por favor digite seu nome: ")

                salvar_variaveis('variaveis.txt',nome = nome_v )
   

def info():
    print("projeto megaman x4\nEsse projeto tem como objetivo dar informações sobre o jogo Megaman X4\n")

    verifica_primeira_vez()

    print("Escolha uma das três opções de informações para ver:")
    print(" 1 - História 2 - chefes 3 - itens")
    
    opcao = input("Escolha uma opção: ")
    while True:
        match opcao:
            case "1":
                print("HISTÓRIA DE MEGAMAN X4\nNo ano 21XX, dois grandes exércitos Reploids existem para combater os Mavericks: os Maverick Hunters e a Repliforce.\nAs duas organizações colaboraram em várias ocasiões. Zero fez amizade com Colonel e Iris, irmã de Colonel. A cidade flutuante Sky Lagoon foi atacada por Mavericks, resultando em uma catástrofe e suspeitas sobre a Repliforce.\nA Repliforce então se declara aliada aos Mavericks, dando início a uma grande guerra entre os Mavericks Hunters e a Repliforce, com o retorno de Sigma ao cenário.")
                print("\n")
                entrada = input("Você quer continuar o programa? Digite [s] para voltar ou [n] para encerrar: ")
                match entrada:
                    case "s":
                        print("Voltando...")
                        info()
                    case "n":
                        print("Fim do programa")
                        break
            case "2":
                chefes_info()

            case "3":
                itens_info()

            case _:
                print("Essa opção não existe, tente de novo.")
                info()
                break

def chefes_info():
    print("Informações dos chefes. Qual chefe você quer saber sobre?")
    entrada = input("1 - Magma Dragoon, 2 - Frost Walrus, 3 - Jet Stingray, 4 - Slash Beast, 5 - Web Spider, 6 - Split Mushroom, 7 - Cyber Peacock, 8 - Storm Owl, 9 é para sair, 10 é para voltar: ")
    print("\n")
    
    match entrada:
        case "1":
            print("NOME - Magma Dragoon\nESTÁGIO - Volcano\nAntigo membro da 14ª Unidade de Combate Garra, ele traiu os Maverick Hunters, tornando-se um Maverick, tudo por uma chance de duelar com X e Zero.\nAtaque/Técnica - Rising Fire / Ryuenjin\nFraqueza - Double Cyclone / Raijingeki")
        case "2":
            print("NOME - Frost Walrus\nESTÁGIO - Snow Base\nDe temperamento ruim e turbulento, seu comportamento destrutivo foi o que marcou sua classificação como Maverick.\nAtaque/Técnica - Frost Tower / Hyouretsuzan\nFraqueza - Rising Fire / Ryuenjin")
        case "3":
            print("NOME - Jet Stingray\nESTÁGIO - Marine Base\nDedicado à sua carreira militar, subiu na hierarquia da marinha da Repliforce. Atacou uma estação de energia para atrair os Maverick Hunters.\nAtaque/Técnica - Ground Hunter / Hienkyaku\nFraqueza - Frost Tower / Hyouretsuzan")
        case "4":
            print("NOME - Slash Beast\nESTÁGIO - Military Train\nAlistou-se na Repliforce para exercitar suas habilidades de combate. Durante o golpe, foi encarregado de guardar um trem de suprimentos militar.\nAtaque/Técnica - Twin Slasher / Shippuga\nFraqueza - Ground Hunter / Raijingeki")
        case "5":
            print("NOME - Web Spider\nESTÁGIO - Jungle\nAntes de sua carreira militar, era um Maverick Hunter. Foi mandado para a base da selva da Repliforce.\nAtaque/Técnica - Lightning Web / Raijingeki\nFraqueza - Twin Slasher / Z-saber")
        case "6":
            print("NOME - Split Mushroom\nESTÁGIO - Bio Laboratory\nReativado por Sigma, tornou-se um Maverick e reativou operações do Bio-Laboratório.\nAtaque/Técnica - Soul Body / Kuuenbu\nFraqueza - Lightning Web / Raijingeki")
        case "7":
            print("NOME - Cyber Peacock\nESTÁGIO - Cyberspace\nEra uma IA que protegia a rede antes de ser corrompido por Sigma.\nAtaque/Técnica - Aiming Laser / Rakuhouha\nFraqueza - Soul Body / Ryuenjin")
        case "8":
            print("NOME - Storm Owl\nESTÁGIO - Air Forces\nUm dos generais mais engenhosos da Repliforce, lançou uma brigada aérea para desviar a atenção dos Maverick Hunters.\nAtaque/Técnica - Double Cyclone / Tenkuuha\nFraqueza - Aiming Laser / Rakuhouha")
        case "9":
            print("Fim do programa")
        case "10":
            print("Voltando...")
            info()
        case _:
            print("Digitou errado, tente de novo")
    print("\n")
    
def itens_info():
    print("AQUI ESTÃO AS INFORMAÇÕES DE TODOS OS ITENS DO JOGO")
    entrada = input("Escolha o tipo de item que deseja obter informação\n[1] Tanks\n[2] Armaduras\n[3] Veículos\n[4] Sair\n[5] Voltar: ")

    match entrada:
        case "1":
            print("E-Tank ou Sub-Tank: Guardam energia extra para quando for preciso.\nSão dois ao todo. Usam 16 cápsulas de qualquer tamanho para encher completamente cada tanque.\nW-Tank: Reenche a energia de todas as suas armas. Heart-Tank: Aumenta sua energia máxima.")
            print("1-Up e o EX-Tank: Esses itens dão uma vida extra ao jogador. O EX-Tank aumenta o número de vidas de 3 para 5.\n")
        case "2":
            print("ARMADURA - Fourth ou Nova Armor\n")
            print("BRAÇOS: Encontrados na fase do Storm Owl. Dois tipos: Stock Charge e Plasma Charge.\n")
            print("CABEÇA: Encontrada na fase do Cyber Peacock. Permite que você não gaste armas não carregadas.\n")
            print("CORPO: Reduz os danos e acumula energia para o ataque Nova Strike.\n")
            print("PERNAS: Encontradas na fase do Web Spider. Permitem dash aéreo e flutuação temporária.\n")
            print("ULTIMATE ARMOR: Armadura secreta com Nova Strike infinito. Pode ser desbloqueada com código secreto.\n")
        case "3":
            print("VEÍCULOS\n")
            print("EAGLE ARMOR: Encontrada na fase de Storm Owl. Armadura azul com mísseis e capacidade de flutuar.\n")
            print("RAIDEN ARMOR: Encontrada nas fases de Slash Beast e Magma Dragoon. Armadura vermelha para combate mano a mano.\n")
            print("JET BIKE: Encontrada na fase do Jet Stingray. Moto veloz com dashes aéreos que destroem inimigos.\n")
        case "4":
            print("Fim do programa")
        case "5":
            print("Voltando...")
            info()
        case _:
            print("Digitou errado, tente novamente")
    print("\n")
    
info()