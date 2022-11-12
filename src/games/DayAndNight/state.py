from pickle import TRUE
from typing import Optional

import move as move

from src.games.DayAndNight import player
from src.games.DayAndNight.action import DayAndNightAction
from src.games.DayAndNight.result import DayAndNightResult
from src.games.state import State


class DayAndNightState(State):

    EMPTY_CELL = -1

    
    



    ###Tamanho do tabuleiro 11x11

    def __init__(self, num_rows: int = 11, num_cols: int = 11):  
        super().__init__()

        ###Tamanho do tabuleiro tem de ser pelo menos 8x8
        if num_rows < 8:
            raise Exception("the number of rows must be 8 or over")
        if num_cols < 8:
            raise Exception("the number of cols must be 8 or over")

        ###Verifica se o tabuleiro tem o nº de colunas = ao nº de linhas
        if num_rows!=num_cols:
            raise Exception ("O tabuleiro deve ser do tipo N x N")
        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        self.__grid = [[DayAndNightState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]
        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 5 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 4):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player and \
                        self.__grid[row][col + 4] == player:
                    return True

        # check for 5 up and down
        for row in range(0, self.__num_rows - 4):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player and \
                        self.__grid[row + 4][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: DayAndNightAction) -> bool:
        colf = action.get_col()
        rowf = action.get_lin()

        # valid column
        if colf < 0 or colf >= self.__num_cols:
            return True

        # validar linha
        if rowf < 0 or rowf >= self.__num_rows:
            return True

        # Espaco ocupado por outra peca
        if self.__grid[colf][rowf] == DayAndNightState.EMPTY_CELL:
            return True
            ###Alterei de != para == 

        # Validar se e adjacente
        #if self.__grid[colf][rowf] == self.__grid[coli+1][rowi] or self.__grid[coli-1][rowi] or self.__grid[coli][rowi -1] or self.__grid[coli][rowi +1]:
            return True

        # Validar se e lugar preto
        ###Valida se a posição é par ou impar , se for impar é quadrado preto, senão é branco
        if self.__grid[colf][rowf] % 2 != 0:
            return True



    ###Se se quiser mover uma peça , em vez de colocar uma nova
    def validate_move(self, action: DayAndNightAction) -> bool:
        colm = move.get_col()
        rowm = move.get_lin()

        # valid column
        if colm < 0 or colm >= self.__num_cols:
            return True

        # validar linha
        if rowm < 0 or rowm >= self.__num_rows:
            return True

        # Espaco ocupado por outra peca
        if self.__grid[colm][rowm] != DayAndNightState.EMPTY_CELL :
            return True

        ### Se o espaço estiver ocupado por uma peça do player atual 
        if self.__grid[colm][rowm] == player  :
            return True 

        # Validar se e adjacente
        #if self.__grid[colm][rowm] == self.__grid[coli+1][rowi] or self.__grid[coli-1][rowi] or self.__grid[coli][rowi -1] or self.__grid[coli][rowi +1]:
            return True

        # Validar se e lugar preto
        ###Valida se a posição é par ou impar , se for impar é quadrado preto, senão é branco
        if self.__grid[colm][rowm] % 2 != 0:
            return True

        return True







    def update(self, action: DayAndNightAction):
        if self.validate_action ==True:
            col = action.get_col()
            row = action.get_lin()
            for row in range(self.__num_rows - 1, -1, -1):
                if self.__grid[row][col] < 0:
                    self.__grid[row][col] = self.__acting_player
                    break


        ###Se o validate_move for True irá retirar a peça do lugar escolhido e posiciona-la no 
        # novo quadrado e apagaro que tinha no quadrado antigo
        ###Não está a funcionar, é so a teoria
        if self.validate_move == True:
            new_col = action.get_col()
            new_row = action.get_row()
            # drop the checker
            for new_row in range(self.__num_rows - 1, -1, -1):
                if self.__grid[new_row][new_col] < 0:
                    self.__grid[new_row][new_col] = self.__acting_player
                    self.__grid[row][col]=""
                    break



        

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
            0:                              'P',
            1:                              'B',
            DayAndNightState.EMPTY_CELL:       ' '
        }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")
        for row in range(0, self.__num_rows):
            if row < 10:
                print(' ', end="")
            print(row, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = DayAndNightState(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DayAndNightResult]:
        if self.__has_winner:
            return DayAndNightResult.LOOSE if pos == self.__acting_player else DayAndNightResult.WIN
        if self.__is_full():
            return DayAndNightResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass