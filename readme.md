# PyCharm WSL2 Fix

Due to [a bug](https://youtrack.jetbrains.com/issue/PY-46578) that hasn't yet been fixed you can't run Run/Debug
configurations for Docker Compose projects which source lives in WSL2.

## Instructions
1. Install Python on Windows and [add it to the path](https://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them)
2. Set up the virtual env
```bash
python.exe -m virtualenv env
.\env\Scripts\activate.bat
pip install -r requirements.txt
```
2. Update `run.bat` to use the correct PyCharm version you are using
3. Run `.\run.bat`
4. Execute Run/Debug configuration in PyCharm. You should see the files being
watched and replaced by this script.