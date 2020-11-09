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
    version="2.3",
    description='Calculadora de distribuciones discretas o acumuladas en un rango.',
    executables=executables
)