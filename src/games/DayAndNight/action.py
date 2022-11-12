class DayAndNightAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __col: int
    __lin: int

    def __init__(self, col: int, lin: int):
        self.__col = col
        self.__lin = lin

    def get_col(self):
        return self.__col

    def get_lin(self):
        return self.__lin
