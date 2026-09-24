import json
import random
import time
import os
from datetime import datetime


# ==========================================
# SENTINEL WATCH SIMULATOR V2
# ==========================================

DATA_DIR = "data/v2"
os.makedirs(DATA_DIR, exist_ok=True)


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def save_dataset(readings, filename):
    filepath = os.path.join(DATA_DIR, filename)

    # V2 creates a fresh dataset each time
    with open(filepath, "w") as file:
        for reading in readings:
            file.write(json.dumps(reading) + "\n")


def create_reading(heart_rate, spo2, accel_x, accel_y, accel_z, activity):
    return {
        "timestamp": datetime.now().isoformat(),
        "heart_rate": int(heart_rate),
        "spo2": int(spo2),
        "accel_x": round(accel_x, 3),
        "accel_y": round(accel_y, 3),
        "accel_z": round(accel_z, 3),
        "activity": activity
    }


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def show_reading(reading):
    print(json.dumps(reading))


def wait():
    time.sleep(1)


# ==========================================
# NORMAL ACTIVITY
# ==========================================

def generate_normal():

    print("\n🟢 REALISTIC NORMAL ACTIVITY")
    print("-" * 45)

    readings = []

    heart_rate = 78
    spo2 = 98

    for i in range(20):

        # Gradual heart-rate movement
        heart_rate += random.uniform(-3, 3)
        heart_rate = clamp(heart_rate, 70, 90)

        # Small natural SpO2 variation
        spo2 += random.choice([-1, 0, 0, 0, 1])
        spo2 = clamp(spo2, 96, 100)

        activity = random.choice([
            "resting",
            "resting",
            "walking",
            "walking"
        ])

        # Movement changes gradually
        if activity == "walking":
            accel_x = random.uniform(-0.25, 0.25)
            accel_y = random.uniform(-0.25, 0.25)
            accel_z = random.uniform(0.80, 1.20)
        else:
            accel_x = random.uniform(-0.08, 0.08)
            accel_y = random.uniform(-0.08, 0.08)
            accel_z = random.uniform(0.92, 1.08)

        reading = create_reading(
            heart_rate,
            spo2,
            accel_x,
            accel_y,
            accel_z,
            activity
        )

        readings.append(reading)
        show_reading(reading)
        wait()

    save_dataset(readings, "normal.jsonl")

    print("\n✅ V2 normal dataset saved.")


# ==========================================
# FALL EVENT
# ==========================================

def generate_fall():

    print("\n🔴 REALISTIC FALL SEQUENCE")
    print("-" * 45)

    readings = []

    heart_rate = 80
    spo2 = 98

    # --------------------------------------
    # Phase 1: Normal movement
    # --------------------------------------

    print("\nPhase 1 → Normal movement")

    for i in range(10):

        heart_rate += random.uniform(-2, 3)
        heart_rate = clamp(heart_rate, 72, 92)

        spo2 += random.choice([-1, 0, 0, 1])
        spo2 = clamp(spo2, 96, 100)

        reading = create_reading(
            heart_rate,
            spo2,
            random.uniform(-0.25, 0.25),
            random.uniform(-0.25, 0.25),
            random.uniform(0.80, 1.20),
            "walking"
        )

        readings.append(reading)
        show_reading(reading)
        wait()

    # --------------------------------------
    # Phase 2: Sudden impact
    # --------------------------------------

    print("\n⚠️ Phase 2 → Sudden impact")

    reading = create_reading(
        105,
        95,
        random.uniform(-1.5, 1.5),
        random.uniform(-1.5, 1.5),
        random.uniform(2.5, 4.0),
        "fall_event"
    )

    readings.append(reading)
    show_reading(reading)
    wait()

    # --------------------------------------
    # Phase 3: Post-fall low movement
    # --------------------------------------

    print("\n🟡 Phase 3 → Post-fall low movement")

    for i in range(15):

        heart_rate += random.uniform(-2, 2)
        heart_rate = clamp(heart_rate, 70, 105)

        spo2 += random.choice([-1, 0, 0, 1])
        spo2 = clamp(spo2, 93, 98)

        reading = create_reading(
            heart_rate,
            spo2,
            random.uniform(-0.025, 0.025),
            random.uniform(-0.025, 0.025),
            random.uniform(0.97, 1.03),
            "post_fall_inactive"
        )

        readings.append(reading)
        show_reading(reading)
        wait()

    save_dataset(readings, "fall.jsonl")

    print("\n✅ V2 fall dataset saved.")
    print("   Sequence: normal → impact → low movement")


