import json
import os
import sys
import requests

BACKEND_URL = "http://localhost:5000/api/emergency"


def load_dataset(filename):
    path = os.path.join("data", filename)

    if not os.path.exists(path):
        print(f"Dataset not found: {path}")
        return []

    readings = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                readings.append(json.loads(line))

    return readings


def detect_emergency(readings):
    activities = [reading.get("activity") for reading in readings]

    # Fall followed by inactivity
    if "fall_detected" in activities:
        fall_index = activities.index("fall_detected")

        after_fall = activities[fall_index + 1:]

        if "post_fall_inactive" in after_fall:
            return {
                "detected": True,
                "event_type": "Fall + inactivity"
            }

        return {
            "detected": True,
            "event_type": "Fall detected"
        }

    # Prolonged inactivity
    if activities and all(activity == "inactive" for activity in activities):
        return {
            "detected": True,
            "event_type": "Prolonged inactivity"
        }

    # Abnormal health pattern
    if "abnormal" in activities or "abnormal_health" in activities:
        return {
            "detected": True,
            "event_type": "Abnormal health pattern"
        }

    return {
        "detected": False,
        "event_type": None
    }


def send_to_backend(event_type, readings):
    last_reading = readings[-1]

    payload = {
        "eventType": event_type,
        "lastNormalActivity": "23:05",
        "location": "Home",
        "latitude": 19.0760,
        "longitude": 72.8777
    }

    print("\nSending emergency to backend...")

    try:
        response = requests.post(
            BACKEND_URL,
            json=payload,
            timeout=5
        )

        print("Backend status:", response.status_code)
        print("Backend response:")
        print(response.text)

    except requests.exceptions.RequestException as error:
        print("Could not connect to backend.")
        print(error)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("python integration/detect_and_send.py fall.jsonl")
        return

    filename = sys.argv[1]

    print(f"\nReading dataset: {filename}")

    readings = load_dataset(filename)

    if not readings:
        return

    print(f"Readings loaded: {len(readings)}")

    result = detect_emergency(readings)

    if result["detected"]:
        print("\n⚠️ POSSIBLE EMERGENCY DETECTED")
        print("Event:", result["event_type"])

        send_to_backend(
            result["event_type"],
            readings
        )

    else:
        print("\n✅ No emergency detected.")


if __name__ == "__main__":
    main()