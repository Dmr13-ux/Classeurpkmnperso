# Classeur Pokémon Jap

Classeur personnel pour suivre une collection de cartes Pokémon japonaises de l'ère Original :
Expansion Pack, Pokémon Jungle, Mystery of the Fossils, Rocket Gang, Leaders' Stadium et Challenge from the Darkness (457 cartes), plus deux collections thématiques toutes langues : Caninos & Arcanin, Miaouss & Persian (cartes internationales via pokemontcg.io).

- `index.html` : l'application, en un seul fichier. La collection est enregistrée dans le navigateur (export/import de sauvegarde possible).
- `src/` : sources pour régénérer `index.html` (`python3 src/gen_data.py data.js` et `python3 src/gen_themes.py themes.js`, puis insertion des deux fichiers à la place de `/*DATA*/` dans `src/template.html`).

Images des cartes : Pokellector. Usage personnel, non affilié à The Pokémon Company.
