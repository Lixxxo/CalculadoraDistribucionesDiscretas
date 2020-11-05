from cx_Freeze import setup, Executable

base = None

executables = [Executable("gui.py", base=base)]

packages = ["tkinter"]
build_exe_options = {"packages": packages}

options = {
    'build_exe': build_exe_options
}

setup(
    name="Calculadora de distribuciones discretas",
    options=options,
    version="1.0",
    description='Nopp',
    executables=executables
)