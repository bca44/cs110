def draw_flower(bit):
    '''
    Bit starts and ends at the base of the flower facing right
    '''
def exit_pool(bit):
    '''
    Bit starts at the bottom left of a pool, facing down
    Bit finishes at the upper right of the pool, facing up
    '''
def fill_pool(bit):
    '''
    Bit starts facing down into the empty pool on the upper left
    Bit finishes facing down in the bottom left of the bool
    '''
def fill_row_blue(bit):
    '''
    Bit starts facing down with an empty row to Bit's left
    Bit ends facing down in the same position with a blue row to Bit's left
    '''
def pond_and_flower(bit):
    '''
    Bit starts facing right above an empty pool
    Bit needs to fill the pool and draw the flower
    Bit will end facing right at the base of the flower
    '''
