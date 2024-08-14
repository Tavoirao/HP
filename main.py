import tkinter as tk
from functions import show_admin_menu, show_visitor_menu, load_users

def handle_login(username, password, root):
    users = load_users()
    username = username.lower()

    if username == "hp" and password == "HP@33993399":
        show_admin_menu(root, username)
    elif username in users["usuarios"] and users["usuarios"][username]["password"] == password:
        show_visitor_menu(root, username)
    else:
        tk.messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Executa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Login")
    root.configure(bg="black")
    root.state('zoomed')
    
    from functions import show_login_screen
    show_login_screen(root)
    
    root.mainloop()
