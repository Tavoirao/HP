import tkinter as tk
from tkinter import messagebox
import json

# Funções para carregar e salvar dados de usuários
def load_users():
    try:
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"usuarios": {}}
    except json.JSONDecodeError:
        return {"usuarios": {}}

def save_users(users):
    with open('usuarios.json', 'w') as file:
        json.dump(users, file, indent=4)

# Funções para carregar e salvar dados de produtos
def load_products():
    try:
        with open('produtos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"produtos": {}}
    except json.JSONDecodeError:
        return {"produtos": {}}

def save_products(products):
    with open('produtos.json', 'w') as file:
        json.dump(products, file, indent=4)

# Funções do administrador
def show_admin_menu(root, username):
    for widget in root.winfo_children():
        widget.destroy()

    admin_frame = tk.Frame(root, bg="black")
    admin_frame.pack(expand=True)

    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}

    welcome_label = tk.Label(admin_frame, text=f"Bem Vindo {username.capitalize()}", **label_style)
    welcome_label.pack(pady=10)

    create_user_button = tk.Button(admin_frame, text="Criar Usuário", command=lambda: create_user(root), **button_style)
    create_user_button.pack(pady=10)

    delete_user_button = tk.Button(admin_frame, text="Apagar Usuário", command=lambda: delete_user(root), **button_style)
    delete_user_button.pack(pady=10)

    create_product_button = tk.Button(admin_frame, text="Criar Produto", command=lambda: create_product(root), **button_style)
    create_product_button.pack(pady=10)

    delete_product_button = tk.Button(admin_frame, text="Remover Produto", command=lambda: delete_product(root), **button_style)
    delete_product_button.pack(pady=10)

    logout_button = tk.Button(admin_frame, text="Logout", command=lambda: reset_to_login(root), **button_style)
    logout_button.pack(pady=10)

    exit_button = tk.Button(admin_frame, text="Sair", command=handle_exit, **button_style)
    exit_button.pack(pady=10)

def create_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    create_user_frame = tk.Frame(root, bg="black")
    create_user_frame.pack(expand=True)

    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    entry_style = {"font": ("Helvetica", 24), "bg": "white", "fg": "black"}
    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}

    user_label = tk.Label(create_user_frame, text="Novo Usuário", **label_style)
    user_label.pack(pady=10)
    user_entry = tk.Entry(create_user_frame, **entry_style)
    user_entry.pack(pady=10)

    pass_label = tk.Label(create_user_frame, text="Senha", **label_style)
    pass_label.pack(pady=10)
    pass_entry = tk.Entry(create_user_frame, show="*", **entry_style)
    pass_entry.pack(pady=10)

    def save_new_user():
        new_user = user_entry.get().strip().lower()
        new_pass = pass_entry.get().strip()

        if not new_user or not new_pass:
            messagebox.showerror("Erro", "Usuário e senha não podem estar vazios.")
            return
        
        users = load_users()
        
        if new_user in users["usuarios"]:
            messagebox.showerror("Erro", f"Usuário '{new_user}' já existe!")
        else:
            users["usuarios"][new_user] = {"username": new_user, "password": new_pass}
            save_users(users)
            messagebox.showinfo("Sucesso", f"Usuário '{new_user}' criado com sucesso!")
            show_admin_menu(root, "HP")

    save_button = tk.Button(create_user_frame, text="Salvar", command=save_new_user, **button_style)
    save_button.pack(pady=10)

    back_button = tk.Button(create_user_frame, text="Voltar", command=lambda: show_admin_menu(root, "HP"), **button_style)
    back_button.pack(pady=10)

def delete_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    delete_user_frame = tk.Frame(root, bg="black")
    delete_user_frame.pack(expand=True)

    users = load_users()
    user_list = list(users["usuarios"].keys())

    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}

    if not user_list:
        no_user_label = tk.Label(delete_user_frame, text="Nenhum usuário disponível", **label_style)
        no_user_label.pack(pady=10)
        back_button = tk.Button(delete_user_frame, text="Voltar", command=lambda: show_admin_menu(root, "HP"), **button_style)
        back_button.pack(pady=10)
        return

    user_label = tk.Label(delete_user_frame, text="Escolha um usuário para apagar", **label_style)
    user_label.pack(pady=10)

    user_var = tk.StringVar(delete_user_frame)
    user_var.set(user_list[0])

    user_dropdown = tk.OptionMenu(delete_user_frame, user_var, *user_list)
    user_dropdown.config(bg="white", font=("Helvetica", 24), fg="black")
    user_dropdown.pack(pady=10)

    def confirm_delete():
        selected_user = user_var.get()
        if selected_user in users["usuarios"]:
            del users["usuarios"][selected_user]
            save_users(users)
            messagebox.showinfo("Sucesso", f"Usuário {selected_user} apagado com sucesso!")
            show_admin_menu(root, "HP")

    delete_button = tk.Button(delete_user_frame, text="Apagar", command=confirm_delete, **button_style)
    delete_button.pack(pady=10)

    back_button = tk.Button(delete_user_frame, text="Voltar", command=lambda: show_admin_menu(root, "HP"), **button_style)
    back_button.pack(pady=10)

