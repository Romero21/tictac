
import sys

array_list = [["0","1","2","3"],["1","_","_","_"],["2","_","_","_"],["3","_","_","_"]]

def player(number):
    player_choice = []
    player_input = input(f"\nPlayer {number} enter coordinates: ")
    if player_input.lower() == "exit":
        print("Thank you for playing game!!!")
        sys.exit()
    else:
        try:
            for x in player_input:
                if x != ",":
                    player_choice.append(int(x))
            if player_choice[0] > 3 or player_choice[1] > 3:
                print("\nPosition out of range!")
                return player_choice, False
            else:
                return player_choice, True
        except:
            print("Please insert correct coordinates!")
            return player_choice, False
            

def game_array(array_list):
    line = ""
    for x in array_list:
        for y in x:
            line += (y+" ")
        print(f"\t\t\t\t{line}")
        line = ""


def change_array(array_list, input, p_sign):
    temp = array_list[input[0]]
    try:
        if temp[input[1]] != "_":
            print("\n\t\tYou inserted wrong position!")
            return False
        else:
            temp[input[1]] = p_sign
            array_list[input[0]] = temp
            return True
    except:
        print("\n\t\tWrong format inserted!!!")


def check_array(array_list, p_sign):
    line1, line2, line3 = array_list[1], array_list[2], array_list[3]
    for x in range(1,4):
        if line1[x] == p_sign and line2[x] == p_sign and line3[x] == p_sign:
            return True
    for line in array_list:
        if line[1] == p_sign and line[2] == p_sign and line[3] == p_sign:
            return True
    if line1[1] == p_sign and line2[2] == p_sign and line3[3] == p_sign:
        return True
    if line1[3] == p_sign and line2[2] == p_sign and line3[1] == p_sign:
        return True


def play_player(p_sign, player_num):
    player_input, status = player(player_num)
    if status:
        if change_array(array_list, player_input, p_sign):
            game_array(array_list)
        else:
            play_player(p_sign, player_num)
    else:
        play_player(p_sign, player_num) 
    return player_num


def play_again():
    global array_list
    user_input = input("\nDo you wanna play again?(Y/N): ")
    if user_input.lower() == "y":
        array_list = [["0","1","2","3"],["1","_","_","_"],["2","_","_","_"],["3","_","_","_"]]
        game_array(array_list); main_game()
    elif user_input.lower() == "n":
        sys.exit()
    else:
        print("\nPlease insert correct option(Y/N)"); play_again()

def check_empty_positions(array_list):
    line1, line2, line3 = array_list[1], array_list[2], array_list[3]
    if "_" in line1 or "_" in line2 or "_" in line3:
        pass
    else:
        print("Game over! No left free positions!"); play_again()


if __name__ == "__main__":
    print('''
    
                         Welcome to game TIC TAC.
                            Enjoy your game.
        For playing insert coordinates in format 0,0(row, coloumn).
                         For exit game type exit.

          ''')
    game_array(array_list)
    while True:
        def main_game():
            player_num = play_player(p_sign = "X", player_num = 1)
            if check_array(array_list, p_sign = "X"):
                print(f"\nPlayer {player_num} is winner!")
                play_again()
            check_empty_positions(array_list)
            player_num = play_player(p_sign = "O", player_num = 2)
            if check_array(array_list, p_sign = "O"):
                print(f"\nPlayer {player_num} is winner!")
                play_again()
            check_empty_positions(array_list)
        main_game()