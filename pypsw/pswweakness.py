import tkinter as tk
import string
import re

def check_psw_comuni(psw):
    with open('C:\\Users\\nicol\\desktop\\PyProg\\pypsw\\rockyou.txt', 'r', encoding='latin-1') as f:
        comune = f.read().splitlines()
    return psw in comune

def psw_strength(psw):
    score = 0
    length = len(psw)
    thresholds = [8, 12, 17, 20]
    result = [
        (lambda s: s < 4, "Weak"),
        (lambda s: s == 4, "Okay"),
        (lambda s: 4 <= s < 6, "Good"),
        (lambda s: s >= 6, "Strong")
    ]

    upper_case = any(c.isupper() for c in psw)
    lower_case = any(c.islower() for c in psw)
    special_char = any(c in string.punctuation for c in psw)
    num = any(c.isdigit() for c in psw)

    caratteri = [upper_case, lower_case, special_char, num]

    for threshold in thresholds:
        if length > threshold:
            score += 1

    score += sum(caratteri) - 1

    for condition, rating in result:
        if condition(score):
            return rating, score

def feedback(psw):
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    if check_psw_comuni(psw):
        result_text.insert(tk.END, "\u26a0\ufe0f Password trovata nella lista delle password comuni\n", 'warning')
        result_text.insert(tk.END, "Score: 0/7", 'danger')
    else:
        rating, score = psw_strength(psw)
        result_text.insert(tk.END, f"\ud83d\udd11 Password: {psw}\n", 'info')
        result_text.insert(tk.END, f"\ud83d\udd12 Rating: {rating}\n", 'info')
        result_text.insert(tk.END, f"\ud83d\udd22 Score: {score}/7\n", 'info')

    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=tk.DISABLED)

# Interfaccia grafica
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.config(bg="#2E3440")

# Label per il titolo
title_label = tk.Label(root, text="Controllo Sicurezza Password", bg="#2E3440", fg="#ECEFF4", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Label per l'inserimento della password
psw_label = tk.Label(root, text="Inserisci la password da verificare:", bg="#2E3440", fg="#D8DEE9", font=("Arial", 12))
psw_label.pack(pady=5)

# Entry per la password
psw_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30, bd=2, relief="groove")
psw_entry.pack(pady=5)

# Bottone per verificare la password
check_button = tk.Button(root, text="Verifica", command=lambda: feedback(psw_entry.get()), bg="#5E81AC", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3)
check_button.pack(pady=10)

# Text widget per mostrare il risultato
result_text = tk.Text(root, height=4, width=35, bg="#3B4252", fg="#ECEFF4", font=("Arial", 12), wrap="word", state=tk.DISABLED)
result_text.tag_configure('warning', foreground="#D08770", font=("Arial", 12, "bold"))
result_text.tag_configure('danger', foreground="#BF616A", font=("Arial", 12, "bold"))
result_text.tag_configure('info', foreground="#A3BE8C", font=("Arial", 12, "bold"))
result_text.tag_configure("center", justify='center')
result_text.pack(pady=10)

root.mainloop()
