import React, { useState } from "react";
import axios from "axios";
import styles from "./JoinParty.module.scss";
import { useNavigate } from "react-router-dom";

const JoinParty = ({ onSubmit }) => {
  const [gameNumber, setGameNumber] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  const handleChange = (event) => {
    setGameNumber(event.target.value);
  };

  const handleJoin = async () => {
    try {
      const response = await axios.post(
        `http://localhost:5000/join-game/${gameNumber}`
      );
      if (response.status === 200) {
        // Rediriger vers la salle de jeu si la connexion est réussie
        navigate(`/game-room/${gameNumber}`);
      } else {
        setErrorMessage(
          response.data.error ||
            "An error occurred while joining the game. Please try again later."
        );
      }
    } catch (error) {
      console.error("Error joining game:", error);
      setErrorMessage(
        "An error occurred while joining the game. Please try again later."
      );
    }
  };

  return (
    <div className={styles.container}>
      <h2>Enter Game Number</h2>
      <div className={styles["input-container"]}>
        <input
          type="text"
          placeholder="Enter game number"
          value={gameNumber}
          onChange={handleChange}
        />
      </div>
      {errorMessage && <p className={styles.error}>{errorMessage}</p>}
      <button className={styles.joinButton} onClick={handleJoin}>
        Join
      </button>
    </div>
  );
};

export default JoinParty;
