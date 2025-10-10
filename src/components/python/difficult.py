import serial
import numpy as np
import chess
import chess.svg
import time

board = chess.Board()


def reset_svg_board():
    board = chess.Board()
    svg_board = chess.svg.board(board=board)
    with open("chess_board.svg", "w") as svg_file:
        svg_file.write(svg_board)


# Appeler cette fonction au début du script pour créer le fichier SVG initial
reset_svg_board()

# Connexion à l'Arduino via la communication série
port_arduino = "COM4"  # COM4 est le port spécifique de votre Arduino
ser = serial.Serial(port_arduino)
s_ech = []
echiquier = []
movehistory = []
idx = 1

# Pièces pour l'IA

pawntable = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    5,
    10,
    10,
    -20,
    -20,
    10,
    10,
    5,
    5,
    -5,
    -10,
    0,
    0,
    -10,
    -5,
    5,
    0,
    0,
    0,
    20,
    20,
    0,
    0,
    0,
    5,
    5,
    10,
    25,
    25,
    10,
    5,
    5,
    10,
    10,
    20,
    30,
    30,
    20,
    10,
    10,
    50,
    50,
    50,
    50,
    50,
    50,
    50,
    50,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

knightstable = [
    -50,
    -40,
    -30,
    -30,
    -30,
    -30,
    -40,
    -50,
    -40,
    -20,
    0,
    5,
    5,
    0,
    -20,
    -40,
    -30,
    5,
    10,
    15,
    15,
    10,
    5,
    -30,
    -30,
    0,
    15,
    20,
    20,
    15,
    0,
    -30,
    -30,
    5,
    15,
    20,
    20,
    15,
    5,
    -30,
    -30,
    0,
    10,
    15,
    15,
    10,
    0,
    -30,
    -40,
    -20,
    0,
    0,
    0,
    0,
    -20,
    -40,
    -50,
    -40,
    -30,
    -30,
    -30,
    -30,
    -40,
    -50,
]

bishopstable = [
    -20,
    -10,
    -10,
    -10,
    -10,
    -10,
    -10,
    -20,
    -10,
    5,
    0,
    0,
    0,
    0,
    5,
    -10,
    -10,
    10,
    10,
    10,
    10,
    10,
    10,
    -10,
    -10,
    0,
    10,
    10,
    10,
    10,
    0,
    -10,
    -10,
    5,
    5,
    10,
    10,
    5,
    5,
    -10,
    -10,
    0,
    5,
    10,
    10,
    5,
    0,
    -10,
    -10,
    0,
    0,
    0,
    0,
    0,
    0,
    -10,
    -20,
    -10,
    -10,
    -10,
    -10,
    -10,
    -10,
    -20,
]

