import cx_Freeze

executables = [cx_Freeze.Executable("finalPlaneGame.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["arcade", "pyglet.clock"],
                           "include_files":["Maps", "Sprites"]}},
    executables = executables

    )