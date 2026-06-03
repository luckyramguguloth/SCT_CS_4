# Task 04: Local Event Key Logger & Defensive Study

An educational project demonstrating safe local-scoped application event handling alongside a comprehensive cybersecurity defensive analysis report.

## Overview
This folder contains two main components:
1.  **`key_listener.py`**: A safe local key logger that uses Python's built-in `tkinter` graphical engine to render a simple writing editor. Keystrokes are intercepted *only* when the editor window has focus. Keystrokes entered outside the application are completely ignored.
2.  **`keylogger_defense_report.md`**: A professional, highly technical study detailing how rogue system-wide keyloggers function, how operating systems operate their input event hooks, and how modern EDR and endpoint security solutions defend against unauthorized logging.

## Getting Started

### Prerequisites
*   Python 3.x installed.
*   `tkinter` library (standard package included with default Python installations).

### How to Run
Execute the local GUI listener via terminal:
```bash
python key_listener.py
```

### Log File Location
Once typing begins inside the editor window, the keys are recorded in real-time to a file named:
```
local_events.txt
```
*(Saved inside the same directory from which the script was executed).*

## Execution Result
Here is the execution demonstration showing the safe local GUI window keypress capture tool:

![Execution Result](Screenshot%202026-06-01%20095216.png)

