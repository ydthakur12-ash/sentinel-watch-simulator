require('dotenv').config();

const express = require('express');
const cors = require('cors');
const emergencyRoutes = require('./routes/emergencyRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.json({
    project: 'Team Sentinel',
    module: 'Backend + Emergency Alert',
    status: 'running',
    prototype: true
  });
});

app.use('/api/emergency', emergencyRoutes);

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({
    success: false,
    message: 'Internal server error'
  });
});

app.listen(PORT, () => {
  console.log(`Team Sentinel backend running on http://localhost:${PORT}`);
});
