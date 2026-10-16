"""Génère les données des sets (JS) pour le classeur Pokémon jap."""
import json, re, sys

# espèce anglaise -> (nom FR, n° Pokédex, type TCG)
SP = {
"Bulbasaur":("Bulbizarre",1,"G"),"Ivysaur":("Herbizarre",2,"G"),"Venusaur":("Florizarre",3,"G"),
"Charmander":("Salamèche",4,"F"),"Charmeleon":("Reptincel",5,"F"),"Charizard":("Dracaufeu",6,"F"),
"Squirtle":("Carapuce",7,"W"),"Wartortle":("Carabaffe",8,"W"),"Blastoise":("Tortank",9,"W"),
"Caterpie":("Chenipan",10,"G"),"Metapod":("Chrysacier",11,"G"),"Butterfree":("Papilusion",12,"G"),
"Weedle":("Aspicot",13,"G"),"Kakuna":("Coconfort",14,"G"),"Beedrill":("Dardargnan",15,"G"),
"Pidgey":("Roucool",16,"C"),"Pidgeotto":("Roucoups",17,"C"),"Pidgeot":("Roucarnage",18,"C"),
"Rattata":("Rattata",19,"C"),"Raticate":("Rattatac",20,"C"),"Spearow":("Piafabec",21,"C"),"Fearow":("Rapasdepic",22,"C"),
"Ekans":("Abo",23,"G"),"Arbok":("Arbok",24,"G"),"Pikachu":("Pikachu",25,"L"),"Raichu":("Raichu",26,"L"),
"Sandshrew":("Sabelette",27,"Fi"),"Sandslash":("Sablaireau",28,"Fi"),
"Nidoran♀":("Nidoran♀",29,"G"),"Nidorina":("Nidorina",30,"G"),"Nidoqueen":("Nidoqueen",31,"G"),
"Nidoran♂":("Nidoran♂",32,"G"),"Nidorino":("Nidorino",33,"G"),"Nidoking":("Nidoking",34,"G"),
"Clefairy":("Mélofée",35,"C"),"Clefable":("Mélodelfe",36,"C"),"Vulpix":("Goupix",37,"F"),"Ninetales":("Feunard",38,"F"),
"Jigglypuff":("Rondoudou",39,"C"),"Wigglytuff":("Grodoudou",40,"C"),"Zubat":("Nosferapti",41,"G"),"Golbat":("Nosferalto",42,"G"),
"Oddish":("Mystherbe",43,"G"),"Gloom":("Ortide",44,"G"),"Vileplume":("Rafflesia",45,"G"),
"Paras":("Paras",46,"G"),"Parasect":("Parasect",47,"G"),"Venonat":("Mimitoss",48,"G"),"Venomoth":("Aéromite",49,"G"),
"Diglett":("Taupiqueur",50,"Fi"),"Dugtrio":("Triopikeur",51,"Fi"),"Meowth":("Miaouss",52,"C"),"Persian":("Persian",53,"C"),
"Psyduck":("Psykokwak",54,"W"),"Golduck":("Akwakwak",55,"W"),"Mankey":("Férosinge",56,"Fi"),"Primeape":("Colossinge",57,"Fi"),
"Growlithe":("Caninos",58,"F"),"Arcanine":("Arcanin",59,"F"),"Poliwag":("Ptitard",60,"W"),"Poliwhirl":("Têtarte",61,"W"),"Poliwrath":("Tartard",62,"W"),
"Abra":("Abra",63,"P"),"Kadabra":("Kadabra",64,"P"),"Alakazam":("Alakazam",65,"P"),
"Machop":("Machoc",66,"Fi"),"Machoke":("Machopeur",67,"Fi"),"Machamp":("Mackogneur",68,"Fi"),
"Bellsprout":("Chétiflor",69,"G"),"Weepinbell":("Boustiflor",70,"G"),"Victreebel":("Empiflor",71,"G"),
"Tentacool":("Tentacool",72,"W"),"Tentacruel":("Tentacruel",73,"W"),
"Geodude":("Racaillou",74,"Fi"),"Graveler":("Gravalanch",75,"Fi"),"Golem":("Grolem",76,"Fi"),
"Ponyta":("Ponyta",77,"F"),"Rapidash":("Galopa",78,"F"),"Slowpoke":("Ramoloss",79,"P"),"Slowbro":("Flagadoss",80,"P"),
"Magnemite":("Magnéti",81,"L"),"Magneton":("Magnéton",82,"L"),"Farfetch'd":("Canarticho",83,"C"),
"Doduo":("Doduo",84,"C"),"Dodrio":("Dodrio",85,"C"),"Seel":("Otaria",86,"W"),"Dewgong":("Lamantine",87,"W"),
"Grimer":("Tadmorv",88,"G"),"Muk":("Grotadmorv",89,"G"),"Shellder":("Kokiyas",90,"W"),"Cloyster":("Crustabri",91,"W"),
"Gastly":("Fantominus",92,"P"),"Haunter":("Spectrum",93,"P"),"Gengar":("Ectoplasma",94,"P"),"Onix":("Onix",95,"Fi"),
"Drowzee":("Soporifik",96,"P"),"Hypno":("Hypnomade",97,"P"),"Krabby":("Krabby",98,"W"),"Kingler":("Krabboss",99,"W"),
"Voltorb":("Voltorbe",100,"L"),"Electrode":("Électrode",101,"L"),"Exeggcute":("Noeunoeuf",102,"G"),"Exeggutor":("Noadkoko",103,"G"),
"Cubone":("Osselait",104,"Fi"),"Marowak":("Ossatueur",105,"Fi"),"Hitmonlee":("Kicklee",106,"Fi"),"Hitmonchan":("Tygnon",107,"Fi"),
"Lickitung":("Excelangue",108,"C"),"Koffing":("Smogo",109,"G"),"Weezing":("Smogogo",110,"G"),
"Rhyhorn":("Rhinocorne",111,"Fi"),"Rhydon":("Rhinoféros",112,"Fi"),"Chansey":("Leveinard",113,"C"),"Tangela":("Saquedeneu",114,"G"),
"Kangaskhan":("Kangourex",115,"C"),"Horsea":("Hypotrempe",116,"W"),"Seadra":("Hypocéan",117,"W"),
"Goldeen":("Poissirène",118,"W"),"Seaking":("Poissoroy",119,"W"),"Staryu":("Stari",120,"W"),"Starmie":("Staross",121,"W"),
"Mr. Mime":("M. Mime",122,"P"),"Scyther":("Insécateur",123,"G"),"Jynx":("Lippoutou",124,"P"),"Electabuzz":("Élektek",125,"L"),
"Magmar":("Magmar",126,"F"),"Pinsir":("Scarabrute",127,"G"),"Tauros":("Tauros",128,"C"),"Magikarp":("Magicarpe",129,"W"),
"Gyarados":("Léviator",130,"W"),"Lapras":("Lokhlass",131,"W"),"Ditto":("Métamorph",132,"C"),"Eevee":("Évoli",133,"C"),
"Vaporeon":("Aquali",134,"W"),"Jolteon":("Voltali",135,"L"),"Flareon":("Pyroli",136,"F"),"Porygon":("Porygon",137,"C"),
"Omanyte":("Amonita",138,"W"),"Omastar":("Amonistar",139,"W"),"Kabuto":("Kabuto",140,"Fi"),"Kabutops":("Kabutops",141,"Fi"),
"Aerodactyl":("Ptéra",142,"Fi"),"Snorlax":("Ronflex",143,"C"),"Articuno":("Artikodin",144,"W"),"Zapdos":("Électhor",145,"L"),
"Moltres":("Sulfura",146,"F"),"Dratini":("Minidraco",147,"C"),"Dragonair":("Draco",148,"C"),"Dragonite":("Dracolosse",149,"C"),
"Mewtwo":("Mewtwo",150,"P"),"Mew":("Mew",151,"P"),
}
OWN = {"Brock's":"de Pierre","Misty's":"d'Ondine","Lt. Surge's":"du Major Bob","Erika's":"d'Érika",
       "Sabrina's":"de Morgane","Koga's":"de Koga","Blaine's":"d'Auguste","Giovanni's":"de Giovanni",
       "Rocket's":"de Rocket","Imakuni?'s":"d'Imakuni?","_____'s":"de _____"}
