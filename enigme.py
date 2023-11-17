import tkinter as tk
from threading import Thread
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk

def afficher_video():
    chemin_video = "ressources/desert.mp4"  # Remplacez par le chemin de votre vidéo
    clip = VideoFileClip(chemin_video)
    # Redimensionner la vidéo à la nouvelle largeur et hauteur
    nouvelle_largeur = 640
    nouvelle_hauteur = 480
    clip = clip.resize(width=nouvelle_largeur, height=nouvelle_hauteur)

    def boucle_video():
        while True:
            clip.preview()
    # Lancer la boucle dans un thread
    thread_boucle = Thread(target=boucle_video)
    thread_boucle.start()

def verifier_nombre(numero, entree, message_label):
    global message_label3, message_label1, message_label2
    try:
        nombre_entre = float(entree.get())
        if nombre_entre == numero:
            message_label.config(text="Succès!")
        else:
            message_label.config(text="Échec!")
        if (message_label1["text"] == 'Succès!' and message_label2["text"] == 'Succès!'):
            message_label3.config(text="Coordonnées GPS débloquées", fg='green')
            afficher_video()
    except ValueError:
        message_label.config(text="Veuillez entrer un nombre valide.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Test des nombres")

# Chargement des images (remplacez les noms de fichiers par vos propres images)
image_parchemin_1 = Image.open("ressources/parchemin 1.png")
largeur_image = 400  # Définissez la largeur souhaitée
hauteur_image = (largeur_image * image_parchemin_1.height) // image_parchemin_1.width  # Calculez la hauteur proportionnellement
image_parchemin_1 = image_parchemin_1.resize((largeur_image, hauteur_image), Image.ANTIALIAS)  # Redimensionnez l'image

image_parchemin_2 = Image.open("ressources/parchemin 2.png")
largeur_image = 400  # Définissez la largeur souhaitée
hauteur_image = (largeur_image * image_parchemin_2.height) // image_parchemin_2.width  # Calculez la hauteur proportionnellement
image_parchemin_2 = image_parchemin_2.resize((largeur_image, hauteur_image), Image.ANTIALIAS)  # Redimensionnez l'image

image1 = ImageTk.PhotoImage(image_parchemin_1)
image2 = ImageTk.PhotoImage(image_parchemin_2)

# Création des étiquettes pour afficher les images
label_image1 = tk.Label(fenetre, image=image1)
label_image2 = tk.Label(fenetre, image=image2)

# Positionnement des étiquettes sur la même ligne avec un espace entre elles
label_image1.grid(row=0, column=0, padx=(10, 0))
label_image2.grid(row=0, column=2, padx=(0, 10))

# Ajout des champs de saisie
entree1 = tk.Entry(fenetre)
entree2 = tk.Entry(fenetre)

entree1.grid(row=1, column=0, pady=(10, 0))
entree2.grid(row=1, column=2, pady=(10, 0))

# Ajout des boutons pour vérifier les nombres
bouton1 = tk.Button(fenetre, text="Vérifier", command=lambda: verifier_nombre(29.825402027423607, entree1, message_label1))
bouton2 = tk.Button(fenetre, text="Vérifier", command=lambda: verifier_nombre(-5.722615680620322, entree2, message_label2))

bouton1.grid(row=2, column=0, pady=(0, 10))
bouton2.grid(row=2, column=2, pady=(0, 10))

# Ajout des étiquettes pour afficher les messages de succès/échec
message_label1 = tk.Label(fenetre, text="")
message_label2 = tk.Label(fenetre, text="")
message_label3 = tk.Label(fenetre, text="")

message_label3.grid(row=3, column=1)
message_label1.grid(row=3, column=0)
message_label2.grid(row=3, column=2)

# Lancement de la boucle principale
fenetre.mainloop()
