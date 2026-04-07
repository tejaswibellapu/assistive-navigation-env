---
title: Assistive Navigation Env
emoji: 🚶‍♂️
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false

---# 🌍 Assistive Navigation Decision Environmen

## 🚀 Overview

The **Assistive Navigation Decision Environment** is a real-world inspired OpenEnv environment designed to train and evaluate AI agents in making **safe navigation decisions for visually impaired individuals**.

This project is an extension of **GUIDEX**, an IoT-based smart mobility aid that uses camera input and edge processing to assist users in real-world navigation.

---

## 💡 Motivation

Visually impaired individuals face challenges such as:

* Detecting obstacles
* Crossing roads safely
* Navigating dynamic environments

While hardware systems (like GUIDEX) can capture environmental data, intelligent decision-making is still a critical component.

👉 This environment focuses on training the **decision-making intelligence (AI brain)** behind such systems.

---

## 🔗 Connection to GUIDEX

In the GUIDEX project:

* ESP32-CAM captures real-world visuals
* Computer vision + NLP convert scenes into descriptive text

In this environment:

* We simulate that pipeline using structured **text-based observations**
* The agent learns to make navigation decisions based on these inputs

This abstraction allows:

* Faster training
* Controlled evaluation
* Reproducible benchmarks

---

## ⚙️ Environment Design

### 🧾 Observation Space

The agent receives a **textual description of the environment**, for example:

```
"You are standing at a crosswalk. The signal is red. A car is approaching from the left."
```

This simulates processed perception from sensors/camera systems.

---

### 🎮 Action Space

The agent can choose from the following actions:

* MOVE_FORWARD
* STOP
* TURN_LEFT
* TURN_RIGHT
* WAIT

---

### 🔁 Core API (OpenEnv)

The environment follows the OpenEnv standard:

* `reset()` → initializes environment
* `step(action)` → returns:

  * observation
  * reward
  * done
  * info
* `state()` → returns current state

---

## 🎯 Tasks & Difficulty Levels

### 🟢 Easy Task — Obstacle Awareness

* Detect immediate danger
* Example: obstacle ahead → STOP

---

### 🟡 Medium Task — Directional Decision

* Choose correct path
* Example: blocked path → TURN_LEFT

---

### 🔴 Hard Task — Multi-step Navigation

* Handle sequences of decisions
* Example:

  * Wait for green signal
  * Cross road safely
  * Avoid moving obstacles

---

## 🧮 Reward Function

The reward system provides continuous feedback:

* ✅ Safe action → +0.5
* ✅ Correct navigation → +0.3
* ❌ Unsafe action → -1.0
* 🎯 Goal reached → +1.0

This ensures:

* Learning from partial progress
* Penalizing risky decisions
* Encouraging optimal behavior

---

## 🤖 Baseline Inference

The environment includes a baseline agent (`inference.py`) that:

* Uses OpenAI-compatible API
* Interacts with the environment
* Produces structured logs:

```
[START] ...
[STEP] ...
[END] ...
```

---

## 🐳 Setup & Installation

### 🔧 Prerequisites

* Docker
* Python 3.9+
* openenv-core

### 📦 Install dependencies

```
pip install openenv-core openai
```

---

### 🐳 Run with Docker

```
docker build -t assistive-env .
docker run assistive-env
```

---

### ▶️ Run Validation

```
openenv validate
```

---

## 🌐 Deployment

This environment is deployed on **Hugging Face Spaces** and responds to:

```
POST /reset
```

---

## 📊 Evaluation Criteria

Agents are evaluated based on:

* Safety of decisions
* Task completion
* Efficiency of navigation
* Reward accumulation

---

## 🌟 Key Features

* Real-world assistive navigation simulation
* Multi-level tasks (easy → hard)
* Continuous reward shaping
* OpenEnv compliant
* Reproducible evaluation

---

## 🚀 Future Work

* Integration with real-time camera input (ESP32-CAM)
* Multimodal inputs (vision + audio)
* Reinforcement learning training pipelines
* Deployment on wearable assistive devices

---

## 🏆 Conclusion

The Assistive Navigation Decision Environment bridges the gap between **AI decision-making and real-world accessibility challenges**, providing a scalable platform for training intelligent agents that can improve independent mobility for visually impaired individuals.

---
