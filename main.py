from pynput import keyboard
import webbrowser

class KeyListener:
    def __init__(self, key_combo=[]):
        self.keys_pressed = set()
        self.key_combo = key_combo

    def on_press(self, key):
        print(f"Pressed {str(key)}")
        try:
            self.keys_pressed.add(key.char)
        except AttributeError:
            self.keys_pressed.add(str(key))

        # if 'c' in self.keys_pressed and "Key.tab" in self.keys_pressed:
        if all(k in self.keys_pressed for k in self.key_combo):
            webbrowser.open('https://chat.openai.com', new=0)
            self.keys_pressed.clear()  # Reset the set

    def on_release(self, key):
        print(f"Released {str(key)}")
        try:
            self.keys_pressed.discard(key.char)
        except AttributeError:
            self.keys_pressed.discard(str(key))
    
    def listen(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    key_listener = KeyListener(key_combo=['c', 'Key.tab'])
    key_listener.listen()
