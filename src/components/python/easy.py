import serial
import numpy as np
import chess
import chess.svg
import time

import serial
import numpy as np
import chess
import chess.svg
import time

couleur = "blanc"  # faut mettre noir si on joue les noirs
case_white = [(0, i) for i in range(8)] + [(1, i) for i in range(8)]
case_black = [(6, i) for i in range(8)] + [(7, i) for i in range(8)]

board = chess.Board()


def reset_svg_board():
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


def nb_nonnull(M):
    s = 0
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] != 0:
                s += 1
    return s


def couleur_init(M):
    M = np.zeros((8, 8))


def detection_mangerbouger(L, M):
    S = M - L
    if nb_nonnull(S) == 2:
        return "bouger"
    elif nb_nonnull(S) == 1:
        return "manger"
    else:
        return "probleme"


def coordonnechess(x):
    coord = ["a", "b", "c", "d", "e", "f", "g", "h"]
    (i, j) = x
    return coord[j] + str((i + 1))


def printcoup(coups):
    (i, j) = coups[0]
    (k, l) = coups[1]
    return coordonnechess((i, j)) + coordonnechess((k, l))


def coupjoue(L, M):
    coups = [(0, 0), (0, 0)]
    S = M - L
    n = len(L)
    m = len(L[0])
    for i in range(n):
        for j in range(m):
            if S[i][j] == -1:
                coups[0] = (n - i - 1, j)
            elif S[i][j] == 1:
                coups[1] = (n - i - 1, j)
    return (printcoup(coups), coups[0], coups[1])


def convertir_en_coord(move):
    from_square = move.from_square
    to_square = move.to_square

    # Convertir de la représentation de la case (0-63) à (i, j)
    case_prec = divmod(from_square, 8)
    case_actuelle = divmod(to_square, 8)

    return case_prec, case_actuelle


def projection(matrice, cases):
    L = []
    for x in cases:
        (i, j) = x
        L.append(((i, j), matrice[7 - i][j]))
    return L


def unnonblack(matrice, black):
    L = []
    for i in range(8):
        for j in range(8):
            if (i, j) not in black:
                if matrice[7 - i][j] == 1:
                    L.append((8 - i, j))
    return L


def piecemorte(depart, arrivee, case_potentiel):
    victime = (-1, -1)
    compteur = 0
    for case in case_potentiel:  # voir s'il y'a une pièce noires qui bouge
        (i, j) = case
        if depart[7 - i][j] == 1:
            if arrivee[7 - i][j] == 0:
                victime = case
                compteur += 1
    if compteur > 1:
        print("probleme : il ya plusieurs pieces noires qui ont bouge")
    return victime


def trouvermoinsun(prec, suiv):
    S = suiv - prec
    n = len(S)
    for i in range(n):
        for j in range(n):
            if S[i][j] == -1:
                return (7 - i, j)


z = 1
t = 0  # Quand t vaut 0 on est en phase de deplacement, que ce soit nous ou l'adverse, quand t vaut 1, cest quand l'IA doit reflechir
if couleur == "blanc":
    turn = 0  # faut le initialiser a 1 si le joueur reel jour le noir
else:
    turn = 1  # ça cest le tour des noirs

