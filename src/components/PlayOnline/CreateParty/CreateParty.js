import React, { useState } from "react";
import styles from "./CreateParty.module.scss";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const CreateParty = () => {
  const [gameNumber, setGameNumber] = useState("");
  const navigate = useNavigate();

  const navigateToGameRoom = async () => {
    try {
      // Tentez de "rejoindre" la partie que vous venez de créer pour incrémenter le nombre de joueurs
      await axios.post(`http://localhost:5000/join-game/${gameNumber}`);
      // Si tout va bien, naviguez vers la salle de jeu
      navigate(`/game-room/${gameNumber}`);
    } catch (error) {
      console.error(
        "Erreur lors de la tentative de rejoindre la partie créée :",
        error
      );
    }
  };

  const generateNumber = async () => {
    try {
      const response = await axios.post("http://localhost:5000/games");
      const generatedGameNumber = response.data.gameNumber;
      console.log(
        "Numéro de partie enregistré avec succès:",
        generatedGameNumber
      );
      setGameNumber(generatedGameNumber);
    } catch (error) {
      console.error(
        "Erreur lors de l'enregistrement du numéro de partie :",
        error
      );
    }
  };

  return (
    <div className={styles.container}>
      <h2>Generate Game Number</h2>
      <button onClick={generateNumber} className={styles.generateButton}>
        Generate
      </button>
      <div className={styles.gameNumber}>
        {gameNumber && <p>Game Number: {gameNumber}</p>}
      </div>
      <button className={styles.generateButton} onClick={navigateToGameRoom}>
        Go to Game Room
      </button>
    </div>
  );
};

export default CreateParty;
