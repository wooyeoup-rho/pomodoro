# Pomodoro App
A simple Pomodoro Timer built with Python and Tkinter.

Created as a part of [
100 Days of Code: The Complete Python Pro Bootcamp
](https://www.udemy.com/course/100-days-of-code/) by Angela Yu.

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