# ==========================================
# PROLONGED INACTIVITY
# ==========================================

def generate_inactivity():

    print("\n🟡 REALISTIC PROLONGED INACTIVITY")
    print("-" * 45)

    readings = []

    heart_rate = 72
    spo2 = 98

    for i in range(20):

        heart_rate += random.uniform(-1.5, 1.5)
        heart_rate = clamp(heart_rate, 65, 82)

        spo2 += random.choice([-1, 0, 0, 1])
        spo2 = clamp(spo2, 96, 100)

        reading = create_reading(
            heart_rate,
            spo2,
            random.uniform(-0.025, 0.025),
            random.uniform(-0.025, 0.025),
            random.uniform(0.97, 1.03),
            "inactive"
        )

        readings.append(reading)
        show_reading(reading)
        wait()

    save_dataset(readings, "inactivity.jsonl")

    print("\n✅ V2 inactivity dataset saved.")


# ==========================================
# ABNORMAL HEALTH
# ==========================================

def generate_abnormal():

    print("\n🟠 SIMULATED ABNORMAL HEALTH TREND")
    print("-" * 45)

    readings = []

    heart_rate = 95
    spo2 = 95

    for i in range(20):

        # Gradual trend instead of random jumps
        heart_rate += random.uniform(0, 3)
        heart_rate = clamp(heart_rate, 95, 135)

        spo2 -= random.uniform(0, 0.4)
        spo2 = clamp(spo2, 89, 95)

        reading = create_reading(
            heart_rate,
            spo2,
            random.uniform(-0.20, 0.20),
            random.uniform(-0.20, 0.20),
            random.uniform(0.85, 1.15),
            "abnormal_health"
        )

        readings.append(reading)
        show_reading(reading)
        wait()

    save_dataset(readings, "abnormal.jsonl")

    print("\n✅ V2 abnormal-health dataset saved.")


# ==========================================
# REPLAY V2 DATASET
# ==========================================

def replay_dataset():

    print("\n📂 V2 SAVED DATASETS")
    print("-" * 45)

    print("1. Normal")
    print("2. Fall")
    print("3. Inactivity")
    print("4. Abnormal Health")

    choice = input("\nSelect dataset (1-4): ")

    datasets = {
        "1": "normal.jsonl",
        "2": "fall.jsonl",
        "3": "inactivity.jsonl",
        "4": "abnormal.jsonl"
    }

    if choice not in datasets:
        print("❌ Invalid choice.")
        return

    filename = datasets[choice]
    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.exists(filepath):
        print("❌ Dataset does not exist yet.")
        print("Generate the dataset first.")
        return

    print(f"\n▶ REPLAYING V2: {filename}")
    print("-" * 45)

    with open(filepath, "r") as file:

        for line in file:

            reading = json.loads(line)

            show_reading(reading)
            wait()

    print("\n========================================")
    print("         V2 REPLAY COMPLETE")
    print("========================================")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    print("========================================")
    print("   SENTINEL WATCH DATA SIMULATOR V2")
    print("========================================")

    print("1. Realistic Normal Activity")
    print("2. Realistic Fall Sequence")
    print("3. Realistic Prolonged Inactivity")
    print("4. Simulated Abnormal Health Trend")
    print("5. Replay V2 Saved Dataset")

    choice = input("\nSelect scenario (1-5): ")

    if choice == "1":
        generate_normal()

    elif choice == "2":
        generate_fall()

    elif choice == "3":
        generate_inactivity()

    elif choice == "4":
        generate_abnormal()

    elif choice == "5":
        replay_dataset()

    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()