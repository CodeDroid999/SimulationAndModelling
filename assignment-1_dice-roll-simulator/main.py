import tkinter as tk
from tkinter import ttk
import random

# Unicode characters for dice faces (⚀ to ⚅)
DICE_UNICODE = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


def roll_dice():
    """Simulate rolling a six-sided die using random.random()."""
    value = random.random()
    if 0 <= value < 1/6:
        return 1
    elif 1/6 <= value < 2/6:
        return 2
    elif 2/6 <= value < 3/6:
        return 3
    elif 3/6 <= value < 4/6:
        return 4
    elif 4/6 <= value < 5/6:
        return 5
    else:
        return 6


class DiceSimulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roll Simulator")

        # Configure grid layout
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        # Left frame for dice display
        self.left_frame = ttk.Frame(self.master, padding="10")
        self.left_frame.grid(row=0, column=0, sticky="NSEW")

        self.dice_label = ttk.Label(
            self.left_frame, text='', font=("Helvetica", 100))
        self.dice_label.pack(pady=20)

        # Right frame for frequency table
        self.right_frame = ttk.Frame(self.master, padding="10")
        self.right_frame.grid(row=0, column=1, sticky="NSEW")

        self.tree = ttk.Treeview(self.right_frame, columns=(
            'Face', 'Frequency', 'Percentage'), show='headings', height=7)
        self.tree.heading('Face', text='Face')
        self.tree.heading('Frequency', text='Frequency')
        self.tree.heading('Percentage', text='Percentage')
        self.tree.column('Face', anchor='center')
        self.tree.column('Frequency', anchor='center')
        self.tree.column('Percentage', anchor='center')
        self.tree.pack()

        # Roll button
        self.roll_button = ttk.Button(
            self.master, text="Roll Dice", command=self.run_simulation)
        self.roll_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Initial simulation
        self.run_simulation()

    def run_simulation(self):
        rolls = 1000
        face_counts = {i: 0 for i in range(1, 7)}

        # Simulate dice rolls
        for _ in range(rolls):
            face = roll_dice()
            face_counts[face] += 1

        # Update dice display with the last roll
        last_face = face
        self.dice_label.config(text=DICE_UNICODE[last_face - 1])

        # Clear existing data in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new data into the treeview
        for face in range(1, 7):
            count = face_counts[face]
            percentage = (count / rolls) * 100
            self.tree.insert('', 'end', values=(
                face, count, f"{percentage:.1f}%"))

        # Insert total row
        total_frequency = sum(face_counts.values())
        total_percentage = (total_frequency / rolls) * 100
        self.tree.insert('', 'end', values=(
            'Total', total_frequency, f"{total_percentage:.1f}%"))

        # Print results to terminal
        print("Face  Frequency   Percentage")
        for face, count in face_counts.items():
            percentage = (count / rolls) * 100
            print(f"{face:4}   {count:9}   {percentage:.1f}%")
            print("___________________________________ \n")
            print(f"Total  {total_frequency:9}   {total_percentage:.1f}%\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulatorGUI(root)
    root.mainloop()
