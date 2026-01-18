# Piveo

## Fonction du projet

MémoVue est une application éducative développée en Python avec une interface graphique PySide6 pour les écoles, les entreprises et les parlementaires
Elle permet d’apprendre ou de retrouver les noms et prénoms de personnes à partir d'une base de données SQLite3.

<p align="center">
  <img src="fichiers/images/accueil.png" alt="Accueil">
</p>

## Fonctionnement

L'interface comporte trois zones :  

- **Zone gauche** : affiche les informations sur la personne.  
- **Zone en haut à droite** : permet de répondre aux questions.  
- **Zone en bas à droite** : permet d'effectuer les réglages (n'oubliez pas le bouton **Valider** !).  

![interface](fichiers/images/interface-1.png)

De bas en haut, dans la zone en bas à droite :  

1. Sélection de ce que l'on souhaite afficher :  
   - prénom et nom  
   - prénom seul  
   - nom seul  
2. Activation optionnelle du **mode aléatoire** (présentation dans le désordre).  
3. Choix du **Département** puis de la **Fonction** via les deux listes déroulantes (*combobox*).  
4. Choix du **mode d’utilisation** :  
   - **Apprentissage** : affichage des personnes et de leurs informations.  
   - **Test écrit** : l’utilisateur doit saisir les noms ou prénoms.  
   - **Test oral** : affichage d’une photo, l’utilisateur cherche mentalement avant de voir la correction.  
   - **Recherche** : retrouver une personne à partir d’un nom ou prénom.  
5. Les quatre boutons sous l’image permettent de faire défiler les personnes sélectionnées.  
6. La zone de saisie (en haut à droite) est utilisée dans les tests écrits et pour certaines recherches.

Le programme utilise:

- Trois bases de données SQLite (`eleves.db`, `deputes.db` ou `salaries.db` à la racine du projet).  
- Des images des personnes.
- des fichiers d'initialisation CSV.

Trois organismes sont fournis par défaut (Établissement scolaire, Parlement, Entreprise), mais il est possible d’ajouter un organisme personnalisé (ex. club de sport) en créant sa propre base, ses images et ses fichiers CSV.  
Le choix de l’organisme se fait au lancement, via **Piveo.pyw**.

## Vidéo

[Vidéo de présentation de Piveo](https://youtu.be/upmGYy93n2w)

## Installation

### 🔗 Depuis les sources

1. **Cloner le dépôt**  
   
   ```bash
   git clone https://github.com/GerardLeRest/Piveo
   cd Fenetre
   ```

2. **Créer un environnement virtuel**  
   `venv` doit être installé. Ici, *mon_env* est le nom choisi pour l'environnement Python.  
   
   ```bash
   python3 -m venv mon_env
   source mon_env/bin/activate
   ```

3. **Installer la dépendance**  
   MémoVue utilise la bibliothèque **PySide6** pour l’interface graphique :  
   
   ```bash
   pip install pyside6
   ```



### 🪟 Windows

- Aller sur https://github.com/GerardLeRest/Piveo/releases/
- Sélectionner et télécharger "PiveoSetup-1.1.1.exe"  
- Suivre les instructions et installer-le sur votre poste Windows.
- Lancer le logiciel depuis les programmes ou depuis le Bureau
- 

### 🐧GNU/Linux

#### 1. Créer un dossier de travail

```bash
mkdir -p ~/Piveo
```

---

#### 2. Se placer dans le dossier de téléchargement

```bash
cd ~/Téléchargements
```

---

#### 3. Télécharger l’archive AppImage

Rendez-vous sur la page des releases GitHub :  
https://github.com/GerardLeRest/Piveo/releases

#### Téléchargez la **dernière archive AppImage**, par exemple :

Piveo-x.x.x-_x86_64.AppImage (x.x.x sont à remplacer par 2.2.1 pour la version 2.2.1, par exemple)

#### 4. Décompresser l’archive

```bash
tar -xf Piveo-x.x.x-_x86_64.AppImage.tar.xz
```

---

#### 5. Copier les fichiers dans le dossier Piveo

```bash
cp -r ~/Téléchargements/Piveo-x.x.x-_x86_64.AppImage/. ~/Piveo
```

On peut également utiliser le dossier /opt au lieu de ~/Piveo de  qui est spécialement conçu pour ce genre d'installation.

---

#### 6. Vérifier le contenu

```bash
ls ~/Piveo
```

Le dossier doit contenir :

- l’AppImage **Piveo_1.2.0_x86_64.AppImage**
- **six fichiers**
- le dossier **`fichiers`**

---

#### 7. Rendre l’AppImage exécutable

```bash
chmod +x ~/Piveo-x.x.x-_x86_64.AppImage
```

---

#### 8. Lancer le logiciel

Se rendre dans le dossier ~/Piveo:

```bash
cd ~/Piveo
```

Lancer Piveo:

```bash
./Piveo_1.2.0_x86_64.AppImage
```

---

<p align="center">
  <img src="fichiers/images/piveo.png" alt="Icone">
</p>

## (Optionnel) Intégration au menu du système

Vous pouvez installer **Alacarte**, qui permet d’ajouter facilement Piveo au menu des applications :

```bash
sudo apt install alacarte
```

## Remarques

- Compatible Python 3.8+  
- Testé sous Ubuntu et Windows  
- L’application est en cours d’amélioration (v1.0.0)

## Liens

- [Site internet](https://gerardlerest.github.io/piveo/)  
- [Dépôt GitHub](https://github.com/GerardLeRest/Piveo)
- [page wiki](https://doc.ubuntu-fr.org/Piveo)

## Licence & photos

Ce projet est distribué sous licence **GPL-v3**.  
© 2026 Gérard LE REST  

Les portraits ont été générés par une intelligence artificielle et sont utilisés dans un cadre pédagogique non commercial.  
*"Image by Generated Photos (https://generated.photos), used with permission."*
