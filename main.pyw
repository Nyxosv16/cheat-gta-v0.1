import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pyautogui
import time
import keyboard

commandes_effectuees = []

def afficher_commande_jeu(code, duree=None):
    commande = f"Commande activée : {code}"
    if duree:
        if duree == "infini":
            commande += " (∞)"
        else:
            commande += f" ({duree}s)"
    keyboard.write(commande)
    keyboard.press_and_release('enter')
    commandes_effectuees.append(commande)

def activer_triche(code, duree=None):
    print(f"Code de triche activé : {code}")
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)
    
    pyautogui.press('t')  # Ouvrir le chat/console dans le jeu
    time.sleep(0.5)
    
    for chiffre in code:
        if chiffre != '-':
            pyautogui.press(chiffre)
            time.sleep(0.1)
    
    pyautogui.press('enter')
    time.sleep(0.5)
    
    afficher_commande_jeu(code, duree)
    
    pyautogui.press('backspace')
    
    pyautogui.hotkey('alt', 'tab')

def ouvrir_page_info():
    fenetre_info = ctk.CTkToplevel()
    fenetre_info.title("À propos")
    fenetre_info.geometry("500x400")
    fenetre_info.configure(bg_color="#2C2F33")
    
    titre = ctk.CTkLabel(fenetre_info, text="GTA CHEAT PANNEL", 
                         font=("Roboto", 28, "bold"), text_color="#7289DA")
    titre.pack(pady=25)
    
    cadre_info = ctk.CTkFrame(fenetre_info, corner_radius=15)
    cadre_info.pack(padx=25, pady=15, fill="both", expand=True)
    
    texte_info = ctk.CTkTextbox(cadre_info, width=450, height=250, 
                                font=("Roboto", 14), text_color="#FFFFFF")
    texte_info.pack(padx=15, pady=15, fill="both", expand=True)
    
    info_contenu = """
    🌐 Site web : https://guns.lol/killnet
    📂 GitHub : https://guns.lol/killnet
    🎮 Discord : nyxosv19
    🚀 Serveur Discord : https://discord.gg/kVSckV43Fq
    """
    
    texte_info.insert("1.0", info_contenu)
    texte_info.configure(state="disabled")
    
    bouton_fermer = ctk.CTkButton(fenetre_info, text="Fermer", 
                                  command=fenetre_info.destroy,
                                  fg_color="#7289DA", hover_color="#5B6EAE",
                                  font=("Roboto", 14, "bold"))
    bouton_fermer.pack(pady=20)

def afficher_commandes_effectuees():
    fenetre_commandes = ctk.CTkToplevel()
    fenetre_commandes.title("Commandes effectuées")
    fenetre_commandes.geometry("800x600")
    fenetre_commandes.configure(bg_color="#2C2F33")
    
    titre = ctk.CTkLabel(fenetre_commandes, text="Liste des commandes effectuées", 
                         font=("Roboto", 28, "bold"), text_color="#7289DA")
    titre.pack(pady=25)
    
    cadre_commandes = ctk.CTkScrollableFrame(fenetre_commandes, corner_radius=15)
    cadre_commandes.pack(padx=25, pady=15, fill="both", expand=True)
    
    for commande in commandes_effectuees:
        ctk.CTkLabel(cadre_commandes, text=commande, font=("Roboto", 14), text_color="#FFFFFF").pack(anchor="w", pady=2)
    
    bouton_fermer = ctk.CTkButton(fenetre_commandes, text="Fermer", 
                                  command=fenetre_commandes.destroy,
                                  fg_color="#7289DA", hover_color="#5B6EAE",
                                  font=("Roboto", 14, "bold"))
    bouton_fermer.pack(pady=20)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

fenetre = ctk.CTk()
fenetre.title("GTA CHEAT PANNEL")
fenetre.geometry("1000x700")

titre = ctk.CTkButton(fenetre, text="GTA CHEAT PANNEL", 
                      font=("Arial", 36, "bold"), 
                      command=ouvrir_page_info,
                      fg_color="#7289DA", 
                      hover_color="#5B6EAE")
titre.pack(pady=30)

bouton_commandes_effectuees = ctk.CTkButton(fenetre, text="Afficher les commandes effectuées", 
                                        command=afficher_commandes_effectuees,
                                        fg_color="#4CAF50", 
                                        hover_color="#45a049",
                                        font=("Roboto", 16, "bold"))
