
# ⏱ Pomodoro Timer App (Tkinter)

A simple Pomodoro timer built using Python and Tkinter. This app helps you stay focused and productive by working in short, timed intervals followed by breaks.

---

## 🚀 Features So Far

- Displays a 25-minute timer with a tomato image (Pomodoro-style)
- Start button to begin countdown
- Reset button (functionality yet to be added)
- Countdown updates every second on the screen
- Visual checkmark placeholder for tracking completed sessions
- Clean and aesthetic UI using color constants

---

## 🧱 Current UI Elements

- 🖼 **Canvas with a tomato image**
- ⏲ **Dynamic timer text (00:00 format)**
- 🎯 **Title label ("Timer")**
- ✅ **Start & Reset buttons**
- ✔️ **Checkmark label for progress**

---

## 🎨 Constants Used

| Constant         | Purpose                  |
|------------------|---------------------------|
| `PINK`           | For short breaks (future) |
| `RED`            | For long breaks (future)  |
| `GREEN`          | For UI text/labels        |
| `YELLOW`         | Background color          |
| `FONT_NAME`      | Uniform UI font           |
| `WORK_MIN`       | 25-minute work session    |
| `SHORT_BREAK_MIN`| 5-minute short break      |
| `LONG_BREAK_MIN` | 20-minute long break      |

---

## 🖼 Tomato Image

Make sure you have a `tomato.png` file in the same directory as `main.py`. It’s used as the centerpiece image in the UI.

---

## 🧠 Logic Implemented

- `start_timer()`: Starts a 25-minute countdown (currently hardcoded as 25 seconds for demo)
- `count_down(count)`: Updates the timer every second using `window.after`

---

## ✅ Next Steps (Not Implemented Yet)

- Add Reset button functionality
- Switch between work, short break, and long break sessions
- Track and display completed sessions with checkmarks
- Add session cycle logic (e.g., 4 Pomodoros = 1 long break)
- Optional: Add sound alerts