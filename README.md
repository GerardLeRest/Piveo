# MémoVue

## Fonction du projet

MémoVue est une application éducative développée en Python avec une interface graphique PySide6.  
Elle permet d’apprendre ou de retrouver les noms et prénoms de personnes à partir d'une base de données SQLite3.

## Fonctionnement

L'interface comporte trois zones :  

- **Zone gauche** : affiche les informations sur la personne.  
- **Zone en haut à droite** : permet de répondre aux questions.  
- **Zone en bas à droite** : permet d'effectuer les réglages (n'oubliez pas le bouton **Valider** !).  

![interface](fichiers/images/interface.png)

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
Le choix de l’organisme se fait au lancement, via **MemoVue.pyw**.

## Vidéo

[Vidéo de présentation de MémoVue](https://youtu.be/upmGYy93n2w)

## Installation

### Depuis les sources

1. **Cloner le dépôt**  
   
   ```bash
   git clone https://github.com/GerardLeRest/MemoVue
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

### Windows

- Aller sur https://github.com/GerardLeRest/MemoVue/releases/tag/v1.0.0 
- Sélectionner et télécharger "MemoVueSetup-1.0.0.exe"  ainsi que le dossier zip. Mettre les fichiers à mettre avec l'exécutableble dans un dossier.
- Installer-le sur votre poste Windows.
- Lancer le logiciel depuis les programmes ou depuis le Bureau

### GNU/Linux

- Aller sur https://github.com/GerardLeRest/MemoVue/releases/tag/v1.0.0

- Sélectionner et télécharger "MemoVue_1.0.0_x86_64.AppImage" ainsi que le dossier zip. Mettre les fichiers qui seront à mettre avec l'exécutableble dans un dossier.

- Créer un dossier ~/MemoVue_data

- Y mettre les six fichiers et "MemoVue_1.0.0_x86_64.AppImage"

- se déplacer dans le dossier
  
  ```bash
  cd  ~/MemoVue_data~
  ```
  
  Rendre le fichier exécutable
  
  ```bash
  chmod +x MemoVue_1.0.0_x86_64.AppImage
  ```
  
  lancer le logiciel
  
  ```bash
  ./MemoVue_1.0.0_x86_64.AppImage
  ```
  
  Installer si vous le souhaitez, Alacarte qui permet d'intégrer votre logiciel au menu
  
  ```bash
  sudo apt install alacarte
  ```

## Remarques

- Compatible Python 3.8+  
- Testé sous Ubuntu et Windows  
- L’application est en cours d’amélioration (v1.0.0)

## Liens

- [Site internet](https://gerardlerest.github.io/memovue/)  
- [Dépôt GitHub](https://github.com/GerardLeRest/MemoVue)

## Licence & photos

Ce projet est distribué sous licence **GPL-v3**.  
© 2025 Gérard LE REST  

Les portraits ont été générés par une intelligence artificielle et sont utilisés dans un cadre pédagogique non commercial.  
*"Image by Generated Photos (https://generated.photos), used with permission."*
