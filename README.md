# 🧭 Python GPS Tracker

A simple Python program that simulates a basic GPS tracker.  
The player starts at the origin `(0, 0)` and can move **North, South, East, or West** using commands.

---

## 🚀 Features

- Start at position `(0, 0)`
- Move with commands:
  - `N` or `North` → Move **North**
  - `S` or `South` → Move **South**
  - `E` or `East` → Move **East**
  - `W` or `West` → Move **West**
- Case-insensitive commands (e.g., `n`, `NORTH`, `east`)
- Show current position **after each move**
- Enter `STOP` to end the session
- At the end:
  - Show the **final position**
  - Check if the user returned to the origin `(0, 0)`

---

## 📦 Installation

Clone this repository and navigate into it:

```bash
git clone https://github.com/yourusername/HCI-Examination.git
cd HCI-Examination

# For windows
python -m venv .venv

# For Linux or MacOS
python3 -m venv .venv

# gumawa ng environemnt
#pumasok sa environment

```

---

## ▶️ Usage

Run the program with:

```bash
python main.py
```

Example session:

```
Starting at position (0, 0)
Enter directions: N (North), S (South), E (East), W (West)
Type STOP to end the session.

Enter command: n
Current position: (0, 1)

Enter command: e
Current position: (1, 1)

Enter command: stop

Session ended.
Final position: (1, 1)
You did not return to the origin.
```

---

## 📝 Notes

- Invalid inputs are handled gracefully.
- Only the commands listed above are accepted.

---

## 📜 License

This project is licensed under the MIT License.

```

---
```
