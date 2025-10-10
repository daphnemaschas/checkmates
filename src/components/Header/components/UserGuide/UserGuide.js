import React from "react";
import styles from "./UserGuide.module.scss"; // Assurez-vous que ce chemin est correct

function UserGuide() {
  return (
    <div className={styles.container}>
      <h1>User Guide</h1>
      <h2>Introduction:</h2>
      <p>
        Welcome to the user guide for the Connected Chessboard. This guide will
        walk you through the setup and basic usage of the connected chessboard,
        allowing you to enjoy the game of chess in a new and interactive way.
      </p>
      <h2>Table of Contents:</h2>
      <li>Hardware Setup</li>
      <li>Connecting to the App</li>
      <li>Playing Chess</li>
      <li>Additional Features</li>
      <li>Troubleshooting</li>
      <h2>1. Hardware Setup:</h2>
      <p>
        Unbox the connected chessboard and ensure all components are present.
        Place the chessboard on a stable surface. Connect to the chessboard
        using Bluetooth. Wait for the indicator lights to show that the
        chessboard is ready for use.
      </p>
      <h2>2. Connecting to the App:</h2>
      <p>
        Open the ChessMates.com or download it from the App Store or Google Play
        Store. Open the app and follow the on-screen instructions to create an
        account or log in. Once logged in, navigate to the settings menu and
        select "Connect to Chessboard." Follow the prompts to pair your device
        with the chessboard via Bluetooth or Wi-Fi.
      </p>
      <h2>3. Playing Chess:</h2>
      <p>
        Select "Play" from the main menu to start a new game. Choose your
        opponent (human or AI) and game settings (difficulty level, time
        controls, etc.). Place your pieces on the chessboard according to the
        standard setup. Use the app to make your moves by tapping on the piece
        you want to move and then tapping on the destination square or move
        directly the piece from the board. The chessboard will automatically
        update to reflect the current game state. Enjoy playing chess with
        friends or challenging the AI opponent.
      </p>
      <h2>4. Additional Features:</h2>
      <p>
        The Connected Chessboard app may include additional features such as
        tutorials, puzzles, and online multiplayer. Explore the app to discover
        all available features and settings.
      </p>
      <h2>5. Troubleshooting:</h2>
      <p>
        If you encounter any issues with the connected chessboard or app, refer
        to the troubleshooting section of the app or user manual. Common issues
        may include connectivity problems, software glitches, or hardware
        malfunctions. If unable to resolve the issue, contact customer support
        for assistance.
      </p>
    </div>
  );
}

export default UserGuide;
