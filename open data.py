import csv
import matplotlib.pyplot as plt

# Initialiser les variables pour chaque colonne pour pouvoir les incrémenter 
nb_vote_blanc = 0
nb_vote_nul = 0
nb_exprime = 0
arthaud_nathalie = 0
roussel_fabien = 0
macron_emmanuel = 0
lassalle_jean = 0
le_pen_marine = 0
zemmour_eric = 0
melenchon_jean_luc = 0
hidalgo_anne = 0
jadot_yannick = 0
pecresse_valerie = 0
poutou_philippe = 0
dupont_aignan_nicolas = 0



# Ouvrir le fichier CSV en mode lecture
with open("csv/election.csv", "r") as fichier_csv:
    # Créer un lecteur CSV
    lecteur_csv = csv.DictReader(fichier_csv)

    # Itérer sur chaque ligne
    for ligne in lecteur_csv:
        # Ajouter la valeur de chaque colonne à sa variable respective
        nb_vote_blanc += float(ligne["nb_vote_blanc"])
        nb_vote_nul += float(ligne["nb_vote_nul"])
        nb_exprime += float(ligne["nb_exprime"])
        arthaud_nathalie += float(ligne["arthaud_nathalie"])
        roussel_fabien += float(ligne["roussel_fabien"])
        macron_emmanuel += float(ligne["macron_emmanuel"])
        lassalle_jean += float(ligne["lassalle_jean"])
        le_pen_marine += float(ligne["le_pen_marine"])
        zemmour_eric += float(ligne["zemmour_eric"])
        melenchon_jean_luc += float(ligne["melenchon_jean_luc"])
        hidalgo_anne += float(ligne["hidalgo_anne"])
        jadot_yannick += float(ligne["jadot_yannick"])
        pecresse_valerie += float(ligne["pecresse_valerie"])
        poutou_philippe += float(ligne["poutou_philippe"])
        dupont_aignan_nicolas += float(ligne["dupont_aignan_nicolas"])



# Créer un dictionnaire avec les données "key" :  value,
donnees = {
    "nb_vote_blanc": nb_vote_blanc,
    "nb_vote_nul": nb_vote_nul,
    "nb_exprime": nb_exprime,
    "arthaud_nathalie": arthaud_nathalie,
    "roussel_fabien": roussel_fabien,
    "macron_emmanuel": macron_emmanuel,
    "lassalle_jean": lassalle_jean,
    "le_pen_marine": le_pen_marine,
    "zemmour_eric": zemmour_eric,
    "melenchon_jean_luc": melenchon_jean_luc,
    "hidalgo_anne": hidalgo_anne,
    "jadot_yannick": jadot_yannick,
    "pecresse_valerie": pecresse_valerie,
    "poutou_philippe": poutou_philippe,
    "dupont_aignan_nicolas": dupont_aignan_nicolas,

}

# Définir le nom du fichier CSV
fichier_csv = "csv/donnees_votes.csv"

# Écrire les données dans le fichier CSV
with open(fichier_csv, "w", newline="") as csvfile:
    # Crée un objet writer avec un en-tête correspondant aux clés du dictionnaire "donnees"
    writer = csv.DictWriter(csvfile, fieldnames=donnees.keys())
     # Écrit l'en-tête dans le fichier CSV
    writer.writeheader()
    # Écrit une ligne contenant les données dans le fichier CSV
    # "donnees" est un dictionnaire contenant les données à écrire
    writer.writerow(donnees)

# Afficher un message de confirmation
print("Les données ont été enregistrées dans le fichier", fichier_csv)


# Afficher le résultat pour chaque colonne (vérification)
print("Nombre de votes blancs :", nb_vote_blanc)
print("Nombre de votes nuls :", nb_vote_nul)
print("Nombre de votes exprimés :", nb_exprime)
print("Nombre de votes pour Nathalie Arthaud :", arthaud_nathalie)
print("Nombre de votes pour Fabien Roussel :", roussel_fabien)
print("Nombre de votes pour Emmanuel Macron :", macron_emmanuel)
print("Nombre de votes pour Jean Lassalle :", lassalle_jean)
print("Nombre de votes pour Marine Le Pen :", le_pen_marine)
print("Nombre de votes pour Eric Zemmour :", zemmour_eric)
print("Nombre de votes pour Jean-Luc Mélenchon :", melenchon_jean_luc)
print("Nombre de votes pour Anne Hidalgo :", hidalgo_anne)
print("Nombre de votes pour Yannick Jadot :", jadot_yannick)
print("Nombre de votes pour Valerie Pecresse :", pecresse_valerie)
print("Nombre de votes pour Philippe Poutou :", poutou_philippe)
print("Nombre de votes pour Nicolas Dupont Aignan :", dupont_aignan_nicolas)

#calcule le % pour chaque candidat avec round (2 chiffres après la ,)
netvotemanu = round((macron_emmanuel / nb_exprime) * 100, 2)
netvotemarine  = round((le_pen_marine / nb_exprime) * 100, 2)
netvotemelanchon = round((melenchon_jean_luc / nb_exprime) * 100, 2)
netvoteyannick = round((jadot_yannick / nb_exprime) * 100, 2)
netvotezemmour = round((zemmour_eric / nb_exprime) * 100, 2)
netvotejadot = round((jadot_yannick / nb_exprime) * 100, 2)
netvotelasalle = round((lassalle_jean / nb_exprime) * 100, 2)
netvotehidalgo  = round((hidalgo_anne / nb_exprime) * 100, 2)
netvotenicolas  = round((dupont_aignan_nicolas / nb_exprime) * 100, 2)
netvotenathalie  = round((arthaud_nathalie/ nb_exprime) * 100, 2)
netvotepoutou  = round((poutou_philippe / nb_exprime) * 100, 2)
netvotevalerie  = round((pecresse_valerie/ nb_exprime) * 100, 2)
netvoteroussel = round((roussel_fabien / nb_exprime) * 100, 2)

