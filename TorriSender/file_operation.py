from tkinter import messagebox
from config import *
from pathlib import Path
import os, sys

def get_activation_file_path():
    user_dir = Path.home()  # Получаем домашнюю директорию текущего пользователя
    activation_dir = user_dir / "AppData" / "Roaming" / "TorriSender"
    activation_dir.mkdir(parents=True, exist_ok=True)  # Создаём папку, если её нет
    return activation_dir / "activation_key.txt"
    

ACTIVATION_FILE = get_activation_file_path() # Путь к файлу, где будет храниться ключ активации

#Функция для получения пути к файлу в PyInstaller
def resource_path(relative_path):
    try:
        # PyInstaller создает временный путь, если файл находится внутри .exe
        base_path = sys._MEIPASS
    except AttributeError:
        # Если скрипт запускается не как .exe, используем текущую директорию
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def read_file_lines(file_path):
    """Читает строки из указанного файла."""
    global file_lines, current_file
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            file_lines = file.readlines()
        current_file = Path(file_path).name
        messagebox.showinfo("маладец)", "666")
        name_file.config(text=f"вот тако: {current_file}")
    except Exception as e:
        messagebox.showerror("лс ты ебанный)", f"ни палучалс загрузить: {e}")
    return current_file
