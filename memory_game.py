import tkinter as tk
import random
from functools import partial
from tkinter import messagebox

# -----------------------------
# Setup
# -----------------------------
root = tk.Tk()
root.title("🧠 Memory Matching Game")
root.resizable(False, False)

# Card symbols (you can change or use emojis)
symbols = ['🍎', '🍌', '🍇', '🍒', '🍉', '🍍', '🥝', '🍓']
symbols *= 2  # make pairs → total 16 symbols
random.shuffle(symbols)

# Variables
buttons = []
flipped = []
matched = []
moves = 0

# -----------------------------
# Functions
# -----------------------------
def flip_card(index):
    """Handles flipping cards and checking matches."""
    global moves

    # Ignore clicks on matched or already flipped cards
    if index in matched or index in flipped:
        return

    # Show the card
    buttons[index].config(text=symbols[index], state="disabled", disabledforeground="black")
    flipped.append(index)

    # If two cards are flipped, check for match after short delay
    if len(flipped) == 2:
        moves += 1
        root.after(700, check_match)

def check_match():
    """Check if two flipped cards match."""
    global flipped

    i1, i2 = flipped
    if symbols[i1] == symbols[i2]:
        matched.extend(flipped)
        buttons[i1].config(bg="lightgreen")
        buttons[i2].config(bg="lightgreen")
    else:
        # Flip them back
        buttons[i1].config(text="", state="normal")
        buttons[i2].config(text="", state="normal")

    flipped = []

    # Check if game is complete
    if len(matched) == len(symbols):
        messagebox.showinfo("🎉 You Win!", f"You matched all pairs in {moves} moves!")
        root.quit()  # end game cleanly

# -----------------------------
# Build GUI
# -----------------------------
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for i in range(16):
    btn = tk.Button(
        frame,
        text="",
        width=6,
        height=3,
        font=("Arial", 18, "bold"),
        command=partial(flip_card, i),
        bg="lightgray"
    )
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    buttons.append(btn)

# -----------------------------
# Run the Game
# -----------------------------
root.mainloop()
