from tkinter import Tk, Label, Entry, Button, Text, END
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_text.delete("1.0", END)
            result_text.insert("1.0", "Please enter a valid positive number.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_text.delete("1.0", END)
        result_text.insert("1.0", password)
    except ValueError:
        result_text.delete("1.0", END)
        result_text.insert("1.0", "Please enter a numeric value for length.")

# Initialize the GUI application
app = Tk()
app.title("Random Password Generator")
app.geometry("400x300")

# Length label and entry
length_label = Label(app, text="Password Length:")
length_label.pack()
length_entry = Entry(app, width=20)
length_entry.pack()

# Generate button
generate_button = Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

# Result output area
result_label = Label(app, text="Generated Password:")
result_label.pack()
result_text = Text(app, height=2, width=40)
result_text.pack()

# Run the application
app.mainloop()
