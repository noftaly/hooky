# Hooky

## Cahier des charges

- Menu :
  - Jouer : affiche le sélécteur de maps
  - Options : affiche le menus des options (modifier les binds des touches, le volume, reset les scores...)
- Jeu :
  - Encodage des cartes :
    - Espaces : Air | 0 : Block | 1 : Reset | 2 : Blue | 3 : Orange | 4
    - Dans un .txt ou autre
  - Personnage :
    - Peut hook des blocs avec un grapin
    - Peut jump/double jump
    - Peut se déplacer (gauche/droite) (Dans les airs, mais moindrement)
- Bonus :
  - Editeur de niveau
  - Blocks bleus/oranges (inspiré de Portal)
  - Portal gun avec le clic gauche

## Organisation des fichiers

- Dossier `Assets` : Contient toutes les ressources utilisées (images, musiques...).
- Dossier `Levels` : Contient tous les fichiers des niveaux.
- Dossier `Sources` : Contient le code source Python.
  - Fichier `main.py` : Fait appel à la méthode `main()` du menu, installe les librairies manquantes
  - Fichier `menu.py` : Définit la classe `Menu`, qui elle même fait appel à des classes widgets définis dans d'autres fichiers
  - Fichier `game.py` : Définit la classe `Game`, qui fait appel à `Player` et `Level`

## Répartition des tâches

- Maitre Bendo gère le piano 🪗
- Aly à la créa 🎨
- Ulysse au level design 🧱
- Elliot au jeu 💻 (on partage hein)
- Zebty fait le GUI 🖼
