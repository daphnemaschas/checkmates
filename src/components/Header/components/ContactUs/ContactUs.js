import React, { useState } from "react";
import styles from "./ContactUs.module.scss";

function ContactUs() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    // Vous pouvez ici envoyer le message ou effectuer toute autre action nécessaire
    // Après avoir soumis le formulaire, réinitialiser les champs
    setName("");
    setEmail("");
    setMessage("");
  };

  return (
    <div className={styles.container}>
      <h2>Contact Us</h2>
      <p>
        Don't hesitate to contact us in case of any issues, feedback, or
        suggestions for improvement. We value your input and are here to assist
        you.
      </p>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="message">Message:</label>
          <textarea
            id="message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            required
          ></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default ContactUs;
