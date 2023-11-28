import tkinter as tk
import time
import random
import string
import threading
import keyboard

class SpamBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Spam Bot GUI")

        self.spamming = False

        self.label = tk.Label(master, text="Spam Bot")
        self.label.pack()

        self.activation_label = tk.Label(master, text="Состояние: Не активирован")
        self.activation_label.pack()

        self.start_button = tk.Button(master, text="Start Spam", command=self.start_spam)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Spam", command=self.stop_spam)
        self.stop_button.pack()

        self.bind_label = tk.Label(master, text="Бинды: 9 - Start Spam, 0 - Stop Spam")
        self.bind_label.pack()

        self.bind_keys()

    def start_spam(self, event=None):
        if not self.spamming:
            self.spamming = True
            self.update_activation_label()
            threading.Thread(target=self.spam).start()

    def stop_spam(self, event=None):
        if self.spamming:
            self.spamming = False
            self.update_activation_label()

    def spam(self):
        time.sleep(10)  # Пауза 10 секунд перед началом цикла

        while self.spamming:
            phrase = "PLEASE "
            word = phrase + ''.join(random.choice(string.ascii_letters) for _ in range(6))

            keyboard.write(word)  # Вводим фразу и 6 рандомных букв
            keyboard.press_and_release('enter')  # Нажимаем Enter

            time.sleep(60)  # Пауза 10 секунд перед следующей итерацией

    def update_activation_label(self):
        state = "Активирован" if self.spamming else "Не активирован"
        self.activation_label.config(text=f"Состояние: {state}")

    def bind_keys(self):
        self.master.bind_all("9", self.start_spam)
        self.master.bind_all("0", self.stop_spam)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamBotGUI(root)
    root.mainloop()
