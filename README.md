# Classeur Pokémon

Classeur personnel pour suivre une collection de cartes Pokémon shiny et deux collections par espèce.

- **Shiny** : Baby Shiny (269 shiny simples de Destins Occultes, Destinées Radieuses, Destinées de Paldea), Pokémon Radieux (16), Pokémon Brillant (20).
- **Collections** : Caninos & Arcanin, Miaouss & Persian (cartes japonaises et internationales, de 1996 à aujourd'hui).

- `index.html` : l'application, en un seul fichier. La collection est enregistrée dans le navigateur (export/import de sauvegarde, et import « ajout » qui complète la collection sans l'écraser).
- `src/` : sources pour régénérer `index.html` (`python3 src/gen_data.py data.js` et `python3 src/gen_themes.py themes.js`, puis insertion des deux fichiers à la place de `/*DATA*/` dans `src/template.html`).

Images des cartes : pokemontcg.io, Scrydex, Pokellector. Usage personnel, non affilié à The Pokémon Company.
