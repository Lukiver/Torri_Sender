import customtkinter as ctk
from tkinter import filedialog, messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from logic import send_seconds, toggle_state, select_file, start_sending, send_random_text, send_text_loop, exit_app, toggle_pause
from activation import check_activation_supabase, open_info  # Ensure this file contains the required functions
from file_operation import resource_path

print("Запуск программы...")
# Main window setup
root = ctk.CTk()
root.iconbitmap(default=resource_path("antik.ico"))
root.title("TorriOtpravitel")
root.geometry("527x300")

# Load background image
image_path = resource_path("back1.jpg")  # Path to the image
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Set background image
background_label = ctk.CTkLabel(root, image=photo)
background_label.place(relwidth=1, relheight=1)  # This stretches the image across the entire window

# Activation check
write_check_activation = ctk.CTkEntry(root)
write_check_activation.place(y=10, relwidth=1.0, relheight=0.5)

button_check_activation = ctk.CTkButton(root, text="отправить", command=lambda: check_activation_supabase(write_check_activation.get()))
button_check_activation.place(y=150, relwidth=1.0, relheight=0.5)

# Text rate entry
text_second = ctk.CTkLabel(root, text="скок текста в секунду (например, 1 или 1.5)")
text_second.pack(anchor="w", pady=10)

write_seconds = ctk.CTkEntry(root)
write_seconds.pack(anchor="w", pady=5)

seconds_button = ctk.CTkButton(root, text="ну думаю сойдет", command=send_seconds)
seconds_button.pack(anchor="w", pady=5)

# Toggle state button
toggle_button = ctk.CTkButton(root, text="нельзя писать", command=toggle_state)
toggle_button.place(x=130, y=43)

# Nickname entry
nick_label = ctk.CTkLabel(root, text="введи тег (с @):")
nick_label.pack(anchor="w", pady=5)

nick_entry = ctk.CTkEntry(root)
nick_entry.pack(anchor="w", pady=5)

# File selection
select_button = ctk.CTkButton(root, text="выбрать пророчества", command=select_file)
select_button.pack(anchor="w")

# File name label
name_file = ctk.CTkLabel(root, text="ничо нет")
name_file.pack(anchor="w")

# Start button
start_button = ctk.CTkButton(root, text="я лелуш британский повелеваю начать!", state="disabled", command=start_sending)
start_button.place(x=150, y=130)

# Pause button
pause_button = ctk.CTkButton(root, text="F9", command=toggle_pause)
pause_button.place(x=260, y=170)

# Exit button
exit_button = ctk.CTkButton(root, text="close game)", command=exit_app)
exit_button.place(x=453, y=0)

# Send with tag checkbox
send_with_tag = ctk.BooleanVar(root)
send_with_tag.set(True)  # Default state is checked (with tag)

tag_checkbox = ctk.Checkbutton(root, text="с тегом", variable=send_with_tag)
tag_checkbox.pack(anchor="w", pady=5)

# Info button
info_button = ctk.CTkButton(text="гайдек", command=open_info)
info_button.pack(anchor="sw", expand=1)

# Status label
status_label = ctk.CTkLabel(root, text="нучо")
status_label.place(x=235, y=270)

# Handle close window event
root.protocol("WM_DELETE_WINDOW", exit_app)

try:
    root.mainloop()
except Exception as e:
    print(f"Ошибка при запуске: {e}")
