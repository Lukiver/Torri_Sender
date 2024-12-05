from supabase import create_client, Client
import subprocess
from pathlib import Path
import os
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Supabase API URL и ключ
SUPABASE_URL = "https://bomjwsilmmgnsqnnarua.supabase.co"  # Замените на ваш проект
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvbWp3c2lsbW1nbnNxbm5hcnVhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE5NzgzNTUsImV4cCI6MjA0NzU1NDM1NX0.Ton0bNObiU-V1iiWAbGrJiChYC2Pg7whURaTQGzK0sI"

# Создаем клиент Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


#Гайд
def open_info(): 
    showinfo(title="гайдек для ебаната", message='1. нужно ввести задержку либо x либо x.x где х это любое число. например 1 и 1.5 и нажать на кнопку "ну думаю сойдет"\n2. поставь галочку с тегом или без. если тегом то введи с @. а потом на "нельзя писать.\n3. потом нажми на выбрать пророчество и выбераешь файл с текстом\n4. теперь можешь ебашить нажав на лелуша\n так же ты можешь нажать на паузу выыбрать другой файл или другую задержку(для этого нажми на можна писать) или же ник и потом вновь продолжить нажав на ф9.\n by torri/yoha')


def get_activation_file_path():
    user_dir = Path.home()  # Получаем домашнюю директорию текущего пользователя
    activation_dir = user_dir / "AppData" / "Roaming" / "TorriSender"
    activation_dir.mkdir(parents=True, exist_ok=True)  # Создаём папку, если её нет
    return activation_dir / "activation_key.txt"
    

ACTIVATION_FILE = get_activation_file_path() # Путь к файлу, где будет храниться ключ активации

def get_system_uuid():
    """Получить UUID системы."""
    try:
        result = subprocess.check_output(
            ['wmic', 'csproduct', 'get', 'UUID'],
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            text=True
        ).splitlines()
        filtered_result = [line.strip() for line in result if line.strip()]
        return filtered_result[1] if len(filtered_result) > 1 else "Не удалось получить UUID"
    except Exception as e:
        return f"Ошибка получения UUID: {e}"

def check_activation_supabase(activation_key: str, user_uuid = get_system_uuid()) -> bool:
    """
    Проверяет, существует ли ключ активации в базе данных Supabase.
    
    """
    try:
        # Отправляем запрос к таблице "activation_keys" для проверки ключа
        response = supabase.table('keys').select('*').eq('key', activation_key).eq('uuid', user_uuid).execute()
        if response.data:
            # Сохранить ключ в локальный файл
            with open(ACTIVATION_FILE, "w") as f:
                f.write(activation_key)
            return True
        else:
            messagebox.showerror("ерор", "неверный ключек(")
            return False
    except Exception as e:
        messagebox.showerror("ошибка", f"Ошибка проверки активации: {e}")
        return False


def initial_activation_check_supabase():
    """
    Проверяет наличие локального файла с ключом активации и сверяет его с Supabase.
    """
    if os.path.exists(ACTIVATION_FILE):
        # Считываем ключ из файла
        with open(ACTIVATION_FILE, "r") as f:
            stored_key = f.read().strip()
        # Проверяем ключ через Supabase
        if check_activation_supabase(stored_key):
            return True
        else:
            return False
    else:
        # Если файла нет, запросить ключ активации
        messagebox.showinfo(
            "активация",
            'чтоб написать/вставить нужно нажать на "доо" и потом уже сможешь написать и еще чтоб ты смог вставить (ctrl + c) нужно чтоб была английска расскладка. так же после успешной проверки, перезапусти прогу',
        )
        return False

