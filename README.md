# Space Network Simulation 🛰️

A robust Python simulation of a deep-space communication network, modeling signal transmission, satellite relaying, and error handling.

## 🚀 Overview
This project simulates the real-world challenges of communicating across vast distances in space. It implements complex routing logic to overcome signal degradation, range limits, and random environmental interference.

## 🛠️ Key Features
* **Onion Routing Implementation:** Simulates secure, multi-hop message passing by encapsulating packets within packets (recursively).
* **Advanced Error Handling:** Uses a custom Exception hierarchy (`CommsError`, `LinkTerminatedError`, etc.) to manage signal loss, temporary interference, and recovery strategies.
* **Dynamic Routing Algorithm:** Implements a "Smart Send" logic that filters and sorts available satellites based on range and proximity to the target.
* **Object-Oriented Design:** Clean inheritance structure (`SpaceEntity` -> `Satellite`, `Planet`) to model the physical components.
* **Progressive Complexity:** Structured in 6 levels, moving from direct transmission to complex multi-hop automated routing.

## 💻 Technologies
* **Language:** Python 3.x
* **Core Concepts:** OOP, Recursion, Algorithms (Bubble Sort, Pathfinding), Exception Handling.

## 📂 Project Structure
* `space_network_lib.py`: The physics engine (Range limits, Entropy/Noise simulation).
* `mission_utils.py`: The logic layer (Routing algorithms, Retry patterns, Packet decoding).
* `level-*.py`: Progressive scenarios testing the network capabilities.

---
*Created as part of an advanced Python Object-Oriented Programming study.*

