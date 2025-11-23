import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ COST MAPPING ------------------
sqft_cost_map = {
    "simple": 1500,
    "duplex": 2050,
    "luxury": 2600
}


# ------------------ LOGIC FUNCTION ------------------
def do_cost_estimate():
    try:
        area_val = float(area_input.get())
        floors_val = int(floor_input.get())
        h_type = house_choice.get()

        if floors_val <= 0:
            messagebox.showerror("Floor Error", "Number of floors must be at least 1.")
            return

        if not h_type:
            messagebox.showerror("Error", "Please pick a house style first.")
            return

        base_cost = sqft_cost_map[h_type]
        total_cost = area_val * base_cost * floors_val

        output_label.config(
            text=f"Estimated Cost for {floors_val} Floor(s): ₹{total_cost:,.2f}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# ------------------ WINDOW SETUP ------------------
main_win = tk.Tk()
main_win.title("🏠 Modern House Cost Estimator")
main_win.geometry("520x700")

# 🌟 NEW BACKGROUND → Light Brown
main_win.configure(bg="#D9C4A3")    # light brown shade

# ttk style (Modern Look)
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 12, "bold"),
    padding=10,
    relief="flat",
    background="#6D4C41",   # chocolate brown
    foreground="white"
)

style.map(
    "TButton",
    background=[("active", "#5D4037")]   # darker brown on hover
)

style.configure(
    "TCombobox",
    padding=8,
    font=("Segoe UI", 12)
)


# ------------------ MAIN TITLE ------------------
title_lbl = tk.Label(
    main_win,
    text="🏠 Modern House Cost Estimator",
    font=("Segoe UI", 20, "bold"),
    bg="#D9C4A3",      # match background
    fg="#3E2723"       # dark brown
)
title_lbl.pack(pady=20)


# ------------------ CARD FRAME ------------------
card = tk.Frame(
    main_win,
    bg="#FAF3E0",             # light cream-brown card
    bd=0,
    highlightbackground="#BFA888",   # soft border
    highlightthickness=2
)
card.pack(pady=10, padx=30, fill="both")


# ------------------ INPUT FIELDS ------------------
tk.Label(
    card,
    text="Enter Area (sqft)",
    font=("Segoe UI", 14),
    bg="#FAF3E0",
    fg="#4E342E"
).pack(pady=10)

area_input = tk.Entry(card, font=("Segoe UI", 12), bd=2, relief="groove", width=25)
area_input.pack()

tk.Label(
    card,
    text="Number of Floors",
    font=("Segoe UI", 14),
    bg="#FAF3E0",
    fg="#4E342E"
).pack(pady=10)

floor_input = tk.Entry(card, font=("Segoe UI", 12), bd=2, relief="groove", width=25)
floor_input.pack()


# ------------------ HOUSE TYPE ------------------
tk.Label(
    card,
    text="Select House Type",
    font=("Segoe UI", 14),
    bg="#FAF3E0",
    fg="#4E342E"
).pack(pady=15)

house_choice = tk.StringVar()

type_selector = ttk.Combobox(
    card,
    textvariable=house_choice,
    values=["simple", "duplex", "luxury"],
    font=("Segoe UI", 12),
    state="readonly",
    width=22
)
type_selector.pack()


# ------------------ BUTTON ------------------
ttk.Button(
    card,
    text="Estimate Cost",
    command=do_cost_estimate
).pack(pady=25)


# ------------------ OUTPUT ------------------
output_label = tk.Label(
    main_win,
    text="",
    font=("Segoe UI", 16, "bold"),
    bg="#D9C4A3",
    fg="#3E2723"
)
output_label.pack(pady=20)


main_win.mainloop()
