def king_is_in_check(chessboard : list[list[str]]) -> bool:
    King = [[n,x.index('♔')] for n,x in enumerate(chessboard) if '♔' in x]
    Pawn = [[n,h] for n,x in enumerate(chessboard) for h in range(0, len(x)) if '♟' == x[h]]   
    Rook = [[n,h] for n,x in enumerate(chessboard) for h in range(0, len(x)) if '♜' == x[h]] 
    if len(Pawn) > 0:
        for s in Pawn:
            s_1 = [s[0],s[1]]
            s_1[0] = s_1[0] + 1            
            for k in range(2):
                if k == 0:
                    s_1[1] = s_1[1] - 1
                    if [s_1] == King:
                        return True                
                else:
                    s_1[1] = s_1[1] + 2
                    if [s_1] == King:
                        return True
                    
    if len(Rook) > 0:
        for s in Rook: 
            s_1 = [s[0],s[1]] 
            for k in range(4):
                if k == 0:
                    while s_1[0] > 0:
                        s_1[0] = s_1[0] - 1
                        for u in Pawn:                                 
                            if s_1 == u:
                                s_1[0] = -1
                                break 
                        if [s_1] == King:
                            return True  
                elif k == 1:
                    s_1 = [s[0],s[1]]
                    while s_1[0] < 8:
                        s_1[0] = s_1[0] + 1
                        for u in Pawn:                                 
                            if s_1 == u:
                                s_1[0] = 8
                                break 
                        if [s_1] == King:
                            return True  
                elif k == 2:
                    s_1 = [s[0],s[1]]
                    while s_1[1] >= 0:
                        s_1[1] = s_1[1] - 1
                        for u in Pawn:                                 
                            if s_1 == u:
                                s_1[1] = -1
                                break 
                        if [s_1] == King:
                            return True                                                       
                elif k == 3:
                    s_1 = [s[0],s[1]]
                    while s_1[1] < 8:
                        s_1[1] = s_1[1] + 1 
                        for u in Pawn:                                 
                            if s_1 == u:
                                s_1[1] = 8
                                break 
                        if [s_1] == King:
                            return True                   
                                       

    return False
    





print(king_is_in_check([
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '♔'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '♜'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '♟'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♜', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]))



def king_is_in_check1(chessboard : list[list[str]]) -> bool:
    King = [(n,x.index('♔')) for n,x in enumerate(chessboard) if '♔' in x]
    Pawn = [(n,h) for n,x in enumerate(chessboard) for h in range(0, len(x)) if '♟' == x[h]]   
    Rook = [(n,h) for n,x in enumerate(chessboard) for h in range(0, len(x)) if '♜' == x[h]] 
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