#Partie graphique (un exemple commenter on fera la même chose pour les 11 autres candidats)
# Données
labels = ['Emmanuel Macron', 'Autres']
pourcentages = [netvotemanu, 100-netvotemanu]

# Créer un graphique en camembert avec les pourcentages
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')

# Ajouter un titre
ax.set_title("Répartition des votes en île de France en %")

# Exporter le graphique sous forme d'image
fig.savefig("img/Figure1.png")

# Afficher un message pour confirmer que l'image a été enregistrée
print("Graphique enregistré sous le nom de Figure1.png")



labels = ['Marine Lepen', 'Autres']
pourcentages = [netvotemarine, 100-netvotemarine]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure2.png")
print("Graphique enregistré sous le nom de Figure2.png")

labels = ['Jean Luc Melanchon', 'Autres']
pourcentages = [netvotemelanchon, 100-netvotemelanchon]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure3.png")
print("Graphique enregistré sous le nom de Figure3.png")




labels = ['Eric Zemmour', 'Autres']
pourcentages = [netvotezemmour, 100-netvotezemmour]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure4.png")
print("Graphique enregistré sous le nom de Figure4.png")


labels = ['Yanick Jadot', 'Autres']
pourcentages = [netvotejadot, 100-netvotejadot]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure5.png")
print("Graphique enregistré sous le nom de Figure5.png")




labels = ['Jean Lasalle', 'Autres']
pourcentages = [netvotelasalle, 100-netvotelasalle]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure6.png")
print("Graphique enregistré sous le nom de Figure6.png")

labels = ['Anne Hidalgo', 'Autres']
pourcentages = [netvotehidalgo, 100-netvotehidalgo]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure7.png")
print("Graphique enregistré sous le nom de Figure7.png")

labels = ['Nicolas Aignant ', 'Autres']
pourcentages = [netvotenicolas, 100-netvotenicolas]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure8.png")
print("Graphique enregistré sous le nom de Figure8.png")

labels = ['Nathalie Arthaud', 'Autres']
pourcentages = [netvotenathalie, 100-netvotenathalie]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure9.png")
print("Graphique enregistré sous le nom de Figure9.png")


labels = ['Philippe Poutou', 'Autres']
pourcentages = [netvotepoutou, 100-netvotepoutou]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure10.png")
print("Graphique enregistré sous le nom de Figure10.png")

labels = ['Valérie Pécresse', 'Autres']
pourcentages = [netvotevalerie, 100-netvotevalerie]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure11.png")
print("Graphique enregistré sous le nom de Figure11.png")

labels = ['Fabien Roussel', 'Autres']
pourcentages = [netvoteroussel, 100-netvoteroussel]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("img/Figure12.png")
print("Graphique enregistré sous le nom de Figure12.png")


#Partie interraction avec l'utilisateur via le terminal

candidat = int(input( "\n 1 : Emmanuel Macron \n 2 : Nathalie Arthaud \n 3 : Fabien Roussel\n 4 : Jean Lasalle\n 5 : Marine Le Pen\n 6 : Eric Zemmour\n 7 : Jean-Luc-Mélanchon\n 8 : Anne Hidalgo\n 9 : Yannick Jadot\n 10: Valérie Pécresse\n 11: Philippe Poutou\n 12: Nicolas Dupont Aignan \n Quel candidat voulez-vous choisir [1:12]:" ))

#créer un dictionnaire pour avoir tous les cas de figures
lut = {1: ("macron_emmanuel", "Emmanuel Macron"),
       2: ("arthaud_nathalie", "Nathalie Arthaud"),
       3: ("roussel_fabien", "Fabien Roussel"),
       4: ("lassalle_jean", "Jean Lassalle"),
       5: ("le_pen_marine", "Marine Le Pen"),
       6: ("zemmour_eric", "Eric Zemmour"),
       7: ("melenchon_jean_luc", "Jean-Luc Mélenchon"),
       8: ("hidalgo_anne", "Anne Hidalgo"),
       9: ("jadot_yannick", "Yannick Jadot"),
       10: ("pecresse_valerie", "Valérie Pécresse"),
       11: ("poutou_philippe", "Philippe Poutou"),
       12: ("dupont_aignan_nicolas", "Nicolas Dupont-Aignan")}

#regarder à l'index 0 et 1 pour la key et la value
candidat_key = lut[candidat][0]
candidat_name = lut[candidat][1]

pourcentage_score = round((donnees[candidat_key] / nb_exprime) * 100, 2)

fichier_csv = "csv/resultat.csv"    #générer un fichier csv pour chaque candidat choisi
with open(fichier_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["candidat", "score_en_pourcentages", "nb_voies"]) #création de descripteur
    writer.writerow([candidat_name, pourcentage_score, donnees[candidat_key]])

#afficher la phrase de conclusion en utilisant le formatage (f)
print(f"{candidat_name} a obtenu {pourcentage_score}% des votes du premier tour en île de France.\n Le fichier resultat.csv a été généré sur le candidat choisi")





















