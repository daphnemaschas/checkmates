// server.js
const express = require('express');
const connectDB = require('./config/db');
const createPartyRouter = require('./routes/CreateParty');
const joinPartyRouter = require('./routes/JoinParty');

const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors())
// Middleware pour permettre les requêtes de n'importe quelle origine
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
  });

// Connect to MongoDB
connectDB();

// Middleware
app.use(express.json());

// Routes
app.use('/api',createPartyRouter);
app.use('/api',joinPartyRouter);

// Start server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
