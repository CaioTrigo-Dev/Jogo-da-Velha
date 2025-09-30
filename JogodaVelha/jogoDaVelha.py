theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

playerOne = 'X'
playerTwo = 'O'

choicePlayerOne = ''
def game():
    print('Resultado atual:')
    print(f'  {theBoard["top-L"]} | {theBoard["top-M"]} | {theBoard["top-R"]} ')
    print('-------------')
    print(f'  {theBoard["mid-L"]} | {theBoard["mid-M"]} | {theBoard["mid-R"]} ')
    print('-------------')
    print(f'  {theBoard["low-L"]} | {theBoard["low-M"]} | {theBoard["low-R"]} ')
    print()
choicePlayerTwo = ''
while True:

    game()
    
    print('Instruções: Escolha uma posição para jogar. Exemplo: top-L, mid-M, low-R')
    print()
    print('Jogador 1 é X  |  Jogador 2 é O')

    choicePlayerOne = input('Jogador 1, escolha sua posição: ')
    try:
        def check_winner():
            if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] != ' ':
                print(f'Jogador {theBoard["top-L"]} venceu!')
                game()
            elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] != ' ':
                print(f'Jogador {theBoard["mid-L"]} venceu!')
                game()
            elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] != ' ':
                print(f'Jogador {theBoard["low-L"]} venceu!')
                game()
            elif theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] != ' ':
                print(f'Jogador {theBoard["top-L"]} venceu!')
                game()
            elif theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] != ' ':
                print(f'Jogador {theBoard["top-M"]} venceu!')
                game()
            elif theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] != ' ':
                print(f'Jogador {theBoard["top-R"]} venceu!')
                game()
            elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] != ' ':
                print(f'Jogador {theBoard["top-L"]} venceu!')
                game()
            elif theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] != ' ':
                print(f'Jogador {theBoard["top-R"]} venceu!')
                game()
            elif all(value != ' ' for value in theBoard.values()):
                print('Empate!')
                game()
        def check_position_player_one():
            for key, value in theBoard.items():
                if choicePlayerOne == key:
                    if value == ' ':
                        theBoard[key] = playerOne
                        check_winner()
                        game()
                    else:
                        print('Posição já ocupada! Tente novamente.')
                        game()
                elif choicePlayerOne not in theBoard.keys():
                    raise ValueError('Essa Posição não existe! Tente novamente.')
        check_position_player_one()
        choicePlayerTwo = input('Jogador 2, escolha sua posição: ')
        def check_position_player_two():
            for key, value in theBoard.items():
                if choicePlayerTwo == key:
                    if value == ' ':
                        theBoard[key] = playerTwo
                        check_winner()
                    else:
                        print('Posição já ocupada! Tente novamente.')
                elif choicePlayerTwo not in theBoard.keys():
                    raise ValueError('Essa Posição não existe! Tente novamente.')
        check_position_player_two()
    except ValueError as e:
        print(e)
        continue
















