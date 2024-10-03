import os

def info():
    print(" projeto megaman x4 \n esse projeto tem como objetivo dar informaçoes de megaman x4\n")
    nome = input("primeiramente antes de começar digite seu nome: ")
    print("escolha uma das tres opçoes de informaçoes para ver \na opçao 1 conta a historia \na opçao 2 da informaçoes dos chefe \na opçao 3 mostra todos os itens do jogo")
    opcao = input("escolha uma das tres opçoes [1] - historia [2] - chefes - [3] itens: ")


    while True:
        if opcao == "1":
            print("HISTORIA DE MEGAMAN X4\n No ano 21XX, dois grandes exércitos Reploids existem para combater os Mavericks: Os Maverick Hunters e a Repliforce.\n As duas organizações colaboraram em várias ocasiões, e durante este tempo, Zero fez amizade com Colonel e Iris (irmã mais nova de Colonel) \n Em um dia, a cidade flutuante Sky Lagoon foi atacada por Mavericks, que sabotaram seu gerador de energia, fazendo-a cair sobre a cidade abaixo, matando milhares de pessoas. \n Como a Repliforce estava presente na área, os Maverick Hunters acabaram desconfiando de uma possível aliança da Repliforce com seus inimigos, os Mavericks, algo que acaba se concretizando.\n Durante suas investigações na área da tragédia, X e Zero encontram Colonel e o interrogam, por sua vez ele nega as acusações desse possível ataque dizendo que só estava presente na área para salvar sua irmã.\n Logo após o incidente e as acusações, General realiza um pronunciamento alegando que a Repliforce prega a paz e união entre humanos e Reploids e jamais se aliaria aos inimigos,\n algo que é dado como mentira pelos Mavericks Hunters e dias depois a Repliforce declara-se aliada aos Mavericks e uma gigantesca guerra tem início entre os Mavericks Hunters e os Mavericks unidos com a Repliforce que gera inúmeras \nreviravoltas e a descoberta do retorno e envolvimento de Sigma novamente")
            print("\n")
            entrada = input("vc quer continuar o programa? digite [s] para voltar ou [n] para encerrar: ")
            if entrada == "s":
              print("voltando...")
              info()
            elif entrada  == "n":
                print("fim do programa")
                break
            



        elif opcao == "2":
            print("informaçoes dos chefes qual chefe vc quer saber sobre?: ") 
            entrada =  input("1 - Magma Dragoon, 2 - Frost Walrus, 3 - Jet Stingray, 4 - Slash Beast, 5 - Web Spider, 6 - Split Mushroom, 7 - Cyber Peacock, 8 - Storm Owl, 9 é para sair, 10 é para voltar: ")  
            print("\n")                                     
            if entrada == "1":
                print(" NOME - Magma Dragoon\n ESTAGIO - Volcano \n Antigo membro da 14ª Unidade de Combate Garra, ele traiu os Maverick Hunters, tornando-se um Maverick, tudo por uma chance de duelar com X e Zero.\n ataque/tecnica - Rising Fire / Ryuenjin \n fraqueza - Double Cyclone / Raijingeki")
                print("\n")
            elif entrada == "2":
                print(" NOME - Frost Walrus\n ESTAGIO - Snow Base \n De temperamento ruim e turbulento, seu comportamento destrutivo foi o que marcou para sua classificação como um Maverick, mas ele evitou isto juntando-se a Repliforce. Quando o golpe começou, ele ficou satisfeito.\n Para ele, era uma desculpa perfeita para o motim, tanto quanto ele gostava. Walrus foi mandado para a base secreta de neve da Repliforce e foi encarregado de guardar a nova arma em construção.\n ataque/tecnica - Frost Tower / Hyouretsuzan \n fraqueza - Rising Fire / Ryuenjin ")
                print("\n")
            elif entrada == "3":
                print(" NOME - Jet Stingray \n ESTAGIO - Marine Base \n Dedicado à sua carreira militar, ele trilhou seu caminho para subir na hierarquia e conseguiu uma grande patente na marinha da Repliforce.\n Ele tinha grande respeito por General e Colonel, então, quando General anunciou seu golpe para a independência Reploid,\n não havia nenhuma dúvida para onde sua lealdade o levaria. Quando o golpe começou, como diversão, ele atacou uma estação de energia subterrânea de uma cidade criando o caos para atrair os Maverick Hunters.\n ataque/tecnica - Ground Hunter / Hienkyaku \n fraqueza - Frost Tower / Hyouretsuzan")
                print("\n")
            elif entrada == "4":
                print(" NOME - Slash Beast \n ESTAGIO - Military Train \n Alistou-se na Repliforce apenas para exercitar livremente suas habilidades de combate, mas apesar desta atitude ele mostrou grande coragem em batalha, não temendo ninguém.\n Durante o golpe, Slash Beast foi encarregado de guardar um trem de suprimentos militar da Repliforce. \n ataque/tecnica - Twin Slasher / Shippuga \n fraqueza - Ground Hunter / Raijingeki")
                print("\n")
            elif entrada == "5":
                print(" NOME - Web Spider \n ESTAGIO - Jungle \n Antes de sua carreira militar com a Repliforce, ele era um Maverick Hunter, pertencente à Unidade Especial 0.\n Quando a Repliforce começou sua guerra de independência, foi mandado para base da selva e ficou encarregado de guardar um poderoso canhão de raios ali escondido. \n ataque/tecnica - Lightning Web / Raijingeki \n fraqueza - Twin Slasher / Z-saber")
                print("\n")
            elif entrada == "6":
                print(" NOME - Split Mushroom \n ESTAGIO - Bio Laboratory \n Ele já foi encarregado das operações em um Bio-Laboratório, mas quando o laboratório foi desativado ele foi descartado.\n Mushroom foi posteriormente reativado por alguém (supostamente Sigma) e se tornou um Maverick. \n Ele reativou as operações do Bio-Laboratório, fortificou-o, atacando qualquer invasor para se divertir e agir como uma distração para chamar a atenção dos Maverick Hunters.\n Ele, aparentemente, recebeu ordens de desafiar e testar as habilidades de X e Zero. \n ataque/tecnica - Soul Body / Kuuenbu \n fraqueza - Lightning Web / Raijingeki")
                print("\n")
            elif entrada == "7":
                print(" NOME - Cyber Peacock \n ESTAGIO - Cyberspace \n Ele era originalmente uma IA que protegia a rede de hackers antes de ser corrompido por Sigma.\n Ele então começa a corromper a rede e a si mesmo para chamar a atenção dos Maverick Hunters, pois como Split Mushroom,\n foi dada a ele a tarefa de testar as habilidades de X e Zero, através de uma série de testes e exercícios de treinamento. \n ataque/tecnica - Aiming Laser / Rakuhouha \n fraqueza - Soul Body / Ryuenjin")
                print("\n")
            elif entrada == "8":
                print(" NOME - Storm Owl \n ESTAGIO - Air Forces \n Um dos generais mais engenhosos da Repliforce, Storm Owl considerava toda a equipe como uma família.\n Ele ficou extremamente ressentido quando ele e seus colegas foram taxados como Mavericks pelos caçadores.\n Após o golpe da Repliforce começar, ele lançou uma brigada aérea para desviar a atenção dos Maverick Hunters. \n ataque/tecnica - Double Cyclone / Tenkuuha \n fraqueza - Aiming Laser / Rakuhouha")
                print("\n")
            elif entrada == "9":
                print("fim do programa")
                break
            elif entrada == "10": 
                print("voltando...")
                info()
                break
            else:
                print("digitou errado tente de novo")

        elif opcao == "3":
            print("AQUI TEM ESTAO AS INFORMAÇOES DE TODOS OS ITENS DO JOGO")
            entrada = input("escola o tipo de iten que deseja obter irformaçao \n [1] tanks [2] armadura  [3] veiculos [4] sair [5] para voltar: ")
            if entrada == "1":
                print(" E-Tank ou Sub-Tank \n Guardam energia extra para quando for preciso.\n São dois ao todo. Usam 16 cápsulas de qualquer tamanho para encher completamente cada tanque. \n Ao contrário dos outros jogos, você não precisa necessariamente estar com a energia total para enchê-los, o que é bem mais cômodo.\n")
                print(" W-Tank Reenche a energia de todas as suas armas, e deve ser enchida com cápsulas que recarregam as armas dos chefes.")
                print(" Heart-Tank Dão ao seu personagem mais energia, daí ele pode suportar mais dano. São 8 ao todo, um em cada fase.")
                print(" 1-Up e o EX-Tank Esses itens em forma de capacete dão uma vida extra ao jogador. O EX-Tank aumenta o número normal de vidas de 3 para 5.\n")

            elif entrada == "2":
                print(" ARMADURA-Fourth ou Nova Armor\n")
                print(" BRAÇOS Encontrados na fase do Storm Owl, vêm em dois tipos: Stock Charge (faz os braços do X terem uma coloração azul e cinza claro que essa coloração combina com o resto da armadura) e Plasma Charge (que faz os braços do X terem uma coloração vermelho e preto que não combina com o resto da armadura).\n Stock Charge: Permite a você guardar até quatro tiros carregados e atirá-los continuamente.\n Plasma Charge: Permite lançar uma destrutiva esfera de energia que causa danos até nos mais fortes inimigos, e também deixa rastros de plasma que causam danos adicionais por um bom tempo.\n Plasma Charge é o preferido entre os jogadores. Ambas permitem a ele carregar as armas. ")
                
                print(" CABEÇA Encontrado na fase do Cyber Peacock, no 3º teste da Area 1, é necessário conseguir Rank S para, como prêmio, a cápsula aparecer; a cabeça permite que você não gaste as armas (não-carregadas), somente quando carregadas elas gastam energia. ")
                
                print(" CORPO Encontrado na fase do Magma Dragoon, esta armadura reduz os danos enquanto constrói energia para o ataque Nova Strike (às vezes referido como Giga Attack), que é recarregado enquanto X é danificado. ")
                
                print(" PERNAS Encontradas na fase do Web Spider (logo no começo da Area 1, encontre uma escada e desça conforme o caminho padrão e vá para a direita que você encontra a cápsula), as pernas permitem-o executar duas funções:\n Air Dash: X pode executar o dash em pleno ar.\n Útil para alcançar lugares altos ou para escapadas rápidas. \n Flutuação: Pressionando o botão de pulo enquanto no ar, X flutuará. Sem mover-se, a flutuação manterá-se por 5 segundos. \n Você pode mover-se para frente ou para trás, mas com isso, o movimento só durará 2 segundos.\n Às vezes, é útil para desviar-se de tiros adversários. ")
                print("\n")
                print("ULTIMATE ARMOR A Ultimate Armor é uma armadura secreta que só pode ser utilizada ao digitar um código secreto na tela de seleção de personagem.\n Ela tem todas as características presentes na Fourth Armor, apenas com duas diferenças: o Nova Strike da Ultimate Armor é infinito e não há nenhum aumento de defesa nessa armadura.\n Para o PlayStation, o código é: círculo (2x), esquerda (6x) segurar L1 e R2 e pressionar Start com Mega Man X selecionado.\n Para o Saturn, o código é: B, B, esquerda (6x), segurar L e R e pressionar Start com Mega Man X selecionado.\n Na versão para PC, simplesmente pressione Seta para baixo e Enter ao mesmo tempo.\n Se X aparecer na fase inicial com as partes azul claro de sua armadura roxas, o código funcionou.\n Depois disso, pegue qualquer upgrade de armadura em uma das cápsulas para ativar a Ultimate Armor.")

            elif entrada == "3":
                print(" VEICULOS \n")
                print(" EAGLE ARMOR-Encontrada na fase de Storm Owl, esta armadura azul pode flutuar infinitamente, mas toda vez que é atingida, sua altitude cai.\n Tem mísseis e um canhão que dispara poderosos tiros teleguiados quando carregada e pode dar air-dashes ")     
                print(" RAIDEN ARMOR-Encontrada nas fases do Slash Beast e do Magma Dragoon, esta armadura vermelha foi designada para combate mano a mano,\n que pode também destruir rochas ou mesmo carros-trem. É também à prova de lava, o que permite levá-lo direto à luta contra o Dragoon. ")
                print(" JET BIKE-Encontrada na fase do Jet Stingray, esta moto alcança altas velocidades além de atirar em inimigos.\n Pode também dar poderosos air-dashes que destroem os inimigos quando eles batem na frente da moto no seu período de execução")
            elif entrada == "4":
                print("fim do programa")
                break
            elif entrada == "5":
                print("voltando...")
                info()
                break
            else:
                print("digitou errado tente novamente")
        else:
            print("essa opçao não existe tente de novo")
            info()
            break
info()