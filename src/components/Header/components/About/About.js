import React from "react";
import styles from "./About.module.scss"; // Assurez-vous que ce chemin est correct

function About() {
  return (
    <div className={styles.container}>
      <h1>About Us</h1>
      <p>
        Welcome to CheckMates! This website is the initiative of a team of young
        engineers from CentraleSupélec who have decided to create a connected
        chessboard to enable people at a distance to play together on a physical
        chessboard and to allow people with reduced mobility to play chess with
        someone physically present. We are dedicated to providing the best
        service possible. The team consists of:
      </p>
      <div className={styles.teamGrid}>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Marie-Madelaine.png"
            alt="Marie-Madelaine"
            className={styles.image}
          />
          <p>Marie-Madeleine Salama</p>
          <p>PCB & electronics</p>
        </div>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Elias.png"
            alt="Elias"
            className={styles.image}
          />
          <p>Elias Essaadani</p>
          <p>PCB & electronics</p>
        </div>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Sharif.png"
            alt="Sharif"
            className={styles.image}
          />
          <p>Sharif Abdelhamid</p>
          <p>Mechanical design & assembly</p>
        </div>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Moad.png"
            alt="Moad"
            className={styles.image}
          />
          <p>Moad Ouaaline</p>
          <p>Software & assembly</p>
        </div>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Thomas.png"
            alt="Thomas"
            className={styles.image}
          />
          <p>Thomas Bordino</p>
          <p>Wireless communication & interface</p>
        </div>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Daphne.png"
            alt="Daphne"
            className={styles.image}
          />
          <p>Daphné Maschas</p>
          <p>Interface & Software</p>
        </div>
        <div className={styles.member}>
          <img
            src="/TeamMembers/Victor.png"
            alt="Victor"
            className={styles.image}
          />
          <p>Victor Volts</p>
          <p>Left</p>
        </div>
      </div>
      <p>
        We believe in the power of collaboration and strive to create an
        environment where everyone can thrive. Thank you for taking the time to
        learn more about us.
      </p>
    </div>
  );
}

export default About;
