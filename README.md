# Hooky

## Cahier des charges

- Menu :
  - Jouer : affiche le sélécteur de maps
  - Options : affiche le menus des options (modifier les binds des touches, le volume, reset les scores...)
- Jeu :
  - Encodage des cartes :
    - Dans un .txt ou autre
  - Personnage :
    - Peut hook des blocs avec un grapin
    - Peut jump
    - Peut se déplacer (gauche/droite) (Dans les airs, mais moindrement)
- Bonus :
  - Editeur de niveau
  - Blocks bleus/oranges (inspiré de Portal)
  - Portal gun avec le clic gauche

## Organisation des fichiers

- Dossier `Assets` : Contient toutes les ressources utilisées (images, musiques, polices, niveaux et le fichier de configuration).
- Dossier `Sources` : Contient le code source Python.
  - Fichier `main.py` : Point d'entré du programme
  - Fichier `menu.py` : Définit le menu principal, qui contient des sous-menus appelés par des widgets
  - Fichier `game.py` : Définit la classe `Game` qui gère l'état du jeu
  - Fichier `entity.py` : Définit une entité de base dans le jeu (utilisé pour le grapin et le joueur)
  - Fichier `hook.py` : Définit le grapin
  - Fichier `level.py` : Définit un niveau quelconque
  - Fichier `music_manager.py` : Fonctions permettant de gérer la musique de fond
  - Fichier `player.py` : Définit le joueur
  - Fichier `screens.py` : Différents écrans disponibles (sur le menu principal)
  - Fichier `utils.py` : Diverses fonctions utilitaires
  - Fichier `vector.py` : Définit un vecteur mathématique
  - Fichier `widget.py` : Différents widgets utilisés (bouton, sliders, checkbox, keybinder...)

## Répartition des tâches

- Maitre Bendo gère le piano 🪗
- Aly à la créa 🎨
- Ulysse au level design 🧱
- Elliot au jeu 💻 (on partage hein)
- Zebty fait le GUI 🖼