tempsdattente = 20
compteur_temps = 0
victime = (-1, -1)
mort = False
while 0 < z:
    for i in range(9):
        l = ser.readline().decode("utf-8").strip()
        s_ech.append(l)
    if s_ech[0] == "a":  # le a délimite deux échiquiers
        echiquier = s_ech[1:]
    if s_ech[8] == "a":
        echiquier = s_ech[:8]
    s_ech = []
    boardd = transfo(echiquier)
    print("actuellement")  # On affiche ce qu'on recoit de l'arduino
    for x in boardd:
        print(x)
    if z == 1:
        suiv = boardd
        display_board(board)
    else:
        if t % 2 == 0:  # cest le moment de bouger
            if suiv != boardd:
                print("le compteur temps", compteur_temps)
                if compteur_temps == 0:
                    if turn == 0:
                        if (-1, -1) != piecemorte(
                            suiv, boardd, case_black
                        ) and not mort:
                            victime = piecemorte(suiv, boardd, case_black)
                            mort = True
                    else:
                        if (-1, -1) != piecemorte(
                            suiv, boardd, case_white
                        ) and not mort:
                            victime = piecemorte(suiv, boardd, case_white)
                            mort = True
                    suiv_potentiel = boardd
                    compteur_temps += 1
                elif compteur_temps < tempsdattente:
                    suiv_bis = boardd
                    if turn == 0:  # cest le tour des blancs
                        cases = case_white
                        cases_ennemi = case_black
                    else:
                        cases = case_black
                        cases_ennemi = case_white
                    if mort:
                        if projection(suiv_bis, cases + [victime]) != projection(
                            suiv_potentiel, cases + [victime]
                        ):  # or victime in cases:
                            compteur_temps = 0
                        else:
                            if nb_nonnull(suiv_bis) == nb_nonnull(suiv) - 1:
                                if projection(suiv_bis, cases) != projection(
                                    suiv, cases
                                ):
                                    compteur_temps += 1
                                else:
                                    compteur_temps = 0
                            else:
                                compteur_temps = 0
                    else:
                        if unnonblack(suiv_bis, cases_ennemi) != unnonblack(
                            suiv_potentiel, cases_ennemi
                        ):
                            compteur_temps = 0
                        else:
                            if nb_nonnull(suiv_bis) == nb_nonnull(suiv):
                                compteur_temps += 1
                            else:
                                compteur_temps = 0
                else:  # Ici on a enregistre quun coup doit être joué
                    prec = suiv
                    suiv = suiv_potentiel
                    mangerbouger = detection_mangerbouger(
                        np.array(prec), np.array(suiv)
                    )
                    if mangerbouger == "bouger":
                        coupjoued, case_prec, case_actuelle = coupjoue(
                            np.array(prec), np.array(suiv)
                        )
                        if turn == 0:
                            if (
                                case_prec in case_white
                            ):  # On met a jour les positions des cases blanches
                                case_white.remove(case_prec)
                                case_white.append(case_actuelle)
                        else:
                            if (
                                case_prec in case_black
                            ):  # On met a jour les positions des cases blanches
                                case_black.remove(case_prec)
                                case_black.append(case_actuelle)
                        print(coupjoued)
                        try:
                            # jouer le coup du joueur
                            board.push(chess.Move.from_uci(coupjoued))
                            # Enregistre le nouveau tableau au format SVG
                            svg_board = chess.svg.board(board=board)
                            with open("chess_board.svg", "w") as svg_file:
                                svg_file.write(svg_board)
                        # Attendez 1 secondes avant que l'ordinateur joue
                        except ValueError as e:
                            print(f"Erreur : {e}")
                    elif mangerbouger == "manger":
                        mort = False
                        if turn == 0:
                            case_black.remove(victime)
                            case_white.append(victime)
                            case_depart = trouvermoinsun(np.array(prec), np.array(suiv))
                            case_white.remove(case_depart)
                            case_arrivee = victime
                            coupjoued = printcoup([case_depart, case_arrivee])
                            try:
                                # manger avec le coup du joueur
                                board.push(chess.Move.from_uci(coupjoued))
                                # Enregistre le nouveau tableau au format SVG
                                svg_board = chess.svg.board(board=board)

                                with open("chess_board.svg", "w") as svg_file:
                                    svg_file.write(svg_board)
                            # Attendez 1 secondes avant que l'ordinateur joue
                            except ValueError as e:
                                print(f"Erreur : {e}")
                            # la position de depart cest celle ou il ya un moins 1
                        else:
                            case_white.remove(victime)
                            case_black.append(victime)
                            case_depart = trouvermoinsun(np.array(prec), np.array(suiv))
                            case_black.remove(case_depart)
                            case_arrivee = victime
                            coupjoued = printcoup([case_depart, case_arrivee])
                            try:
                                # manger avec le coup du joueur
                                board.push(chess.Move.from_uci(coupjoued))
                                # Enregistre le nouveau tableau au format SVG
                                svg_board = chess.svg.board(board=board)

                                with open("chess_board.svg", "w") as svg_file:
                                    svg_file.write(svg_board)
                            # Attendez 1 secondes avant que l'ordinateur joue
                            except ValueError as e:
                                print(f"Erreur : {e}")
                            # la position de depart cest celle ou il ya un moins 1
                    else:
                        print("il ya un probleme de detection")
                    compteur_temps = 0
                    # maintenant c'est tour des noirs ou de lautre couleur si on joue les noirs
                    if turn == 0:
                        t = (
                            t + 1
                        ) % 2  # maintenant cest le tour de l'IA, qui joue que si cetait les blancs qui ont joué, si cest ladversaire bah cest a nous de jouer cette fois
                    turn = (turn + 1) % 2  # Ici on donne la main à lautre couleur
            else:
                compteur_temps = 0
                mort = False
        elif t % 2 == 1:  # phase trouver le coup de l'IA
            try:
                # Utiliser l'IA pour sélectionner le prochain coup
                move_from_ai = selectmove(depth=3)
                print("l'ordinateur joue", move_from_ai)
                ser.write(
                    str(move_from_ai).encode()
                )  # THOMAS ICI TU ADAPTES POUR BLUETOOTH STP !!!!!!!!!!!!!!!!!!!!!!!!!
            except ValueError as e:
                print(f"Erreur : {e}")
            t = (
                t + 1
            ) % 2  # maintenant c'est le moment d'observer lechiquier et voir lechiquier bouger puis enregistrer les coups
            # En gros, on considere que quand l'echiquier bouge, c'est comme si on le bouge à la main, on n'actualise le coup de l'IA sur le board que quand il est enregistré physiquement
    z += 1
