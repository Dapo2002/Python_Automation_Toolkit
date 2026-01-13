# A structural validation script that enforces game-specific constraints on a dictionary-based
# state machine, checking for piece counts, coordinate validity, and king existence.

chessBoard = {'1a': 'wrook', '1b': 'wbishop', '1c': 'wknight', '1d': 'wqueen', '1e': 'wking', '1f': 'wknight',
              '1g': 'wbishop', '1h': 'wrook',
              '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn',
              '2h': 'wpawn',
              '8a': 'brook', '8b': 'bbishop', '8c': 'bknight', '8d': 'bqueen', '8e': 'bking', '8f': 'bknight',
              '8g': 'bbishop', '8h': 'brook',
              '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn',
              '7h': 'bpawn', }


def isValidChessBoard(someBoard):
    whiteKing = 0
    blackKing = 0
    whitePieces = 0
    blackPieces = 0
    whitePawns = 0
    blackPawns = 0
    row = [1, 2, 3, 4, 5, 6, 7, 8]
    col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for position, piece in someBoard.items():
        if piece == 'wking':
            whiteKing += 1
        elif piece == 'bking':
            blackKing += 1
        if piece[0] == 'w':
            whitePieces += 1
        elif piece[0] == 'b':
            blackPieces += 1
        if piece == 'wpawn':
            whitePawns += 1
        elif piece == 'bpawn':
            blackPawns += 1
        if len(position) != 2 or int(position[0]) not in row or position[1] not in col:
            return False
        if piece[0] not in ['w', 'b'] or piece[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            return False
    if whiteKing != 1 or blackKing != 1:
        return False
    if whitePieces > 16 or blackPieces > 16:
        return False
    if whitePawns > 8 or blackPawns > 8:
        return False
    return True


result = isValidChessBoard(chessBoard)
print(result)
