import tkinter as tk
from datetime import date

# Set up the root window
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("PTSD Detection Entry Page")

# Color scheme and font settings
bg_color = "#f0f4f7"  # Light grayish blue for background
title_color = "#34495e"  # Darker shade for title
label_color = "#2c3e50"  # Dark gray for labels
button_color = "#3498db"  # Soft blue for buttons
placeholder_color = "grey"  # Color for placeholder text
font_title = ("Helvetica", 24, "bold")
font_label = ("Helvetica", 14)
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")

# Background configuration
root.configure(bg=bg_color)

# Title label with fading animation
title_label = tk.Label(root, text="Welcome to the PTSD Detection System", fg=title_color, font=font_title, bg=bg_color)
title_label.place(relx=0.5, rely=0.15, anchor="center")

def fade_in_text():
    for i in range(0, 11):
        root.after(i * 50, lambda c=i / 10: title_label.config(fg=f"#{int(c * 52):02x}{int(c * 58):02x}{int(c * 78):02x}"))

fade_in_text()

# Function to add placeholder to entry widgets
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg=placeholder_color)
    
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg=placeholder_color)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Label and entry fields for user information with placeholders
name_label = tk.Label(root, text="Name", font=font_label, bg=bg_color, fg=label_color).place(x=200,y=250)
year_label = tk.Label(root, text="Year(YYYY)", font=font_label, bg=bg_color, fg=label_color).place(x=200,y=300)
month_label = tk.Label(root, text="Month(MM)", font=font_label, bg=bg_color, fg=label_color).place(x=200,y=350)
day_label = tk.Label(root, text="Day(DD)", font=font_label, bg=bg_color, fg=label_color).place(x=200,y=400)

nameEntry = tk.Entry(root, font=font_entry, width=25, bd=2)
nameEntry.place(x=350,y=250)
yearEntry = tk.Entry(root, font=font_entry, width=25, bd=2)
yearEntry.place(x=350,y=300)
monthEntry = tk.Entry(root, font=font_entry, width=25, bd=2)
monthEntry.place(x=350,y=350)
dayEntry = tk.Entry(root, font=font_entry, width=25, bd=2)
dayEntry.place(x=350,y=400)



# Function to calculate age and display
result_label = tk.Label(root, font=("Helvetica", 14), bg=bg_color, fg=label_color)
def age_calc():
    try:
        today = date.today()
        birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        result_label.config(text=f"{nameEntry.get()}, your age is {age}")
        result_label.place(relx=0.5, rely=0.85, anchor="center")
    except ValueError:
        result_label.config(text="Please enter a valid date.")
        result_label.place(relx=0.5, rely=0.85, anchor="center")

# Submit button with hover effect
def on_enter(e):
    submit_button.config(bg="skyblue", width=14)

def on_leave(e):
    submit_button.config(bg=button_color, width=12)

submit_button = tk.Button(root, text="Submit", font=font_button, bg=button_color, fg="white", command=age_calc, width=12)
submit_button.place(relx=0.5, rely=0.75, anchor="center")
submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)

root.mainloop()
