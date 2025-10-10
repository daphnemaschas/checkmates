import React, { useMemo, useState, useEffect, useCallback } from "react";
import { Chessboard } from "react-chessboard";
import { Chess } from "chess.js";
import io from "socket.io-client";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import styles from "./PlayLocal.module.scss";

const PlayLocal = () => {
  const game = useMemo(() => new Chess(), []);
  const [gamePosition, setGamePosition] = useState(game.fen());

  const socket = useMemo(
    () => io("http://127.0.0.1:5000/played", { transports: ["websocket"] }),
    []
  );

  // useCallback pour mémoriser playMove
  const playMove = useCallback(
    (move) => {
      const result = game.move(move, { strict: false }); //erreur ici
      if (result) {
        setGamePosition(game.fen());
      } else {
        console.error("Move invalid:", move);
      }
    },
    [game]
  );

  useEffect(() => {
    socket.on("connect", () => {
      console.log("Connected to Flask server on namespace '/played'!");
    });

    socket.on("coupjoued", (data) => {
      console.log("Move received from server:", data.coupjoued);
      playMove(data.coupjoued);
    });

    return () => {
      socket.off("connect");
      socket.off("coupjoued");
      //socket.close();
    };
  }, [socket, playMove]); // Ajout de playMove dans le tableau des dépendances

  function onDrop(sourceSquare, targetSquare) {
    try {
      const move = game.move({
        from: sourceSquare,
        to: targetSquare,
        promotion: "q", // Promotion automatique des pions à la reine pour l'instant
      });

      if (move === null) {
        toast.error("Coup illégal !", {
          position: "top-center",
          autoClose: 3000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "colored",
        });

        return false; // Retourner false si le coup est illégal
      }
      // Récupérer le coup au format standard
      const standardMove =
        sourceSquare + targetSquare + (move.promotion ? move.promotion : "");

      socket.emit("game_mode", { mode: "localplay" });
      // Envoyer le coup au serveur Flask via une requête HTTP POST
      socket.emit("localplayed", { localplayed: standardMove });

      setGamePosition(game.fen()); // Mettre à jour la position du jeu
      return true;
    } catch (error) {
      toast.error("Error on attempted move : " + error.message, {
        position: "top-center",
        autoClose: 3000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "colored",
      });
      return false;
    }
  }

  return (
    <div className={styles.chessBoardContainer}>
      <ToastContainer />
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

export default PlayLocal;
