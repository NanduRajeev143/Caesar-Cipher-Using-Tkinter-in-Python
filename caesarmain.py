from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher():
    start_text = input_text.get().lower()
    shift_amount = int(shift_entry.get()) % 26
    cipher_direction = direction_var.get()

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char

    result_label.config(text=f"Result: {end_text}")


window = Tk()
window.title("Caesar Cipher")
window.config(padx=20, pady=20)
window.configure(bg="#3498db")  # Set the background color to a shade of blue


logo_label = Label(window, text=logo, font=("Courier", 10), bg="#3498db", fg="white")  # Set text color to white for better visibility
logo_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))  # Added pady for spacing


direction_var = StringVar()
direction_var.set("encode")
direction_label = Label(window, text="Direction:", bg="#3498db", fg="red")  # Set text color to red
direction_label.grid(row=1, column=0)
direction_menu = OptionMenu(window, direction_var, "encode", "decode")
direction_menu.grid(row=1, column=1, columnspan=2)


input_label = Label(window, text="Text:", bg="#3498db", fg="black")  # Set text color to black
input_label.grid(row=2, column=0)
input_text = Entry(window, width=30)
input_text.grid(row=2, column=1, columnspan=2)


shift_label = Label(window, text="Shift:", bg="#3498db", fg="red")  # Set text color to red
shift_label.grid(row=3, column=0)
shift_entry = Entry(window, width=10)
shift_entry.grid(row=3, column=1)


result_label = Label(window, text="Result:", bg="#3498db", fg="black")  # Set text color to black
result_label.grid(row=4, column=0, columnspan=3)


encrypt_button = Button(window, text="Encrypt/Decrypt", command=caesar_cipher, bg="#2980b9", fg="white")  # Set button color to a darker blue
encrypt_button.grid(row=5, column=0, columnspan=3)


window.mainloop()
