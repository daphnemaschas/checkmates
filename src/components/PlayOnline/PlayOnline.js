import React from 'react';
import { Link } from 'react-router-dom';
import styles from './PlayOnline.module.scss';

const PlayOnline = () => {
  return (
    <div className={styles['play-online']}>
      <h2>Play Against Another Player Online</h2>
      <main>
        <div className={styles['game-options']}>
          <Link to="/play-online/create-party">
            <button className={styles['create-party']}> Create Party </button>
          </Link>
          <Link to="/play-online/join-party">
            <button className={styles['join-party']}> Join Party </button>
          </Link>
          <Link to="/play-online/join-random">
            <button className={styles['join-random-party']}> Join Random Party </button>
          </Link>
        </div>
      </main>
    </div>
  );
};

export default PlayOnline;