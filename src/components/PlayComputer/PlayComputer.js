import React from 'react';
import { Link } from 'react-router-dom';
import styles from './PlayComputer.module.scss';

const PlayComputer = () => {
  return (
    <div className={styles['play-computer']}>
      <h2>Play Against Computer</h2>
      <main>
        <div className={styles['game-options']}>
          <Link to="/play-computer/play-easy" >
            <button className={styles['easy']}>Easy</button>
          </Link>
          <Link to="/play-computer/play-medium">
            <button  className={styles['medium']}>Medium</button>
          </Link>
          <Link to="/play-computer/play-difficult" >
            <button className={styles['difficult']}>Difficult</button>
          </Link>
        </div>
      </main>
    </div>
  );
};

export default PlayComputer;