def create_product(root):
    for widget in root.winfo_children():
        widget.destroy()

    create_product_frame = tk.Frame(root, bg="black")
    create_product_frame.pack(expand=True)

    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    entry_style = {"font": ("Helvetica", 24), "bg": "white", "fg": "black"}
    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}

    name_label = tk.Label(create_product_frame, text="Nome do Produto", **label_style)
    name_label.pack(pady=10)
    name_entry = tk.Entry(create_product_frame, **entry_style)
    name_entry.pack(pady=10)

    inches_label = tk.Label(create_product_frame, text="Polegadas", **label_style)
    inches_label.pack(pady=10)
    inches_var = tk.StringVar()
    inches_var.set("6")
    inches_options = ["6", "8", "10", "12", "15", "18", "Driver", "Tweeter"]
    inches_dropdown = tk.OptionMenu(create_product_frame, inches_var, *inches_options)
    inches_dropdown.config(bg="white", font=("Helvetica", 24), fg="black")
    inches_dropdown.pack(pady=10)

    ohms_label = tk.Label(create_product_frame, text="Ohms", **label_style)
    ohms_label.pack(pady=10)
    ohms_var = tk.StringVar()
    ohms_var.set("2")
    ohms_options = ["2", "4", "8"]
    ohms_dropdown = tk.OptionMenu(create_product_frame, ohms_var, *ohms_options)
    ohms_dropdown.config(bg="white", font=("Helvetica", 24), fg="black")
    ohms_dropdown.pack(pady=10)

    def save_new_product():
        product_name = name_entry.get().strip()
        inches = inches_var.get()
        ohms = ohms_var.get()

        if not product_name:
            messagebox.showerror("Erro", "O nome do produto não pode estar vazio.")
            return

        products = load_products()
        
        product_key = f"{product_name} - {inches}\" - {ohms}Ω"

        if product_key in products["produtos"]:
            messagebox.showerror("Erro", "Produto já existe!")
        else:
            products["produtos"][product_key] = {"nome": product_name, "polegadas": inches, "ohms": ohms}
            save_products(products)
            messagebox.showinfo("Sucesso", f"Produto '{product_key}' criado com sucesso!")
            show_admin_menu(root, "HP")

    save_button = tk.Button(create_product_frame, text="Salvar", command=save_new_product, **button_style)
    save_button.pack(pady=10)

    back_button = tk.Button(create_product_frame, text="Voltar", command=lambda: show_admin_menu(root, "HP"), **button_style)
    back_button.pack(pady=10)

def delete_product(root):
    for widget in root.winfo_children():
        widget.destroy()

    delete_product_frame = tk.Frame(root, bg="black")
    delete_product_frame.pack(expand=True)

    products = load_products()
    product_list = list(products.get("produtos", {}).keys())

    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}

    if not product_list:
        no_product_label = tk.Label(delete_product_frame, text="Nenhum produto disponível", **label_style)
        no_product_label.pack(pady=10)
        back_button = tk.Button(delete_product_frame, text="Voltar", command=lambda: show_admin_menu(root, "HP"), **button_style)
        back_button.pack(pady=10)
        return

    product_label = tk.Label(delete_product_frame, text="Escolha um produto para apagar", **label_style)
    product_label.pack(pady=10)

    product_var = tk.StringVar(delete_product_frame)
    product_var.set(product_list[0])

    product_dropdown = tk.OptionMenu(delete_product_frame, product_var, *product_list)
    product_dropdown.config(bg="white", font=("Helvetica", 24), fg="black")
    product_dropdown.pack(pady=10)

    def confirm_delete_product():
        selected_product = product_var.get()
        if selected_product in products["produtos"]:
            del products["produtos"][selected_product]
            save_products(products)
            messagebox.showinfo("Sucesso", f"Produto '{selected_product}' apagado com sucesso!")
            show_admin_menu(root, "HP")

    delete_button = tk.Button(delete_product_frame, text="Apagar", command=confirm_delete_product, **button_style)
    delete_button.pack(pady=10)

    back_button = tk.Button(delete_product_frame, text="Voltar", command=lambda: show_admin_menu(root, "HP"), **button_style)
    back_button.pack(pady=10)

# Funções do visitante
def show_visitor_menu(root, username):
    for widget in root.winfo_children():
        widget.destroy()

    visitor_frame = tk.Frame(root, bg="black")
    visitor_frame.pack(expand=True)

    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}

    welcome_label = tk.Label(visitor_frame, text=f"Olá {username.capitalize()}", **label_style)
    welcome_label.pack(pady=10)

    logout_button = tk.Button(visitor_frame, text="Logout", command=lambda: reset_to_login(root), **button_style)
    logout_button.pack(pady=10)

    exit_button = tk.Button(visitor_frame, text="Sair", command=handle_exit, **button_style)
    exit_button.pack(pady=10)

def show_login_screen(root):
    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(expand=True)

    button_style = {"bg": "red", "fg": "white", "font": ("Helvetica", 24), "width": 20, "height": 2}
    label_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 24)}
    entry_style = {"font": ("Helvetica", 24), "bg": "white", "fg": "black"}

    user_label = tk.Label(main_frame, text="Usuário", **label_style)
    user_label.pack(pady=10)
    user_entry = tk.Entry(main_frame, **entry_style)
    user_entry.pack(pady=10)

    pass_label = tk.Label(main_frame, text="Senha", **label_style)
    pass_label.pack(pady=10)
    pass_entry = tk.Entry(main_frame, show="*", **entry_style)
    pass_entry.pack(pady=10)

    login_button = tk.Button(main_frame, text="Login", command=lambda: handle_login(user_entry.get(), pass_entry.get(), root), **button_style)
    login_button.pack(pady=10)

    exit_button = tk.Button(main_frame, text="Sair", command=handle_exit, **button_style)
    exit_button.pack(pady=10)

def reset_to_login(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    show_login_screen(root)

def handle_exit():
    exit()
