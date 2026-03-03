import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# =========================
# VERBI
# =========================
verbi = {
    "andare": ("gehen", "ging", "ist gegangen"),
    "essere": ("sein", "war", "ist gewesen"),
    "avere": ("haben", "hatte", "hat gehabt"),
    "diventare": ("werden", "wurde", "ist geworden"),
    "venire": ("kommen", "kam", "ist gekommen"),
    "vedere": ("sehen", "sah", "hat gesehen"),
    "dare": ("geben", "gab", "hat gegeben"),
    "prendere": ("nehmen", "nahm", "hat genommen"),
    "mangiare": ("essen", "aß", "hat gegessen"),
    "bere": ("trinken", "trank", "hat getrunken"),
    "parlare": ("sprechen", "sprach", "hat gesprochen"),
    "leggere": ("lesen", "las", "hat gelesen"),
    "scrivere": ("schreiben", "schrieb", "hat geschrieben"),
    "dormire": ("schlafen", "schlief", "hat geschlafen"),
    "correre": ("laufen", "lief", "ist gelaufen"),
}

lista_verbi = list(verbi.keys())
random.shuffle(lista_verbi)

indice = 0
punti = 0
totale = len(lista_verbi)

# =========================
# FUNZIONI
# =========================
def aggiorna_progress():
    progress["value"] = (indice / totale) * 100
    punteggio_label.config(text=f"Punteggio: {punti}/{totale}")

def nuova_domanda():
    if indice < totale:
        verbo_label.config(text=f"{lista_verbi[indice]}")
        entry_inf.delete(0, tk.END)
        entry_praet.delete(0, tk.END)
        entry_perf.delete(0, tk.END)
        aggiorna_progress()
    else:
        mostra_risultato()

def controlla():
    global indice, punti

    italiano = lista_verbi[indice]
    infinito, praet, perf = verbi[italiano]

    if (entry_inf.get() == infinito and
        entry_praet.get() == praet and
        entry_perf.get() == perf):
        punti += 1
        risultato_label.config(text="✅ Corretto!", fg="#00cc66")
    else:
        risultato_label.config(
            text=f"❌ {infinito} | {praet} | {perf}",
            fg="#ff4444"
        )

    indice += 1
    root.after(1500, nuova_domanda)

def mostra_risultato():
    percentuale = (punti / totale) * 100

    if percentuale == 100:
        livello = "🏆 LEGGENDARIO"
    elif percentuale >= 80:
        livello = "🥇 ESPERTO"
    elif percentuale >= 60:
        livello = "🥈 BUONO"
    elif percentuale >= 40:
        livello = "🥉 SUFFICIENTE"
    else:
        livello = "📚 STUDIA DI PIÙ"

    messagebox.showinfo(
        "RISULTATO FINALE",
        f"Punteggio: {punti}/{totale}\n"
        f"Percentuale: {round(percentuale,2)}%\n\n"
        f"{livello}\n\n"
        "Creato da Astra (Alex) 🚀"
    )
    root.quit()

# =========================
# FINESTRA
# =========================
root = tk.Tk()
root.title("QUIZ VERBI TEDESCHI - Legendary Edition")
root.geometry("500x500")
root.config(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", thickness=20)

titolo = tk.Label(
    root,
    text="QUIZ VERBI TEDESCHI 🇩🇪",
    font=("Helvetica", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
titolo.pack(pady=20)

verbo_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e2f",
    fg="#00ccff"
)
verbo_label.pack(pady=10)

entry_inf = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry_inf.pack(pady=5)

entry_praet = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry_praet.pack(pady=5)

entry_perf = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry_perf.pack(pady=5)

btn = tk.Button(
    root,
    text="Controlla",
    font=("Helvetica", 14, "bold"),
    bg="#00ccff",
    fg="black",
    command=controlla
)
btn.pack(pady=20)

risultato_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    bg="#1e1e2f"
)
risultato_label.pack()

progress = ttk.Progressbar(root, length=350)
progress.pack(pady=20)

punteggio_label = tk.Label(
    root,
    text="Punteggio: 0/0",
    font=("Helvetica", 12),
    bg="#1e1e2f",
    fg="white"
)
punteggio_label.pack()

nuova_domanda()

root.mainloop()
