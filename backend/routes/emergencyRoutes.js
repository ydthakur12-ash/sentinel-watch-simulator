const express = require('express');
const controller = require('../controllers/emergencyController');

const router = express.Router();

router.post('/', controller.createEmergency);
router.get('/:id', controller.getEmergency);
router.post('/:id/response', controller.respondToEmergency);
router.post('/:id/escalate', controller.escalateEmergency);

module.exports = router;
