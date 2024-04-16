import socket
import time

import keyBoardLogic
from os import getenv
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()  # Finds the .env file path
load_dotenv(dotenv_path)  # loads the .env file from the path found about

PORT = 6667
CHANNEL = "#moffd234"
SERVER = "irc.chat.twitch.tv"
O_AUTH_PASSWORD = getenv("o_auth_password")


def get_chats():
    sock = socket.socket()
    sock.connect((SERVER, PORT))

    # Send channel parameters as encoded strings
    sock.send(f"PASS {O_AUTH_PASSWORD}\n".encode('utf-8'))
    sock.send(f"NICK {CHANNEL}\n".encode('utf-8'))
    sock.send(f"JOIN {CHANNEL}\n".encode('utf-8'))
    # resp = sock.recv(2048).decode('utf-8')
    # resp = sock.recv(2048).decode('utf-8')

    while True:
        time.sleep(.5)
        # Decode the received string and store it in the resp variable
        resp = sock.recv(2048).decode('utf-8')
        resp = trim_string(input_string=resp, start_char=":", end_char=":")
        # print(f"NEW RESPONSE = {resp}")

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            print(f'**{resp.strip()}**')
            handle_input(resp.strip())


def trim_string(input_string, start_char, end_char) -> str:
    start_index = input_string.find(start_char)
    end_index = input_string.find(end_char, start_index + 1)  # Look for end_char after start_index

    if start_index != -1 and end_index != -1:
        # ASSERT: start_index and end_index exist in the string
        trimmed_string = input_string[end_index + 1:]  # Trims the string to start_index + 1 to the end index
        return trimmed_string
    else:
        return input_string


def handle_input(response):
    switch_dict = {
        "up": keyBoardLogic.up_key,
        "down": keyBoardLogic.down_key,
        "left": keyBoardLogic.left_key,
        "right": keyBoardLogic.right_key,
        "start": keyBoardLogic.start,
        "a": keyBoardLogic.a_key,
        "b": keyBoardLogic.b_key,
    }

    # Split the response into command and multiplier
    parts = response.split()

    # Default multiplier is 1
    multiplier = 1

    # Extract the command and check if the last character is a digit
    command = parts[0].lower()
    if command[-1].isdigit():
        multiplier = int(command[-1])
        command = command[:-1]  # Remove the digit from the command

    # Use get() to handle the case where the command is not in the dictionary
    func = switch_dict.get(command)

    if func:
        for _ in range(multiplier):
            func()
    else:
        print("Unknown command:", response)
