from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# --- Functions ---

def translate_text():
    text = input_text.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    # Get language codes from the dictionary
    source = languages[source_lang.get()]
    target = languages[target_lang.get()]

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")


def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)


def copy_text():
    # "end-1c" ensures we don't copy the extra invisible newline Tkinter adds
    text = output_text.get("1.0", "end-1c")

    if text.strip():
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied successfully")
    else:
        messagebox.showwarning("Warning", "Nothing to copy!")


# --- UI Setup ---

root = Tk()
root.title("Language Translation Tool")
root.geometry("750x600")
root.config(bg="lightblue")

# Language Dictionary
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml"
}

# Heading
Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
).pack(pady=15)

# Input Section
Label(root, text="Enter Text", font=("Arial", 12, "bold"), bg="lightblue").pack()
input_text = Text(root, height=7, width=70, font=("Arial", 12))
input_text.pack(pady=10)

# Language Selection Frame
frame = Frame(root, bg="lightblue")
frame.pack(pady=10)

# Source Language Dropdown
Label(frame, text="Source Language", font=("Arial", 11, "bold"), bg="lightblue").grid(row=0, column=0, padx=20)
source_lang = ttk.Combobox(frame, values=list(languages.keys()), width=20, state="readonly")
source_lang.grid(row=1, column=0)
source_lang.set("Auto Detect")

# Target Language Dropdown
Label(frame, text="Target Language", font=("Arial", 11, "bold"), bg="lightblue").grid(row=0, column=1, padx=20)
target_lang = ttk.Combobox(frame, values=list(languages.keys()), width=20, state="readonly")
target_lang.grid(row=1, column=1)
target_lang.set("Tamil")

# Action Buttons
Button(
    root,
    text="Translate",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    padx=20,
    command=translate_text
).pack(pady=10)

# Output Section
Label(root, text="Translated Text", font=("Arial", 12, "bold"), bg="lightblue").pack()
output_text = Text(root, height=7, width=70, font=("Arial", 12))
output_text.pack(pady=10)

# Bottom Button Frame
button_frame = Frame(root, bg="lightblue")
button_frame.pack(pady=10)

Button(
    button_frame,
    text="Copy",
    font=("Arial", 11, "bold"),
    bg="orange",
    fg="white",
    width=10,
    command=copy_text
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=10,
    command=clear_text
).grid(row=0, column=1, padx=10)

# Run Program
root.mainloop()
