import React from "react";
import chessBoardImage from "../../../assets/images/chess_board.svg";
import styles from "./PlayDifficult.module.scss";

const PlayDifficult = () => {
  return (
    <div>
      <img
        src={chessBoardImage}
        alt="Chess Board"
        className={styles.chessBoardImage}
      />
      <div className={styles.chessBoardContainer}>
        <button className={styles.undoButton}>Undo</button>
        <button className={styles.undoButton}>Resign</button>
      </div>
    </div>
  );
};

export default PlayDifficult;
