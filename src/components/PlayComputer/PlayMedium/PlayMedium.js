import React, { useMemo, useState } from "react";
import { Chessboard } from "react-chessboard";
import { Chess } from "chess.js";
import styles from "./PlayMedium.module.scss";

const PlayMedium = () => {
  const game = useMemo(() => new Chess(), []);
  const [gamePosition, setGamePosition] = useState(game.fen());

  function onDrop(sourceSquare, targetSquare) {
    const move = game.move({
      from: sourceSquare,
      to: targetSquare,
      promotion: "q", // Promotion automatique des pions à la reine pour l'instant
    });

    if (move === null) return false; // Retourner false si le coup est illégal
    setGamePosition(game.fen()); // Mettre à jour la position du jeu
    return true;
  }

  return (
    <div className={styles.chessBoardContainer}>
      <div className={styles.chessBoardImage}>
        <Chessboard
          id="BasicBoard"
          position={gamePosition}
          onPieceDrop={onDrop}
          boardWidth={450}
        />
      </div>
      <div className={styles.chessBoardButton}>
        <button
          className={styles.undoButton}
          onClick={() => {
            game.undo();
            game.undo();
            setGamePosition(game.fen());
          }}
        >
          Undo
        </button>
        <button
          className={styles.undoButton}
          onClick={() => {
            game.reset();
            setGamePosition(game.fen());
          }}
        >
          Reset
        </button>
      </div>
    </div>
  );
};

export default PlayMedium;
