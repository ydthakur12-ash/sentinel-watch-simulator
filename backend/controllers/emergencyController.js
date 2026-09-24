const emergencyService = require('../services/emergencyService');
const notificationService = require('../services/notificationService');

async function createEmergency(req, res, next) {
  try {
    const event = emergencyService.createEvent(req.body);

    res.status(201).json({
      success: true,
      message: 'Possible emergency created',
      event
    });
  } catch (error) {
    next(error);
  }
}

async function getEmergency(req, res, next) {
  try {
    const event = emergencyService.getEvent(req.params.id);

    if (!event) {
      return res.status(404).json({
        success: false,
        message: 'Emergency event not found'
      });
    }

    res.json({
      success: true,
      event
    });
  } catch (error) {
    next(error);
  }
}

async function respondToEmergency(req, res, next) {
  try {
    const response = String(req.body.response || '').toUpperCase();

    if (!['SAFE', 'HELP'].includes(response)) {
      return res.status(400).json({
        success: false,
        message: 'response must be SAFE or HELP'
      });
    }

    const event = emergencyService.updateEvent(req.params.id, response);

    if (!event) {
      return res.status(404).json({
        success: false,
        message: 'Emergency event not found'
      });
    }

    let notification = null;

    if (response === 'HELP') {
      notification = await notificationService.notifyEmergencyContact(event);
    }

    res.json({
      success: true,
      message: response === 'SAFE'
        ? 'Emergency cancelled because user is safe'
        : 'Emergency escalated',
      event,
      notification
    });
  } catch (error) {
    next(error);
  }
}

async function escalateEmergency(req, res, next) {
  try {
    const event = emergencyService.escalateEvent(req.params.id);

    if (!event) {
      return res.status(404).json({
        success: false,
        message: 'Emergency event not found'
      });
    }

    const notification =
      await notificationService.notifyEmergencyContact(event);

    res.json({
      success: true,
      message: 'Emergency escalated because there was no response',
      event,
      notification
    });
  } catch (error) {
    next(error);
  }
}

module.exports = {
  createEmergency,
  getEmergency,
  respondToEmergency,
  escalateEmergency
};
