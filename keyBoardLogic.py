import pydirectinput


def up_key():
    pydirectinput.press("w")
    print("Up pressed")


def down_key():
    pydirectinput.press("s")
    print("Down pressed")


def left_key():
    pydirectinput.press("a")
    print("Left pressed")


def right_key():
    pydirectinput.press("d")
    print("Right pressed")


def a_key():
    pydirectinput.press("x")
    print("A pressed")


def b_key():
    pydirectinput.press("z")
    print("B pressed")


def start():
    pydirectinput.press("return")
    print("Return pressed")
