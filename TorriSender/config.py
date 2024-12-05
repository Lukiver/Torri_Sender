import threading

# Глобальные переменные
file_lines = []
paused = False  # Флаг для приостановки
stop_event = threading.Event()  # Событие для остановки потока
worker_thread = None
second = None
current_file = ""  # Переменная для хранения пути к текущему файлу
current_key = None
