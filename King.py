def king_is_in_check(chessboard : list[list[str]]) -> bool:
    King = [(n,x.index('♔')) for n,x in enumerate(chessboard) if '♔' in x]
    Pawn = [(n,x.index('♟')) for n,x in enumerate(chessboard) if '♟' in x]    
    if len(Pawn) > 0:
        for s in Pawn:
            s_line = s[0]            
            s_line = s_line + 1            
            s_column = s[1]
            for k in range(2):
                if k == 0:
                    s_moving = s_column - 1
                    Pawn_step = [(s_line, s_moving)]
                    if Pawn_step == King:
                        return True                
                else:
                    s_moving = s_column + 1
                    Pawn_step = [(s_line, s_moving)]
                    if Pawn_step == King:
                        return True
    return False
    





print(king_is_in_check([
    ['♟', ' ', ' ', ' ', '♟', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', '♟', ' '],
    [' ', ' ', ' ', '♟', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '♟', ' ', ' ', '♟', ' '],
    [' ', ' ', ' ', ' ', ' ', '♔', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]))


