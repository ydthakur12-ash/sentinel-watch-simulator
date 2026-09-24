# Sentinel Watch Data Simulator

A Python-based wearable sensor data simulator for the Sentinel health and safety system.

The simulator generates sample watch sensor data for different situations and stores the readings in JSONL files. The saved datasets can also be replayed to simulate live sensor input for the detection engine.

---

## Features

- Simulates heart-rate data
- Simulates SpO₂ data
- Simulates 3-axis accelerometer data
- Generates activity/event information
- Supports multiple scenarios
- Saves sensor readings as JSONL datasets
- Replays previously generated datasets
- Provides a consistent sensor-data format for the detection engine

---

## Scenarios

The simulator supports four scenarios:

### 1. Normal Activity

Simulates regular watch readings during normal activity such as:

- Walking
- Resting

Dataset:

```text
data/normal.jsonl
---

## V2 Realistic Simulation

The `realistic-v2` branch contains an improved sensor simulation designed to produce more realistic temporal patterns.

### V2 Improvements

- Gradual heart-rate changes
- Gradual SpO₂ changes
- More natural accelerometer variation
- Multi-stage fall sequence
- Sustained low movement after a fall
- Gradual abnormal-health trend
- Separate V2 datasets
- Replay support for V2 datasets

### V2 Data

V2 datasets are stored separately from the original datasets:

```text
data/v2/
├── normal.jsonl
├── fall.jsonl
├── inactivity.jsonl
└── abnormal.jsonl---

## V2 Realistic Simulation

The `realistic-v2` branch contains an improved sensor simulation designed to produce more realistic temporal patterns.

### V2 Improvements

- Gradual heart-rate changes
- Gradual SpO₂ changes
- More natural accelerometer variation
- Multi-stage fall sequence
- Sustained low movement after a fall
- Gradual abnormal-health trend
- Separate V2 datasets
- Replay support for V2 datasets

### V2 Data

V2 datasets are stored separately from the original datasets:

```text
data/v2/
├── normal.jsonl
├── fall.jsonl
├── inactivity.jsonl
└── abnormal.jsonl
```

Current V2 dataset sizes:

- Normal: 20 readings
- Fall: 26 readings
- Inactivity: 20 readings
- Abnormal health: 20 readings

### Fall Sequence

The V2 fall scenario contains:

```text
Normal movement
       ↓
Sudden impact
       ↓
Post-fall low movement
```

The `activity` field is retained as a ground-truth label for testing. A detection engine should ideally determine events from the sensor measurements rather than using the activity label directly.

### V2 Branch

V2 development is maintained on:

```text
realistic-v2
```

The stable `main` branch remains unchanged.
