🎮 Jogo da Velha em Python (Tic-Tac-Toe)

Este é um simples jogo da velha (Tic-Tac-Toe) para dois jogadores, desenvolvido em Python para ser jogado no terminal.
O projeto foi feito para treinar lógica de programação, uso de dicionários, funções e tratamento de erros.

🚀 Funcionalidades

✅ Interface no terminal para interação direta com os jogadores.
✅ Validação de jogadas (não permite jogar em posições já ocupadas).
✅ Detecta vitória ou empate automaticamente.
✅ Mensagens de erro amigáveis caso o usuário digite uma posição inválida.

🕹️ Como jogar

Clone este repositório ou faça o download do arquivo:

git clone https://github.com/SEU_USUARIO/nome-do-repo.git


Entre na pasta do projeto:

cd nome-do-repo


Execute o jogo:

python3 jogo_da_velha.py


Siga as instruções no terminal:

O Jogador 1 (X) começa.

Digite a posição do tabuleiro onde deseja jogar.

Exemplo de posições:

top-L | top-M | top-R
mid-L | mid-M | mid-R
low-L | low-M | low-R

🗂️ Estrutura do Código

O tabuleiro é representado por um dicionário Python (theBoard), onde cada chave é uma posição.

Funções principais:

game(): Exibe o tabuleiro atualizado.

check_winner(): Verifica se houve vitória ou empate.

check_position_player_one() / check_position_player_two(): Validam as jogadas de cada jogador.

💡 Exemplo de Jogo
Resultado atual:
    |   |
-------------
    |   |
-------------
    |   |

Instruções: Escolha uma posição para jogar. Exemplo: top-L, mid-M, low-R
Jogador 1 é X  |  Jogador 2 é O
Jogador 1, escolha sua posição: top-M

🛠️ Requisitos

Python 3.x instalado na sua máquina.
