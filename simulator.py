import json
import random
import time
import os
from datetime import datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


# ==============================
# SAVE DATA
# ==============================

def save_data(data, filename):
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, "a") as file:
        file.write(json.dumps(data) + "\n")


def output_data(data, filename):
    print(json.dumps(data))
    save_data(data, filename)


# ==============================
# GENERATE SENSOR READING
# ==============================

def generate_reading(heart_rate, spo2, accel_x, accel_y, accel_z, activity):
    return {
        "timestamp": datetime.now().isoformat(),
        "heart_rate": heart_rate,
        "spo2": spo2,
        "accel_x": accel_x,
        "accel_y": accel_y,
        "accel_z": accel_z,
        "activity": activity
    }


# ==============================
# NORMAL ACTIVITY
# ==============================

def run_normal():

    print("\n🟢 NORMAL ACTIVITY")
    print("-" * 40)

    for i in range(15):

        heart_rate = random.randint(70, 90)
        spo2 = random.randint(96, 100)

        accel_x = round(random.uniform(-0.2, 0.2), 2)
        accel_y = round(random.uniform(-0.2, 0.2), 2)
        accel_z = round(random.uniform(0.85, 1.15), 2)

        activity = random.choice(["walking", "resting"])

        data = generate_reading(
            heart_rate,
            spo2,
            accel_x,
            accel_y,
            accel_z,
            activity
        )

        output_data(data, "normal.jsonl")

        time.sleep(1)

    print("\n========================================")
    print("       SIMULATION COMPLETE")
    print("========================================")


# ==============================
# FALL EVENT
# ==============================

def run_fall():

    print("\n🔴 FALL EVENT")
    print("-" * 40)

    # Normal activity before fall
    for i in range(10):

        heart_rate = random.randint(70, 90)
        spo2 = random.randint(96, 100)

        accel_x = round(random.uniform(-0.2, 0.2), 2)
        accel_y = round(random.uniform(-0.2, 0.2), 2)
        accel_z = round(random.uniform(0.85, 1.15), 2)

        data = generate_reading(
            heart_rate,
            spo2,
            accel_x,
            accel_y,
            accel_z,
            "walking"
        )

        output_data(data, "fall.jsonl")

        time.sleep(1)

    # Fall impact
    data = generate_reading(
        random.randint(105, 125),
        random.randint(92, 96),
        round(random.uniform(-1.5, 1.5), 2),
        round(random.uniform(-1.5, 1.5), 2),
        round(random.uniform(2.5, 4.0), 2),
        "fall_detected"
    )

    output_data(data, "fall.jsonl")

    time.sleep(1)

    # Post-fall inactivity
    for i in range(15):

        heart_rate = random.randint(80, 110)
        spo2 = random.randint(93, 98)

        accel_x = round(random.uniform(-0.05, 0.05), 2)
        accel_y = round(random.uniform(-0.05, 0.05), 2)
        accel_z = round(random.uniform(0.95, 1.05), 2)

        data = generate_reading(
            heart_rate,
            spo2,
            accel_x,
            accel_y,
            accel_z,
            "post_fall_inactive"
        )

        output_data(data, "fall.jsonl")

        time.sleep(1)

    print("\n========================================")
    print("       SIMULATION COMPLETE")
    print("========================================")


# ==============================
# PROLONGED INACTIVITY
# ==============================

def run_inactivity():

    print("\n🟡 PROLONGED INACTIVITY")
    print("-" * 40)

    for i in range(15):

        heart_rate = random.randint(65, 85)
        spo2 = random.randint(96, 100)

        accel_x = round(random.uniform(-0.03, 0.03), 2)
        accel_y = round(random.uniform(-0.03, 0.03), 2)
        accel_z = round(random.uniform(0.95, 1.05), 2)

        data = generate_reading(
            heart_rate,
            spo2,
            accel_x,
            accel_y,
            accel_z,
            "inactive"
        )

        output_data(data, "inactivity.jsonl")

        time.sleep(1)

    print("\n========================================")
    print("       SIMULATION COMPLETE")
    print("========================================")


# ==============================
# ABNORMAL HEALTH
# ==============================

def run_abnormal():

    print("\n🟠 ABNORMAL HEALTH")
    print("-" * 40)

    for i in range(15):

        heart_rate = random.randint(110, 150)
        spo2 = random.randint(88, 95)

        accel_x = round(random.uniform(-0.2, 0.2), 2)
        accel_y = round(random.uniform(-0.2, 0.2), 2)
        accel_z = round(random.uniform(0.85, 1.15), 2)

        activity = "abnormal_health"

        data = generate_reading(
            heart_rate,
            spo2,
            accel_x,
            accel_y,
            accel_z,
            activity
        )

        output_data(data, "abnormal.jsonl")

        time.sleep(1)

    print("\n========================================")
    print("       SIMULATION COMPLETE")
    print("========================================")


# ==============================
# REPLAY SAVED DATASET
# ==============================

def replay_dataset():

    print("\n📂 SAVED DATASETS")
    print("-" * 40)

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
        print("❌ Dataset not found:", filepath)
        return

    print("\n▶ REPLAYING:", filename)
    print("-" * 40)

    with open(filepath, "r") as file:

        for line in file:

            data = json.loads(line)

            print(json.dumps(data))

            time.sleep(1)

    print("\n========================================")
    print("         REPLAY COMPLETE")
    print("========================================")


# ==============================
# MAIN MENU
# ==============================

def main():

    print("========================================")
    print("     SENTINEL WATCH DATA SIMULATOR")
    print("========================================")

    print("1. Normal Activity")
    print("2. Fall Event")
    print("3. Prolonged Inactivity")
    print("4. Abnormal Health")
    print("5. Replay Saved Dataset")

    choice = input("Select scenario (1-5): ")

    if choice == "1":
        run_normal()

    elif choice == "2":
        run_fall()

    elif choice == "3":
        run_inactivity()

    elif choice == "4":
        run_abnormal()

    elif choice == "5":
        replay_dataset()

    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()