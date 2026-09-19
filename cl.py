import tkinter as tk
import random
from tkinter import messagebox

class MemePrankCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Rot Calculator 9000")
        self.root.geometry("380x540")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.display_var = tk.StringVar(value="Enter your low IQ math here...")
        
        # Sarcastic roasts for the prank victims
        self.roasts = [
            "My graphing calculator ancestors are crying right now.",
            "You really needed a computer for that? 💀",
            "Bro missed 1st grade math class.",
            "Error 404: Brain cells not found.",
            "Are you testing me or your own limits?",
            "Even a smart fridge could do this faster."
        ]
        
        self.create_widgets()

    def create_widgets(self):
        # Retro Matrix Display Screen
        display = tk.Entry(
            self.root, textvariable=self.display_var, font=("Courier New", 14, "bold"), 
            bd=10, bg="#121212", fg="#00ff00", justify="right"
        )
        display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="both", expand=True, padx=10, pady=5)

        buttons = [
            ('C', 1, 0, '#ff4757'), ('(', 1, 1, '#747d8c'), (')', 1, 2, '#747d8c'), ('/', 1, 3, '#ffa502'),
            ('7', 2, 0, '#ffffff'), ('8', 2, 1, '#ffffff'), ('9', 2, 2, '#ffffff'), ('*', 2, 3, '#ffa502'),
            ('4', 3, 0, '#ffffff'), ('5', 3, 1, '#ffffff'), ('6', 3, 2, '#ffffff'), ('-', 3, 3, '#ffa502'),
            ('1', 4, 0, '#ffffff'), ('2', 4, 1, '#ffffff'), ('3', 4, 2, '#ffffff'), ('+', 4, 3, '#ffa502'),
            ('0', 5, 0, '#ffffff'), ('.', 5, 1, '#ffffff'), ('=', 5, 2, '#2ed573')
        ]

        for i in range(6): button_frame.rowconfigure(i, weight=1)
        for j in range(4): button_frame.columnconfigure(j, weight=1)

        for text, row, col, bg_color in buttons:
            colspan = 2 if text == '=' else 1
            btn = tk.Button(
                button_frame, text=text, font=("Arial", 16, "bold"),
                bg=bg_color, fg="#2f3542" if bg_color == '#ffffff' else '#ffffff',
                activebackground="#ced6e0", command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif char == '=':
            cleaned_expr = self.expression.replace(" ", "")
            
            # 1. THE PRANK: Check for addition strings like 1+1, 2+2, etc.
            if '+' in cleaned_expr and cleaned_expr.replace('+', '').isdigit():
                numbers = cleaned_expr.split('+')
                # Concatenate them like strings instead of adding mathematically
                meme_result = "".join(numbers)
                self.display_var.set(f"{meme_result} (Duh!)")
                messagebox.showwarning(
                    "Sarcastic Math", 
                    f"Bro, obviously {self.expression} is {meme_result}.\nString concatenation, look it up. 🧠"
                )
                self.expression = meme_result
                return

            try:
                # Roast user randomly for easy math lengths
                if len(cleaned_expr) <= 3 and any(op in cleaned_expr for op in '+-*/'):
                    messagebox.showinfo("Seriously?", random.choice(self.roasts))

                # Standard calculation for everything else
                result = str(eval(self.expression))
                
                # 15% chance to just completely lie about the answer
                if random.random() < 0.15: 
                    wrong_result = str(float(result) + random.randint(5, 50))
                    self.display_var.set(f"{wrong_result} (Trust me bro)")
                    messagebox.showerror("Gaslight Mode", "Sample Message")
                    self.expression = wrong_result
                else:
                    self.display_var.set(result)
                    self.expression = result
                    
            except ZeroDivisionError:
                messagebox.showerror("Sample Message", "You divided by zero. The FBI has been notified. 🚨")
                self.clear_display()
            except Exception:
                messagebox.showerror("Brain Error", "Your math is so bad it broke my code.")
                self.clear_display()
        else:
            default_texts = ["0", "Enter your low IQ math here..."]
            if self.display_var.get() in default_texts and char not in './*+-':
                self.expression = char
            else:
                self.expression += str(char)
            self.display_var.set(self.expression)

    def clear_display(self):
        self.expression = ""
        self.display_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemePrankCalculator(root)
    root.mainloop()
