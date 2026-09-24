function buildEmergencyAlert(event) {
  return {
    title: '🚨 EMERGENCY ALERT',
    body: [
      'Possible emergency detected',
      `Event: ${event.eventType}`,
      `Time: ${formatTime(event.timestamp)}`,
      `Last normal activity: ${formatTime(event.lastNormalActivity)}`,
      `Location: ${event.location}`,
      `Response: ${formatResponse(event.response)}`
    ].join('\n')
  };
}

function formatTime(isoString) {
  const date = new Date(isoString);
  return date.toLocaleTimeString('en-IN', {
    hour: 'numeric',
    minute: '2-digit',
    hour12: true
  });
}

function formatResponse(response) {
  return response.replaceAll('_', ' ');
}

async function notifyEmergencyContact(event) {
  const alert = buildEmergencyAlert(event);

  // Prototype:
  // For now we log the alert. Later this function can call
  // Firebase Cloud Messaging (FCM) or another notification provider.
  console.log('\n===== EMERGENCY CONTACT ALERT =====');
  console.log(alert.title);
  console.log(alert.body);
  console.log('====================================\n');

  return {
    sent: true,
    prototype: true,
    channel: 'console',
    alert
  };
}

module.exports = {
  buildEmergencyAlert,
  notifyEmergencyContact
};