rookstable = [
    0,
    0,
    0,
    5,
    5,
    0,
    0,
    0,
    -5,
    0,
    0,
    0,
    0,
    0,
    0,
    -5,
    -5,
    0,
    0,
    0,
    0,
    0,
    0,
    -5,
    -5,
    0,
    0,
    0,
    0,
    0,
    0,
    -5,
    -5,
    0,
    0,
    0,
    0,
    0,
    0,
    -5,
    -5,
    0,
    0,
    0,
    0,
    0,
    0,
    -5,
    5,
    10,
    10,
    10,
    10,
    10,
    10,
    5,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

queenstable = [
    -20,
    -10,
    -10,
    -5,
    -5,
    -10,
    -10,
    -20,
    -10,
    0,
    0,
    0,
    0,
    0,
    0,
    -10,
    -10,
    5,
    5,
    5,
    5,
    5,
    0,
    -10,
    0,
    0,
    5,
    5,
    5,
    5,
    0,
    -5,
    -5,
    0,
    5,
    5,
    5,
    5,
    0,
    -5,
    -10,
    0,
    5,
    5,
    5,
    5,
    0,
    -10,
    -10,
    0,
    0,
    0,
    0,
    0,
    0,
    -10,
    -20,
    -10,
    -10,
    -5,
    -5,
    -10,
    -10,
    -20,
]

kingstable = [
    20,
    30,
    10,
    0,
    0,
    10,
    30,
    20,
    20,
    20,
    0,
    0,
    0,
    0,
    20,
    20,
    -10,
    -20,
    -20,
    -20,
    -20,
    -20,
    -20,
    -10,
    -20,
    -30,
    -30,
    -40,
    -40,
    -30,
    -30,
    -20,
    -30,
    -40,
    -40,
    -50,
    -50,
    -40,
    -40,
    -30,
    -30,
    -40,
    -40,
    -50,
    -50,
    -40,
    -40,
    -30,
    -30,
    -40,
    -40,
    -50,
    -50,
    -40,
    -40,
    -30,
    -30,
    -40,
    -40,
    -50,
    -50,
    -40,
    -40,
    -30,
]


def display_board(board):
    return chess.svg.board(board=board)


def quiesce(alpha, beta):
    stand_pat = evaluate_board()
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    return alpha


def evaluate_board():
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = (
        100 * (wp - bp)
        + 320 * (wn - bn)
        + 330 * (wb - bb)
        + 500 * (wr - br)
        + 900 * (wq - bq)
    )

    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum(
        [
            -pawntable[chess.square_mirror(i)]
            for i in board.pieces(chess.PAWN, chess.BLACK)
        ]
    )
    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum(
        [
            -knightstable[chess.square_mirror(i)]
            for i in board.pieces(chess.KNIGHT, chess.BLACK)
        ]
    )
    bishopsq = sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum(
        [
            -bishopstable[chess.square_mirror(i)]
            for i in board.pieces(chess.BISHOP, chess.BLACK)
        ]
    )
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum(
        [
            -rookstable[chess.square_mirror(i)]
            for i in board.pieces(chess.ROOK, chess.BLACK)
        ]
    )
    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum(
        [
            -queenstable[chess.square_mirror(i)]
            for i in board.pieces(chess.QUEEN, chess.BLACK)
        ]
    )
    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum(
        [
            -kingstable[chess.square_mirror(i)]
            for i in board.pieces(chess.KING, chess.BLACK)
        ]
    )

    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    if board.turn:
        return eval
    else:
        return -eval


def alphabeta(alpha, beta, depthleft):
    bestscore = -9999
    if depthleft == 0:
        return quiesce(alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if score >= beta:
            return score
        if score > bestscore:
            bestscore = score
        if score > alpha:
            alpha = score
    return bestscore


def selectmove(depth):
    try:
        move = (
            chess.polyglot.MemoryMappedReader("bookfish.bin")
            .weighted_choice(board)
            .move()
        )
        movehistory.append(move)
        return move
    except:
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            board.push(move)
            boardValue = -alphabeta(-beta, -alpha, depth - 1)
            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
            if boardValue > alpha:
                alpha = boardValue
            board.pop()
        movehistory.append(bestMove)
        return bestMove


def transfo(echiquier):
    nv_echiquier = []
    for x in echiquier:
        y = []
        for w in x:
            if w == "0" or w == "1":
                y.append(int(w))
        nv_echiquier.append(y)
    return nv_echiquier


def coupjoue(L, M):
    coups = [(0, 0), (0, 0)]
    S = M - L
    n = len(L)
    m = len(L[0])
    print("m", M)
    print("l", L)
    for i in range(n):
        for j in range(m):
            if S[i][j] == -1:
                coups[0] = (n - i - 1, j)
            elif S[i][j] == 1:
                coups[1] = (n - i - 1, j)
    coord = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def coordonnechess(x):
        (i, j) = x
        return coord[j] + str((i + 1))

    def printcoup(coups):
        (i, j) = coups[0]
        (k, l) = coups[1]
        return coordonnechess((i, j)) + coordonnechess((k, l))

    return printcoup(coups)


z = 1
while 0 < z:
    for i in range(6):
        l = ser.readline().decode("utf-8").strip()
        s_ech.append(l)
    if s_ech[0] == "a":  # le a délimite deux échiquiers
        echiquier = s_ech[1:]
    if s_ech[5] == "a":
        echiquier = s_ech[:5]
    s_ech = []
    boardd = transfo(echiquier)
    print("actuellement", boardd)
    if z == 1:
        suiv = boardd
        display_board(
            board
        )  # je viens de le rajouter pour que le board ait l'air réinitialisé
    if suiv != boardd:
        prec = suiv
        suiv = boardd
        print("prec", prec)
        print("suiv", suiv)
        coupjoued = coupjoue(np.array(prec), np.array(suiv))
        print(coupjoued)
        try:
            # Répondre qu coup du joueur avec l'IA
            board.push(chess.Move.from_uci(coupjoued))

            # Enregistre le nv tableau au format SVG
            svg_board = chess.svg.board(board=board)

            # Attendez 3 secondes avant que l'ordinateur joue
            time.sleep(1)

            # Utiliser l'IA pour sélectionner le prochain coup
            move_from_ai = selectmove(depth=5)
            print("l'ordinateur joue", move_from_ai)
            board.push(move_from_ai)

            # Enregistrez le nouveau tableau au format SVG
            svg_board = chess.svg.board(board=board)

            with open("chess_board.svg", "w") as svg_file:
                svg_file.write(svg_board)
        except ValueError as e:
            print(f"Erreur : {e}")
    z += 1
