import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tris")
        
        self.current_player = "X"
        self.board = [" "]*9
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
    def on_button_click(self, i, j):
        if self.board[i*3 + j] == " ":
            self.buttons[i][j].config(text=self.current_player)
            self.board[i*3 + j] = self.current_player
            
            if self.check_winner():
                messagebox.showinfo("Vittoria", f"Giocatore {self.current_player} ha vinto!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Pareggio", "La partita è finita in pareggio!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [" "]*9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

# Creazione della finestra principale
root = tk.Tk()

# Creazione dell'istanza del gioco
game = TicTacToe(root)

# Avvio dell'applicazione
root.mainloop()
