# Quick Testing

Use PowerShell, Postman, or Thunder Client.

## 1. Start server

```powershell
npm install
npm start
```

## 2. Health check

```powershell
Invoke-RestMethod http://localhost:5000/
```

## 3. Create emergency

```powershell
$body = @{
  userId = "user_001"
  eventType = "Abnormal movement + inactivity"
  lastNormalActivity = "2026-09-24T19:52:00+05:30"
  location = "Home"
  latitude = 19.1234
  longitude = 73.1234
} | ConvertTo-Json

$event = Invoke-RestMethod `
  -Uri http://localhost:5000/api/emergency `
  -Method Post `
  -ContentType "application/json" `
  -Body $body

$event.event.id
```

Copy the returned event ID.

## 4. Simulate no response / escalation

Replace `EVT-...` with your actual ID:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/api/emergency/EVT-XXXXXXXX/escalate `
  -Method Post
```

The terminal should display the contextual emergency alert.

## 5. Test SAFE

Create another event, then:

```powershell
$body = @{ response = "SAFE" } | ConvertTo-Json

Invoke-RestMethod `
  -Uri http://localhost:5000/api/emergency/EVT-XXXXXXXX/response `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

## 6. Test HELP

```powershell
$body = @{ response = "HELP" } | ConvertTo-Json

Invoke-RestMethod `
  -Uri http://localhost:5000/api/emergency/EVT-XXXXXXXX/response `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```
