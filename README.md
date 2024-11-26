# Pomodoro App
A simple Pomodoro Timer built with Python and Tkinter.

Created as a part of [
100 Days of Code: The Complete Python Pro Bootcamp
](https://www.udemy.com/course/100-days-of-code/) by Angela Yu.

![pomodoro](https://github.com/user-attachments/assets/3ebdf367-c6bf-4947-b53d-dcb43fada63a)

---
### Download the executable:
- You can download the precompiled executable directly (Windows):
[Download Pomodoro v1.0](https://github.com/wooyeoup-rho/pomodoro/releases/download/v1.0/pomodoro.exe)

- Or check out the releases page:
[Pomodoro releases](https://github.com/wooyeoup-rho/pomodoro/releases/v1.0)

---
### Demonstration
The demonstration uses:
- Shorter time periods.
- Starts at 6 repetitions completed.

https://github.com/user-attachments/assets/bec9aeb3-7e52-479f-a81f-8b198f6924bd

---
### Requirements
1. Python
2. PyInstaller (For creating the executable)

### Installation
Clone the repository:

```commandline
git clone https://github.com/wooyeoup-rho/pomodoro.git
```

### Running the application:
```commandline
cd pomdoro
python main.py
```

### Creating an executable
1. Install PyInstaller
```commandline
pip install pyinstaller
```
2. Create the executable:
```commandline
pyinstaller --onefile --add-data "assets;assets" --name pomodoro --windowed --icon=assets/images/pomodoro.ico main.py
```
- `--onefile` bundles everything into a single executable.
- `--add-data "assets;assets"` includes everything in the `assets` file into the executable.
- `--name pomodoro` names the executable file.
- `--windowed` prevents a command-line window from appearing.
- `--icon=assets/images/pomodoro.ico` specifies the application icon.
- `main.py` specifies the Python script to bundle.

3. Locate and run the executable:

The executable will be located in the `dist` folder. You can now open the `pomodoro.exe` inside to open the application.
