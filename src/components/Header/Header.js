import React from "react";
import { Link } from "react-router-dom";
import styles from "./Header.module.scss";
import logocheckmates from "../../assets/images/horse_logo.png";
import { useState, useEffect, useRef } from "react";
import HeaderMenu from "./components/HeaderMenu/HeaderMenu";

function Header() {
  const [showMenu, setShowMenu] = useState(false);
  const menuRef = useRef(null);

  const handleClickOutside = (event) => {
    if (menuRef.current && !menuRef.current.contains(event.target)) {
      setShowMenu(false);
    }
  };

  useEffect(() => {
    if (showMenu) {
      document.addEventListener("mousedown", handleClickOutside);
    } else {
      document.removeEventListener("mousedown", handleClickOutside);
    }
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [showMenu]);

  return (
    <header className={styles.header}>
      <div>
        <Link to="/">
          <img
            className={styles.img}
            src={logocheckmates}
            alt="logo CheckMates"
          />
        </Link>
      </div>
      <i
        onClick={() => setShowMenu(true)}
        className={`fa-solid fa-bars ${styles.headerXs}`}
      ></i>
      {showMenu && (
        <div ref={menuRef}>
          <div className="calc"></div>
          <HeaderMenu />
        </div>
      )}
    </header>
  );
}

export default Header;
