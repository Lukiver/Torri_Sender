from tkinter import messagebox
from pathlib import Path
import random
import pyautogui
from file_operation import *
from config import *

# Функция для чтения строк из файла


# Функция для получения случайной строки
def send_random_text():
    """Возвращает случайную строку из списка строк."""
    global file_lines
    if not file_lines:
        return "либо ты ебанат не загрузио файл, либо он пуст("
    return random.choice(file_lines).strip()

# Функция для получения секунд
def send_seconds():
    global second
    second = float(write_seconds.get())
    return second


# Функция для переключения состояния поля ввода
def toggle_state():
    if write_seconds and nick_entry["state"] == "normal":  # Если поле активно
        write_seconds.config(state="readonly")
        nick_entry.config(state="readonly")
        toggle_button.config(text="можна писать")
    else:  # Если поле только для чтения
        write_seconds.config(state="normal")
        nick_entry.config(state="normal")
        toggle_button.config(text="нальзя писать")


# Главная функция отправки текста
def send_text_loop():
    global paused
    while not stop_event.is_set():
        if not paused:
            # Используем .get() для получения значения из BooleanVar
            if send_with_tag.get():  # Проверка на True (отправка с ником)
                nick = nick_entry.get().strip()  # Получаем ник из текстового поля
                # Проверка, что ник не пуст
                if not nick:
                    messagebox.showwarning("ерор(", "без тега и жизни нет)")
                    return  # Не использовать программу дальше
                
                random_line = send_random_text()  # Получаем случайный текст
                tag = f"{nick},"  # Формируем строку вида "@ник, текст из файла"
                
                # Печатает строку в активное окно
                pyautogui.write(tag, 0.001) # задержка с написаем тега для того чтоб не было @pic
                pyautogui.write("space") # на всякий
                pyautogui.write(random_line)
                pyautogui.write("enter")  # Нажимает Enter

            else:  # Если send_with_tag == False (отправка без ника)
                random_line = send_random_text()  # Получаем случайный текст
                pyautogui.write(random_line)  # Печатает строку в активное окно
                pyautogui.write("enter")  # Нажимает Enter

            # Задержка перед следующим вводом
            time.sleep(second)

            

# Функция для выбора файла
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        read_file_lines(file_path)
        start_button["state"] = "normal"  # Разблокировать кнопку старта

# Функция для запуска работы
def start_sending():
    global worker_thread, paused
    if not worker_thread or not worker_thread.is_alive():
        paused = False
        stop_event.clear()
        worker_thread = threading.Thread(target=send_text_loop, daemon=True)
        worker_thread.start()
        status_label.config(text="трахаем))")

# Функция для паузы
def toggle_pause():
    global paused
    paused = not paused
    status_label.config(text="игра приостоновлена.." if paused else "трахаем))")

# Функция для выхода
def exit_app():
    global worker_thread
    if worker_thread and worker_thread.is_alive():
        stop_event.set()
        worker_thread.join()
    root.destroy()
