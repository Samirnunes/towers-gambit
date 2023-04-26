# TOWER'S GAMBIT

Jogo feito como projeto do 1º bimestre da disciplina de CSI-22 (Programação Orientada a Objetos) no ITA.

<p align="center">
    <img width="600" src="https://github.com/Samirnunes/towers_gambit_project_CSI-22/blob/main/readme_images/gameplay.png" alt="Material Bread logo">
<p>

## Grupo e Contato

Gabriel Telles Missailidis - Desenvolvimento e Arte - https://www.linkedin.com/in/gabriel-telles/

João Lucas Rocha Rolim - Desenvolvimento e Game Design - https://www.linkedin.com/in/jo%C3%A3o-lucas-rocha-rolim/

Samir Nunes da Silva - Desenvolvimento e Game Design - https://www.linkedin.com/in/samir-nunes-da-silva/

## Apresentação no Google Slides

**Link**: https://docs.google.com/presentation/d/1_lHMNBS4p0gH9NPpQOGCS_4QjJc6JuBFFhQONNVSnN8/edit?usp=sharing

## Características Principais
    
- **Linguagem de Programação**: Python.
   
- **Biblioteca Principal**: Pygame.

- **Formato**: Tower Defense.
 
- **Temática**: Xadrez/Cartas de Baralho.

- **Objetivo**: proteger o Rei do ataque das Cartas.

- **Aliados**: 
  - **Peças especiais**: 
    - **Rei**: Não morre, se algum inimigo chegar até ele, o jogador perde 1 vida.
    - **Peão**: Pode dar dano no inimigo ao se sacrificar.
    
  - **Peças de ataque**:
     - **Torre**: Ataca na horizontal e vertical.
     - **Bispo**: Ataca nas diagonais.
     - **Rainha**: Junta o ataque da torre e do bispo.
     - **Cavalo**: Ataca em diversas direções de 45º.
 
- **Inimigos**: cartas de baralho. Vida das cartas baseada nos números e naipes.
 
- **Mecânicas principais**: 
  - O Player pode comprar aliados gastando seu dinheiro e tem um número limitado de vidas. 

  - Os aliados só podem ser colocados em locais válidos: onde não há outro aliado ou um inimigo.

  - Inimigos se transformam em cartas de menor número quando tomam dano.

  - Aliados podem ser colocados no caminho dos inimigos, mas morrem se colidirem com eles. 

  - O caso especial é do Peão, que tem mais vidas e dá dano no inimigo com o qual colidiu.

  - O Rei sempre está presente e tenta se proteger com projéteis fracos, mas o Player não pode invocar outro.

## Referências

- Bloons Tower Defense

- Jogo de Xadrez

- Jogos de Baralho

## Documentação do Código

- Baseada em docstrings no próprio código.

- **Arquivos principais**: 

    - **main.py**: utilizado para iniciar o jogo, ao ser rodado.
    
    - **game.py**: arquivo central contendo a classe Game. Tal classe permeia todo o desenvolvimento, pois uma instânia sua pode ser acessada por qualquer outra classe.
    
    - **constants.py**: arquivo central contendo todas as constantes, separadas por namespaces das classes. Utilizado para alterar características essenciais do game, tais como framerate, tamanho da tela e balanceamento no geral.
    
## Artes

- Foram utilizados assets gratuitos da internet para compor a arte do jogo.
