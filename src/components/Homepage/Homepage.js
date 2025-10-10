import React from "react";
import { Link } from "react-router-dom";
import styles from "./Homepage.module.scss";

const Homepage = () => {
  return (
    <div className={styles.homepage}>
      <header>
        <h1>Welcome to CheckMates </h1>
        <p>Play chess with friends or challenge the computer.</p>
      </header>
      <main>
        <div className={styles["game-options"]}>
          <Link to="/play-online">
            <button className={styles["play-online"]}>Play Online</button>
          </Link>
          <Link to="/play-computer">
            <button className={styles["play-computer"]}>
              Play Against Computer
            </button>
          </Link>
          <Link to="/play-local">
            <button className={styles["play-computer"]}>Play Local</button>
          </Link>
        </div>
      </main>
      <footer>
        <p>© 2023 CheckMates. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Homepage;
