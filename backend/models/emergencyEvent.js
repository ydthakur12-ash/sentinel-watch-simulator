function createEmergencyEvent(data) {
  const now = new Date();

  return {
    id: `EVT-${now.getTime()}`,
    userId: data.userId || 'user_001',
    eventType: data.eventType || 'Abnormal movement + inactivity',
    timestamp: data.timestamp || now.toISOString(),
    lastNormalActivity: data.lastNormalActivity || new Date(
      now.getTime() - 18 * 60 * 1000
    ).toISOString(),
    location: data.location || 'Unknown',
    latitude: data.latitude ?? null,
    longitude: data.longitude ?? null,
    response: 'PENDING',
    status: 'POSSIBLE_EMERGENCY',
    createdAt: now.toISOString(),
    updatedAt: now.toISOString()
  };
}

module.exports = { createEmergencyEvent };
