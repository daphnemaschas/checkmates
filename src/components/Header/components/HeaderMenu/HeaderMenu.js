import React from "react";
import { Link } from "react-router-dom";
import styles from "./HeaderMenu.module.scss";

function HeaderMenu() {
  return (
    <div className={styles.MenuContainer}>
      <ul>
        <li>
          <Link to="/about"> About </Link>
        </li>
        <li>
          <Link to="/user-guide"> User Guide </Link>
        </li>
        <li>
          <Link to="/contact-us"> Contact Us </Link>
        </li>
      </ul>
    </div>
  );
}

export default HeaderMenu;
