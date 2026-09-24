# Team Sentinel — Node.js Backend Prototype

This is the backend module for Person 5: Backend + Emergency Alert.

It implements the prototype lifecycle:

DETECT → VERIFY → WAIT → ESCALATE

The backend does not perform sensor detection. The Android/hardware side sends a possible emergency event to this API.

## Stack

- Node.js
- Express.js
- JSON file storage for the prototype
- CORS
- dotenv

No Flutter or Android Studio is required to run this backend.

## Setup

Open a terminal inside this folder:

```powershell
npm install
npm start
```

Server:

```text
http://localhost:5000
```

Test:

```text
GET http://localhost:5000/
```

## API

### 1. Create emergency

POST `/api/emergency`

Example JSON:

```json
{
  "userId": "user_001",
  "eventType": "Abnormal movement + inactivity",
  "lastNormalActivity": "2026-09-24T19:52:00+05:30",
  "location": "Home",
  "latitude": 19.1234,
  "longitude": 73.1234
}
```

### 2. User is safe

POST `/api/emergency/:id/response`

```json
{
  "response": "SAFE"
}
```

Result: `CANCELLED`

### 3. User requests help

POST `/api/emergency/:id/response`

```json
{
  "response": "HELP"
}
```

Result: `ESCALATED` and an emergency-contact alert is generated.

### 4. No response

POST `/api/emergency/:id/escalate`

Result: `ESCALATED` and an emergency-contact alert is generated.

### 5. Get event

GET `/api/emergency/:id`

## Why JSON storage?

This is intentionally a hackathon prototype. A real deployment should use Firestore/PostgreSQL/etc. The service layer isolates storage so it can be replaced later.

## FCM

`services/notificationService.js` currently logs the contextual alert to the terminal. This makes the complete backend flow testable without Firebase credentials.

Later, replace that function with Firebase Admin SDK/FCM. Keep service-account credentials on the backend only; never put them in the Android app.
