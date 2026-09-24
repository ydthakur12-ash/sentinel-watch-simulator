const fs = require('fs');
const path = require('path');
const { createEmergencyEvent } = require('../models/emergencyEvent');

const filePath = path.join(__dirname, '..', 'data', 'emergencyEvents.json');

function readEvents() {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    return [];
  }
}

function writeEvents(events) {
  fs.writeFileSync(filePath, JSON.stringify(events, null, 2));
}

function createEvent(data) {
  const events = readEvents();
  const event = createEmergencyEvent(data);
  events.push(event);
  writeEvents(events);
  return event;
}

function getEvent(id) {
  return readEvents().find(event => event.id === id);
}

function updateEvent(id, response) {
  const events = readEvents();
  const index = events.findIndex(event => event.id === id);

  if (index === -1) return null;

  const event = events[index];
  event.response = response;
  event.status = response === 'SAFE' ? 'CANCELLED' : 'ESCALATED';
  event.updatedAt = new Date().toISOString();

  events[index] = event;
  writeEvents(events);

  return event;
}

function escalateEvent(id) {
  return updateEvent(id, 'NO_RESPONSE');
}

module.exports = {
  createEvent,
  getEvent,
  updateEvent,
  escalateEvent
};
