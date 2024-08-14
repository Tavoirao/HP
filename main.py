import tkinter as tk
from functions import show_login_screen, handle_login

# Executa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Login")
    root.configure(bg="black")
    root.state('zoomed')
    
    show_login_screen(root)
    
    root.mainloop()