ENERGY = {"Potion Energy","Full Heal Energy","Rainbow Energy"}
TRAINER_FR = {"Poké Ball":"Poké Ball","Mr. Fuji":"M. Fuji","Rocket's Sneak Attack":"Attaque surprise de Rocket"}

def card(slug, en, holo=False, img=None):
    owner, base, dark = None, en, False
    for k in OWN:
        if en.startswith(k+" "):
            owner, base = k, en[len(k)+1:]
    if base.startswith("Dark "):
        dark, base = True, base[5:]
    if base in SP:
        fr, dex, t = SP[base]
        if dark: fr += " Obscur"
        if owner: fr += " " + OWN[owner]
    else:
        fr, dex, t = TRAINER_FR.get(en, ""), 0, ("E" if en in ENERGY else "T")
    row = [slug, en, fr if fr != en else "", dex, t]
    if holo or img: row.append(1 if holo else 0)
    if img: row.append(img)
    return row

def from_links(text, holos, overrides=None):
    rows = []
    for i, line in enumerate([l for l in text.strip().splitlines() if l.strip()], 1):
        slug, en = [x.strip() for x in line.split("|")]
        rows.append(card(slug, en, i in holos, (overrides or {}).get(i)))
    return rows

JUNGLE = """
Nidoran|Nidoran♀
Oddish|Oddish
Paras|Paras
Venonat|Venonat
Bellsprout|Bellsprout
Exeggcute|Exeggcute
Butterfree|Butterfree
Nidorina|Nidorina
Gloom|Gloom
Parasect|Parasect
Weepinbell|Weepinbell
Exeggutor|Exeggutor
Nidoqueen|Nidoqueen
Vileplume|Vileplume
Venomoth|Venomoth
Victreebel|Victreebel
Scyther|Scyther
Pinsir|Pinsir
Rapidash|Rapidash
Flareon|Flareon
Goldeen|Goldeen
Seaking|Seaking
Vaporeon|Vaporeon
Pikachu|Pikachu
Electrode|Electrode
Jolteon|Jolteon
Mr-Mime|Mr. Mime
Mankey|Mankey
Cubone|Cubone
Rhyhorn|Rhyhorn
Primeape|Primeape
Marowak|Marowak
Rhydon|Rhydon
Spearow|Spearow
Jigglypuff|Jigglypuff
Meowth|Meowth
Eevee|Eevee
Fearow|Fearow
Persian|Persian
Dodrio|Dodrio
Lickitung|Lickitung
Tauros|Tauros
Pidgeot|Pidgeot
Clefable|Clefable
Wigglytuff|Wigglytuff
Kangaskhan|Kangaskhan
Snorlax|Snorlax
Pok-Ball|Poké Ball
"""
FOSSIL = """
Ekans|Ekans
Zubat|Zubat
Grimer|Grimer
Arbok|Arbok
Golbat|Golbat
Weezing|Weezing
Muk|Muk
Magmar|Magmar
Moltres|Moltres
Psyduck|Psyduck
Tentacool|Tentacool
Shellder|Shellder
Krabby|Krabby
Horsea|Horsea
Omanyte|Omanyte
Golduck|Golduck
Tentacruel|Tentacruel
Cloyster|Cloyster
Kingler|Kingler
Seadra|Seadra
Omastar|Omastar
Lapras|Lapras
Articuno|Articuno
Raichu|Raichu
Magneton|Magneton
Zapdos|Zapdos
Slowpoke|Slowpoke
Slowbro|Slowbro
Gastly|Gastly
Haunter|Haunter
Gengar|Gengar
Hypno|Hypno
Mew|Mew
Geodude|Geodude
Kabuto|Kabuto
Sandslash|Sandslash
Graveler|Graveler
Golem|Golem
Hitmonlee|Hitmonlee
Kabutops|Kabutops
Aerodactyl|Aerodactyl
Ditto|Ditto
Dragonite|Dragonite
Energy-Search|Energy Search
Gambler|Gambler
Mysterious-Fossil|Mysterious Fossil
Recycle|Recycle
Mr-Fuji|Mr. Fuji
"""
ROCKET = """
Ekans|Ekans
Zubat|Zubat
Oddish|Oddish
Grimer|Grimer
Koffing|Koffing
Dark-Gloom|Dark Gloom
Dark-Muk|Dark Muk
Dark-Arbok|Dark Arbok
Dark-Golbat|Dark Golbat
Dark-Vileplume|Dark Vileplume
Dark-Weezing|Dark Weezing
Charmander|Charmander
Ponyta|Ponyta
Dark-Rapidash|Dark Rapidash
Dark-Charmeleon|Dark Charmeleon
Dark-Flareon|Dark Flareon
Dark-Charizard|Dark Charizard
Squirtle|Squirtle
Psyduck|Psyduck
Magikarp|Magikarp
Dark-Wartortle|Dark Wartortle
Dark-Golduck|Dark Golduck
Dark-Vaporeon|Dark Vaporeon
Dark-Blastoise|Dark Blastoise
Dark-Gyarados|Dark Gyarados
Magnemite|Magnemite
Voltorb|Voltorb
Dark-Electrode|Dark Electrode
Dark-Jolteon|Dark Jolteon
Dark-Magneton|Dark Magneton
Abra|Abra
Slowpoke|Slowpoke
Drowzee|Drowzee
Dark-Kadabra|Dark Kadabra
Dark-Alakazam|Dark Alakazam
Dark-Slowbro|Dark Slowbro
Dark-Hypno|Dark Hypno
Diglett|Diglett
Mankey|Mankey
Machop|Machop
Dark-Primeape|Dark Primeape
Dark-Machoke|Dark Machoke
Dark-Dugtrio|Dark Dugtrio
Dark-Machamp|Dark Machamp
Rattata|Rattata
Dark-Raticate|Dark Raticate
Meowth|Meowth
Dark-Persian|Dark Persian
Eevee|Eevee
Porygon|Porygon
Dratini|Dratini
Dark-Dragonair|Dark Dragonair
Dark-Dragonite|Dark Dragonite
Sleep|Sleep!
Digger|Digger
Goop-Gas-Attack|Goop Gas Attack
Nightly-Garbage-Run|Nightly Garbage Run
Challenge|Challenge!
Imposter-Oaks-Revenge|Imposter Oak's Revenge
The-Bosss-Way|The Boss's Way
Rockets-Sneak-Attack|Rocket's Sneak Attack
Here-Comes-Team-Rocket|Here Comes Team Rocket!
Potion-Energy|Potion Energy
Full-Heal-Energy|Full Heal Energy
Rainbow-Energy|Rainbow Energy
"""
LEADERS = """
Brocks-Zubat|Brock's Zubat
Erikas-Oddish|Erika's Oddish
Erikas-Oddish|Erika's Oddish
Erikas-Paras|Erika's Paras
Erikas-Bellsprout|Erika's Bellsprout
Erikas-Tangela|Erika's Tangela
Erikas-Bulbasaur|Erika's Bulbasaur
Brocks-Golbat|Brock's Golbat
Erikas-Gloom|Erika's Gloom
Erikas-Bellsprout|Erika's Bellsprout
Erikas-Weepinbell|Erika's Weepinbell
Erikas-Exeggcute|Erika's Exeggcute
Erikas-Exeggutor|Erika's Exeggutor
Erikas-Vileplume|Erika's Vileplume
Erikas-Victreebel|Erika's Victreebel
Rockets-Scyther|Rocket's Scyther
Brocks-Vulpix|Brock's Vulpix
Brocks-Vulpix|Brock's Vulpix
Brocks-Ninetales|Brock's Ninetales
Rockets-Moltres|Rocket's Moltres
Mistys-Psyduck|Misty's Psyduck
Mistys-Poliwag|Misty's Poliwag
Mistys-Seel|Misty's Seel
Mistys-Horsea|Misty's Horsea
Mistys-Horsea|Misty's Horsea
Mistys-Goldeen|Misty's Goldeen
Mistys-Staryu|Misty's Staryu
Mistys-Magikarp|Misty's Magikarp
Mistys-Poliwhirl|Misty's Poliwhirl
Mistys-Tentacool|Misty's Tentacool
Mistys-Dewgong|Misty's Dewgong
Mistys-Golduck|Misty's Golduck
Mistys-Tentacruel|Misty's Tentacruel
Mistys-Seadra|Misty's Seadra
Mistys-Gyarados|Misty's Gyarados
Lt-Surges-Pikachu|Lt. Surge's Pikachu
Lt-Surges-Magnemite|Lt. Surge's Magnemite
Lt-Surges-Voltorb|Lt. Surge's Voltorb
Lt-Surges-Magnemite|Lt. Surge's Magnemite
Lt-Surges-Magneton|Lt. Surge's Magneton
Lt-Surges-Electabuzz|Lt. Surge's Electabuzz
Lt-Surges-Jolteon|Lt. Surge's Jolteon
Brocks-Sandshrew|Brock's Sandshrew
Brocks-Diglett|Brock's Diglett
Brocks-Mankey|Brock's Mankey
Brocks-Geodude|Brock's Geodude
Brocks-Geodude|Brock's Geodude
Brocks-Onix|Brock's Onix
Brocks-Rhyhorn|Brock's Rhyhorn
Brocks-Sandslash|Brock's Sandslash
Brocks-Primeape|Brock's Primeape
Brocks-Graveler|Brock's Graveler
Brocks-Golem|Brock's Golem
Rockets-Hitmonchan|Rocket's Hitmonchan
Brocks-Rhydon|Brock's Rhydon
Lt-Surges-Rattata|Lt. Surge's Rattata
Lt-Surges-Spearow|Lt. Surge's Spearow
Erikas-Jigglypuff|Erika's Jigglypuff
Lt-Surges-Raticate|Lt. Surge's Raticate
Erikas-Clefairy|Erika's Clefairy
Brocks-Lickitung|Brock's Lickitung
Lt-Surges-Eevee|Lt. Surge's Eevee
Erikas-Dratini|Erika's Dratini
Lt-Surges-Fearow|Lt. Surge's Fearow
Erikas-Clefable|Erika's Clefable
Erikas-Dragonair|Erika's Dragonair
Energy-Flow|Energy Flow
Mistys-Duel|Misty's Duel
Mistys-Tears|Misty's Tears
Narrow-Gym|Narrow Gym
Recall|Recall
Erikas-Maids|Erika's Maids
Erikas-Perfume|Erika's Perfume
Charity|Charity
Mistys-Wrath|Misty's Wrath
Vermilion-City-Gym|Vermilion City Gym
Brocks-Training-Method|Brock's Training Method
Celadon-City-Gym|Celadon City Gym
Pewter-City-Gym|Pewter City Gym
Cerulean-City-Gym|Cerulean City Gym
Lt-Surges-Treaty|Lt. Surge's Treaty
Good-Manners|Good Manners
Erika|Erika
Erikas-Kindness|Erika's Kindness
Misty|Misty
Mistys-Wish|Misty's Wish
Chaos-Gym|Chaos Gym
Secret-Mission|Secret Mission
Brock|Brock
Brocks-Protection|Brock's Protection
Resistance-Gym|Resistance Gym
Lt-Surge|Lt. Surge
Lt-Surges-Secret-Plan|Lt. Surge's Secret Plan
No-Removal-Gym|No Removal Gym
The-Rockets-Training-Gym|The Rocket's Training Gym
The-Rockets-Trap|The Rocket's Trap
"""
CHALLENGE = """
Kogas-Weedle|Koga's Weedle
Kogas-Ekans|Koga's Ekans
Giovannis-Nidoran|Giovanni's Nidoran♀
Giovannis-Nidoran|Giovanni's Nidoran♂
Kogas-Zubat|Koga's Zubat
Sabrinas-Venonat|Sabrina's Venonat
Kogas-Grimer|Koga's Grimer
Kogas-Koffing|Koga's Koffing
Kogas-Tangela|Koga's Tangela
Erikas-Ivysaur|Erika's Ivysaur
Kogas-Kakuna|Koga's Kakuna
Giovannis-Nidorina|Giovanni's Nidorina
Giovannis-Nidorino|Giovanni's Nidorino
Kogas-Golbat|Koga's Golbat
Kogas-Koffing|Koga's Koffing
Kogas-Weezing|Koga's Weezing
Erikas-Venusaur|Erika's Venusaur
Kogas-Beedrill|Koga's Beedrill
Kogas-Arbok|Koga's Arbok
Giovannis-Nidoqueen|Giovanni's Nidoqueen
Giovannis-Nidoking|Giovanni's Nidoking
Sabrinas-Venomoth|Sabrina's Venomoth
Kogas-Muk|Koga's Muk
Giovannis-Pinsir|Giovanni's Pinsir
Blaines-Charmander|Blaine's Charmander
Blaines-Vulpix|Blaine's Vulpix
Blaines-Growlithe|Blaine's Growlithe
Blaines-Ponyta|Blaine's Ponyta
Blaines-Charmeleon|Blaine's Charmeleon
Blaines-Rapidash|Blaine's Rapidash
Blaines-Magmar|Blaine's Magmar
Blaines-Charizard|Blaine's Charizard
Blaines-Ninetales|Blaine's Ninetales
Blaines-Arcanine|Blaine's Arcanine
Blaines-Moltres|Blaine's Moltres
Sabrinas-Psyduck|Sabrina's Psyduck
Giovannis-Magikarp|Giovanni's Magikarp
Sabrinas-Golduck|Sabrina's Golduck
Mistys-Poliwrath|Misty's Poliwrath
Giovannis-Gyarados|Giovanni's Gyarados
Lt-Surges-Raichu|Lt. Surge's Raichu
Rockets-Zapdos|Rocket's Zapdos
Sabrinas-Abra|Sabrina's Abra
Sabrinas-Slowpoke|Sabrina's Slowpoke
Sabrinas-Drowzee|Sabrina's Drowzee
Sabrinas-Mr-Mime|Sabrina's Mr. Mime
Sabrinas-Kadabra|Sabrina's Kadabra
Sabrinas-Slowbro|Sabrina's Slowbro
Sabrinas-Gastly|Sabrina's Gastly
Sabrinas-Haunter|Sabrina's Haunter
Sabrinas-Hypno|Sabrina's Hypno
Sabrinas-Jynx|Sabrina's Jynx
Sabrinas-Alakazam|Sabrina's Alakazam
Sabrinas-Gengar|Sabrina's Gengar
Rockets-Mewtwo|Rocket's Mewtwo
Blaines-Mankey|Blaine's Mankey
Giovannis-Machop|Giovanni's Machop
Blaines-Rhyhorn|Blaine's Rhyhorn
Giovannis-Machoke|Giovanni's Machoke
Brocks-Dugtrio|Brock's Dugtrio
Giovannis-Machamp|Giovanni's Machamp
Kogas-Pidgey|Koga's Pidgey
Giovannis-Meowth|Giovanni's Meowth
Blaines-Doduo|Blaine's Doduo
Blaines-Tauros|Blaine's Tauros
Sabrinas-Porygon|Sabrina's Porygon
Kogas-Pidgey|Koga's Pidgey
Giovannis-Meowth|Giovanni's Meowth
Blaines-Kangaskhan|Blaine's Kangaskhan
Kogas-Pidgeotto|Koga's Pidgeotto
Giovannis-Persian|Giovanni's Persian
Kogas-Ditto|Koga's Ditto
Rockets-Snorlax|Rocket's Snorlax
Imakunis-Doduo|Imakuni?'s Doduo
___s-Chansey|_____'s Chansey
Blaines-Gamble|Blaine's Gamble
Trash-Exchange|Trash Exchange
Sabrinas-Gaze|Sabrina's Gaze
Transparent-Walls|Transparent Walls
Warp-Point|Warp Point
Blaines-Last-Resort|Blaine's Last Resort
Blaines-Quiz-3|Blaine's Quiz #3
Kogas-Ninja-Trick|Koga's Ninja Trick
Tickling-Machine|Tickling Machine
Cinnabar-City-Gym|Cinnabar City Gym
Fuchsia-City-Gym|Fuchsia City Gym
Sabrinas-ESP|Sabrina's ESP
Sabrinas-Psychic-Control|Sabrina's Psychic Control
Minion-of-Team-Rocket|Minion of Team Rocket
Saffron-City-Gym|Saffron City Gym
Rockets-Secret-Experiment|Rocket's Secret Experiment
Rockets-Minefield-Gym|Rocket's Minefield Gym
Blaine|Blaine
Koga|Koga
Giovanni|Giovanni
Giovannis-Last-Resort|Giovanni's Last Resort
Viridian-City-Gym|Viridian City Gym
Sabrina|Sabrina
"""

