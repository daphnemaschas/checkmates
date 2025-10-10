import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'; // Pour obtenir le numéro de partie de l'URL
import styles from './GameRoom.module.scss';
import chessBoardImage from '../../assets/images/chess_board.svg';

const GameRoom = () => {
  const { gameNumber } = useParams(); // Récupérer le numéro de partie de l'URL
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    // Ici, vous pouvez éventuellement ajouter la logique de connexion à votre serveur WebSocket avec le numéro de partie
    // Par exemple, WebSocketInstance.connect(gameNumber);
    // Assurez-vous de définir setConnected(true) lorsque la connexion est établie
    setConnected(true); // Pour l'exemple, nous supposons que la connexion est toujours réussie
  }, [gameNumber]);

  const resignGame = async () => {
    try {
      const response = await fetch(`https://restapi.fr/api/chessgames?gameNumber=${gameNumber}`, {
        method: 'DELETE',
      });
      if (response.ok) {
        console.log('Numéro de partie supprimé avec succès.');
        window.location.href = '/';
      } else {
        console.error('Erreur lors de la suppression du numéro de partie :', response.status);
      }
    } catch (error) {
      console.error('Erreur lors de la requête API :', error);
    }
  };

  return (
    <div>
      {connected ? (
        <h2 className={styles.connectedMessage}>Connected to game room {gameNumber}</h2>
      ) : (
        <h2 className={styles.failedMessage}>Failed to connect to game room {gameNumber}</h2>
      )}
      <img src={chessBoardImage} alt="Chess Board" className={styles.chessBoardImage} />
      <div className={styles.chessBoardContainer}>
      <button className={styles.undoButton}>Undo</button>
      
      <button onClick={resignGame} className={styles.undoButton}>Resign</button>
      </div>
    </div>
  );
};

export default GameRoom;