bouton_commandes_effectuees.pack(pady=10)

frame_principal = ctk.CTkScrollableFrame(fenetre, corner_radius=20)
frame_principal.pack(expand=True, fill="both", padx=40, pady=40)

notebook = ctk.CTkTabview(frame_principal)
notebook.pack(expand=True, fill="both", padx=30, pady=30)

categories = {
    "Armes": {
        "Obtenir des armes": ("1-999-866-587", "TOOLUP", None),
        "Coups de poing explosifs": ("1-999-4684-2637", "HOTHANDS", 300),
        "Balles qui explosent": ("1-999-444-439", "HIGHEX", 300),
        "Visée au ralenti": ("1-999-332-3393", "DEADEYE", 300),
        "Balles enflammées": ("1-999-462-363-4279", "INCENDIARY", 300),
        "Munitions infinies": ("1-999-444-0000", "LEADME", "infini"),
        "Armes de niveau 1": ("1-999-866-587", "TOOLUP", None),
        "Armes de niveau 2": ("1-999-866-587", "FULLY LOADED", None),
        "Armes de niveau 3": ("1-999-866-587", "NUTTERTOOLS", None),
        "Armes de niveau 4": ("1-999-866-587", "PROFESSIONALTOOLS", None)
    },
    "Police": {
        "Diminuer l'indice de recherche": ("1-999-5299-3787", "LAWYERUP", None),
        "Augmenter l'indice de recherche": ("1-999-3844-8483", "FUGITIVE", None),
        "Supprimer l'indice de recherche": ("1-999-5299-3787", "CLEANSED", None),
        "Indice de recherche maximum": ("1-999-3844-8483", "TURNUPTHEHEAT", None),
        "Désactiver la police": ("1-999-5299-3787", "NOPOLICEPLEASE", 300)
    },
    "Véhicules": {
        "Faire déraper les voitures": ("1-999-766-9329", "SNOWDAY", 300),
        "Stunt Plane (avion de voltige)": ("1-999-2276-78676", "BARNSTORM", None),
        "Duster (avion agricole)": ("1-999-359-77729", "FLYSPRAY", None),
        "Buzzard (hélicoptère)": ("1-999-289-9633", "BUZZOFF", None),
        "Comet (voiture sportive)": ("1-999-266-38", "COMET", None),
        "Rapid GT (voiture de course)": ("1-999-727-4348", "RAPIDGT", None),
        "Sanchez (motocross)": ("1-999-633-7623", "OFFROAD", None),
        "Trashmaster (camion poubelle)": ("1-999-872-7433", "TRASHED", None),
        "Stretch (limousine)": ("1-999-846-39663", "VINEWOOD", None),
        "Caddie de golf": ("1-999-465-3461", "HOLEIN1", None),
        "PCJ 600 (moto de course)": ("1-999-762-538", "ROCKET", None),
        "BMX": ("1-999-226-348", "BANDIT", None),
        "Duke O'Death": ("1-999-332-84227", "DEATHCAR", None),
        "Hydravion Dodo": ("1-999-398-4628", "EXTINCT", None),
        "Submersible Kraken": ("1-999-282-2537", "BUBBLES", None),
        "Tank Rhino": ("1-999-872-7496", "TANKME", None),
        "Jetpack": ("1-999-2276-78255", "ROCKETMAN", None),
        "Voiture de sport rapide": ("1-999-227-678-676", "COMET", None),
        "Moto de course": ("1-999-762-538", "ROCKET", None),
        "Hélicoptère d'attaque": ("1-999-289-9633", "BUZZOFF", None),
        "Avion de chasse": ("1-999-872-433", "FLYINGTANK", None),
        "Bateau rapide": ("1-999-228-2463", "SEASHARK", None),
        "Véhicule amphibie": ("1-999-227-678-676", "SEAWAYS", None)
    },
    "Météo": {
        "Changer le temps": ("1-999-625-348-7246", "MAKEITRAIN", None),
        "Temps ensoleillé": ("1-999-625-348-7246", "CLEAR", None),
        "Temps orageux": ("1-999-625-348-7246", "THUNDER", None),
        "Temps neigeux": ("1-999-625-348-7246", "SNOWFALL", None),
        "Temps brumeux": ("1-999-625-348-7246", "FOGGY", None),
        "Temps pluvieux": ("1-999-625-348-7246", "RAINY", None),
        "Temps nuageux": ("1-999-625-348-7246", "OVERCAST", None),
        "Temps de tempête de sable": ("1-999-625-348-7246", "SANDSTORM", None)
    },
    "Personnages": {
        "Recharger la santé et l'armure": ("1-999-887-853", "TURTLE", None),
        "Invincibilité pendant 5 minutes": ("1-999-724-654-5537", "PAINKILLER", 300),
        "Recharger la compétence unique": ("1-999-769-3787", "POWERUP", None),
        "Courir plus vite": ("1-999-228-2463", "CATCHME", 300),
        "Nager plus vite": ("1-999-468-44557", "GOTGILLS", 300),
        "Super force": ("1-999-467-8648", "BUFFMEUP", 300),
        "Mode fantôme": ("1-999-444-0916", "VANISH", 300),
        "Santé au maximum": ("1-999-887-853", "ASPIRINE", None),
        "Armure au maximum": ("1-999-887-853", "PRECIOUSPROTECTION", None),
        "Mode Dieu": ("1-999-724-654-5537", "GODMODE", "infini"),
        "Respiration infinie": ("1-999-468-44557", "LUNGCAPACITY", "infini")
    },
    "Divers": {
        "Mode ivrogne": ("1-999-547-867", "LIQUOR", 300),
        "Ralentir le jeu": ("1-999-756-966", "SLOWMO", 30),
        "Obtenir un parachute": ("1-999-759-3483", "SKYDIVE", None),
        "Skyfall": ("1-999-759-3255", "SKYFALL", None),
        "Gravité lunaire": ("1-999-356-2837", "FLOATER", 300),
        "Super saut": ("1-999-467-8648", "HOPTOIT", 300),
        "Mode Réalisateur": ("1-999-578-25368", "LSTALENT", None),
        "Argent infini": ("1-999-887-853", "RICHMAN", "infini"),
        "Téléportation aléatoire": ("1-999-462-363-4279", "HOUDINI", None),
        "Monde en feu": ("1-999-462-363-4279", "HELLFIRE", 300),
        "Accélérer le temps": ("1-999-756-966", "TIMESPEED", 30),
        "Ralentir le temps": ("1-999-756-966", "SLOWMOTION", 30),
        "Augmenter le niveau de recherche": ("1-999-3844-8483", "TURNUPTHEHEAT", None),
        "Diminuer le niveau de recherche": ("1-999-5299-3787", "LAWYERUP", None),
        "Changer l'apparence du personnage": ("1-999-8265-87", "MAKEOVER", None),
        "Mode Mayhem": ("1-999-444-439", "MAYHEM", 300),
        "Spawn un hélicoptère": ("1-999-359-77729", "BUZZOFF", None),
        "Spawn un jet": ("1-999-2276-78676", "FLYSPRAY", None),
        "Spawn un bateau": ("1-999-398-4628", "SEAWAYS", None),
        "Spawn une voiture de luxe": ("1-999-227-678-676", "IWANTITPAINTEDBLACK", None)
    }
}

for categorie, codes in categories.items():
    tab = notebook.add(categorie)
    
    for nom, (code_tel, code_lettres, duree) in codes.items():
        frame_code = ctk.CTkFrame(tab, corner_radius=10)
        frame_code.pack(pady=10, padx=20, fill=tk.X)
        
        label = ctk.CTkLabel(frame_code, text=nom, width=300, anchor="w", font=("Roboto", 16, "bold"))
        label.pack(side=tk.LEFT, padx=10, pady=5)
        
        bouton_tel = ctk.CTkButton(frame_code, text=code_tel, command=lambda c=code_tel, d=duree: activer_triche(c, d), width=160, font=("Roboto", 14), fg_color="#4CAF50", hover_color="#45a049")
        bouton_tel.pack(side=tk.LEFT, padx=10)
        
        bouton_lettres = ctk.CTkButton(frame_code, text=code_lettres, command=lambda c=code_lettres, d=duree: activer_triche(c, d), width=160, font=("Roboto", 14), fg_color="#2196F3", hover_color="#1976D2")
        bouton_lettres.pack(side=tk.LEFT, padx=10)

fenetre.mainloop()