SETS = [
 dict(id="B02", name="Pokémon Jungle", kana="ポケモンジャングル · 第2弾", date="1er mars 1997", pk=313, base=38163,
      page="Pokemon-Jungle-Expansion", note="Deuxième set principal, centré sur les Pokémon de la jungle et les Évolitions.",
      cards=from_links(JUNGLE, {13,14,15,16,17,18,20,23,25,26,27,43,44,45,46,47}, {48:"Pokeacute-Ball"})),
 dict(id="B03", name="Mystery of the Fossils", kana="化石の秘密 · 第3弾", date="27 juin 1997", pk=314, base=38211,
      page="Mystery-of-the-Fossils-Expansion", note="Troisième set principal : fossiles, oiseaux légendaires et Mew en holo.",
      cards=from_links(FOSSIL, {7,9,22,23,24,25,26,30,31,32,33,39,40,41,42,43})),
 dict(id="B04", name="Rocket Gang", kana="ロケット団 · 第4弾", date="21 novembre 1997", pk=315, base=38259,
      page="Rocket-Gang-Expansion", note="Quatrième set principal, avec les premiers Pokémon Obscurs de la Team Rocket.",
      cards=from_links(ROCKET, {8,9,10,11,17,24,25,30,35,36,37,43,44,53,61,65})),
 dict(id="B05", name="Leaders' Stadium", kana="リーダーズスタジアム · ジム拡張第1弾", date="24 octobre 1998", pk=316, base=38324,
      page="Leaders-Stadium-Expansion", note="Premier set Gym : les Pokémon des champions Pierre, Ondine, Major Bob et Érika.",
      cards=from_links(LEADERS, {14,16,19,20,32,33,34,35,40,41,54,55,64,65,66,96})),
 dict(id="B06", name="Challenge from the Darkness", kana="闇からの挑戦 · ジム拡張第2弾", date="25 juin 1999", pk=317, base=38420,
      page="Challenge-from-the-Darkness-Expansion", note="Second set Gym : Morgane, Koga, Auguste et Giovanni entrent en scène.",
      cards=from_links(CHALLENGE, {17,18,21,32,34,35,40,41,42,53,54,55,61,71,72,95})),
]
expected = {"B02":48,"B03":48,"B04":65,"B05":96,"B06":98}
for s in SETS:
    assert len(s["cards"]) == expected[s["id"]], (s["id"], len(s["cards"]))
    assert sum(1 for c in s["cards"] if len(c) > 5 and c[5]) == 16, s["id"]
unknown = sorted({c[1] for s in SETS for c in s["cards"] if c[4] in "TE" and not c[2]})
print("Dresseurs/énergies gardés en anglais:", len(unknown), file=sys.stderr)
out = "const EXTRA_SETS=" + json.dumps(SETS, ensure_ascii=False, separators=(",", ":")) + ";"
open(sys.argv[1], "w").write(out)
print("ok", sum(len(s["cards"]) for s in SETS), file=sys.stderr)
