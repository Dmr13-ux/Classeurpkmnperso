"""Génère les onglets thématiques (Caninos/Arcanin, Miaouss/Persian) pour le classeur.
Cartes internationales : API pokemontcg.io (images + dates). Cartes japonaises vintage : clés des sets du classeur."""
import json, re, sys

RAW = {}
RAW["growlithe"] = """
base1-28|Growlithe|28|Uncommon|Base|1999/01/09
base4-42|Growlithe|42|Uncommon|Base Set 2|2000/02/24
gym1-35|Blaine's Growlithe|35|Uncommon|Gym Heroes|2000/08/14
gym1-62|Blaine's Growlithe|62|Common|Gym Heroes|2000/08/14
gym2-62|Blaine's Growlithe|62|Common|Gym Challenge|2000/10/16
neo4-68|Growlithe|68|Common|Neo Destiny|2002/02/28
base6-45|Growlithe|45|Uncommon|Legendary Collection|2002/05/24
ecard2-51|Growlithe|51|Uncommon|Aquapolis|2003/01/15
ecard2-80|Growlithe|80|Common|Aquapolis|2003/01/15
ecard3-62|Growlithe|62|Common|Skyridge|2003/05/12
ex2-65|Growlithe|65|Common|Sandstorm|2003/09/18
ex6-64|Growlithe|64|Common|FireRed & LeafGreen|2004/09/01
ex12-55|Growlithe|55|Common|Legend Maker|2006/02/01
tk2b-4|Growlithe|4|-|EX Trainer Kit 2 Minun|2006/03/01
dp3-89|Growlithe|89|Common|Secret Wonders|2007/11/01
pl2-63|Growlithe|63|Common|Rising Rivals|2009/05/16
pl3-108|Growlithe|108|Common|Supreme Victors|2009/08/19
hgss1-65|Growlithe|65|Common|HeartGold & SoulSilver|2010/02/10
bw4-10|Growlithe|10|Common|Next Destinies|2012/02/08
bw4-11|Growlithe|11|Common|Next Destinies|2012/02/08
bw11-RC4|Growlithe|RC4|Uncommon|Legendary Treasures|2013/11/06
xy9-10|Growlithe|10|Common|BREAKpoint|2016/02/03
xy12-17|Growlithe|17|Common|Evolutions|2016/11/02
sm1-21|Growlithe|21|Common|Sun & Moon|2017/02/03
mcd18-1|Growlithe|1|-|McDonald's Collection 2018|2018/10/16
sm10-21|Growlithe|21|Common|Unbroken Bonds|2019/05/03
swsh2-27|Growlithe|27|Common|Rebel Clash|2020/05/01
swsh8-32|Growlithe|32|Common|Fusion Strike|2021/11/12
swsh10-70|Hisuian Growlithe|70|Common|Astral Radiance|2022/05/27
mcd22-4|Growlithe|4|-|McDonald's Collection 2022|2022/08/03
swsh11-83|Hisuian Growlithe|83|Common|Lost Origin|2022/09/09
swsh12-19|Growlithe|19|Common|Silver Tempest|2022/11/11
svp-24|Growlithe|24|Promo|Scarlet & Violet Black Star Promos|2023/01/01
sv1-30|Growlithe|30|Common|Scarlet & Violet|2023/03/31
sv1-31|Growlithe|31|Common|Scarlet & Violet|2023/03/31
sv3pt5-58|Growlithe|58|Common|151|2023/09/22
sv6-99|Hisuian Growlithe|99|Common|Twilight Masquerade|2024/05/24
sv6-181|Hisuian Growlithe|181|Illustration Rare|Twilight Masquerade|2024/05/24
sv10-27|Growlithe|27|Common|Destined Rivals|2025/05/30
"""
RAW["arcanine"] = """
base1-23|Arcanine|23|Uncommon|Base|1999/01/09
basep-6|Arcanine|6|Promo|Wizards Black Star Promos|1999/07/01
base4-33|Arcanine|33|Uncommon|Base Set 2|2000/02/24
gym2-1|Blaine's Arcanine|1|Rare Holo|Gym Challenge|2000/10/16
neo4-12|Light Arcanine|12|Rare Holo|Neo Destiny|2002/02/28
base6-36|Arcanine|36|Uncommon|Legendary Collection|2002/05/24
ecard2-2|Arcanine|2|Rare|Aquapolis|2003/01/15
ecard2-H2|Arcanine|H2|Rare Holo|Aquapolis|2003/01/15
ecard3-3|Arcanine|3|Rare|Skyridge|2003/05/12
ecard3-H2|Arcanine|H2|Rare Holo|Skyridge|2003/05/12
ex2-15|Arcanine|15|Rare|Sandstorm|2003/09/18
ex6-18|Arcanine|18|Rare|FireRed & LeafGreen|2004/09/01
ex12-83|Arcanine ex|83|Rare Holo EX|Legend Maker|2006/02/01
tk2b-1|Arcanine|1|-|EX Trainer Kit 2 Minun|2006/03/01
dp3-22|Arcanine|22|Rare|Secret Wonders|2007/11/01
pl2-1|Arcanine|1|Rare Holo|Rising Rivals|2009/05/16
pl3-15|Arcanine G|15|Rare|Supreme Victors|2009/08/19
pl3-50|Arcanine|50|Uncommon|Supreme Victors|2009/08/19
hgss1-1|Arcanine|1|Rare Holo|HeartGold & SoulSilver|2010/02/10
bw4-12|Arcanine|12|Rare|Next Destinies|2012/02/08
bw4-13|Arcanine|13|Uncommon|Next Destinies|2012/02/08
xyp-XY180|Arcanine BREAK|XY180|Promo|XY Black Star Promos|2016/02/03
xy9-11|Arcanine|11|Uncommon|BREAKpoint|2016/02/03
xy12-18|Arcanine|18|Rare|Evolutions|2016/11/02
sm1-22|Arcanine|22|Rare Holo|Sun & Moon|2017/02/03
det1-6|Arcanine|6|Rare|Detective Pikachu|2019/04/05
sm10-22|Arcanine|22|Rare Holo|Unbroken Bonds|2019/05/03
swshp-SWSH304|Arcanine|SWSH304|Promo|SWSH Black Star Promos|2022/11/11
swsh2-28|Arcanine|28|Rare|Rebel Clash|2020/05/01
swsh8-33|Arcanine|33|Rare|Fusion Strike|2021/11/12
swsh10-71|Hisuian Arcanine|71|Rare|Astral Radiance|2022/05/27
swsh11tg-TG08|Hisuian Arcanine|TG08|Trainer Gallery Rare Holo|Lost Origin Trainer Gallery|2022/09/09
swsh11-84|Hisuian Arcanine|84|Rare Holo|Lost Origin|2022/09/09
swsh12-20|Arcanine|20|Rare|Silver Tempest|2022/11/11
swsh12-90|Hisuian Arcanine V|90|Rare Holo V|Silver Tempest|2022/11/11
swsh12-179|Hisuian Arcanine V|179|Rare Ultra|Silver Tempest|2022/11/11
svp-11|Arcanine|11|Promo|Scarlet & Violet Black Star Promos|2023/01/01
sv1-32|Arcanine ex|32|Double Rare|Scarlet & Violet|2023/03/31
sv1-224|Arcanine ex|224|Ultra Rare|Scarlet & Violet|2023/03/31
sv3pt5-59|Arcanine|59|Uncommon|151|2023/09/22
sv6-100|Hisuian Arcanine|100|Rare|Twilight Masquerade|2024/05/24
sv10-28|Arcanine|28|Uncommon|Destined Rivals|2025/05/30
"""
RAW["meowth"] = """
base2-56|Meowth|56|Common|Jungle|1999/06/16
basep-10|Meowth|10|Promo|Wizards Black Star Promos|1999/07/01
basep-18|Team Rocket's Meowth|18|Promo|Wizards Black Star Promos|1999/07/01
base4-80|Meowth|80|Common|Base Set 2|2000/02/24
base5-62|Meowth|62|Common|Team Rocket|2000/04/24
gym2-43|Giovanni's Meowth|43|Uncommon|Gym Challenge|2000/10/16
gym2-74|Giovanni's Meowth|74|Common|Gym Challenge|2000/10/16
base6-53|Meowth|53|Uncommon|Legendary Collection|2002/05/24
ecard1-121|Meowth|121|Common|Expedition Base Set|2002/09/15
ecard3-78|Meowth|78|Common|Skyridge|2003/05/12
np-13|Meowth|13|Promo|Nintendo Black Star Promos|2003/10/01
ex4-42|Meowth|42|Common|Team Magma vs Team Aqua|2004/03/01
ex6-69|Meowth|69|Common|FireRed & LeafGreen|2004/09/01
ex7-46|Rocket's Meowth|46|Uncommon|Team Rocket Returns|2004/11/01
ex11-77|Meowth|77|Common|Delta Species|2005/10/31
tk2a-4|Meowth|4|-|EX Trainer Kit 2 Plusle|2006/03/01
ex13-71|Meowth δ|71|Common|Holon Phantoms|2006/05/01
pop5-11|Meowth δ|11|Common|POP Series 5|2007/03/01
dp6-106|Meowth|106|Common|Legends Awakened|2008/08/01
pl3-114|Meowth|114|Common|Supreme Victors|2009/08/19
hgss1-75|Meowth|75|Common|HeartGold & SoulSilver|2010/02/10
bwp-BW35|Meowth|BW35|Promo|BW Black Star Promos|2011/03/01
bw3-102|Meowth|102|Rare Secret|Noble Victories|2011/11/16
bw4-80|Meowth|80|Common|Next Destinies|2012/02/08
bw7-106|Meowth|106|Common|Boundaries Crossed|2012/11/07
xy6-67|Meowth|67|Common|Roaring Skies|2015/05/06
xy7-61|Meowth|61|Common|Ancient Origins|2015/08/12
xy8-114|Meowth|114|Common|BREAKthrough|2015/11/04
g1-53|Meowth|53|Common|Generations|2016/02/22
xy10-74|Meowth|74|Common|Fates Collide|2016/05/02
xy11-88|Meowth|88|Common|Steam Siege|2016/08/03
mcd16-11|Meowth|11|-|McDonald's Collection 2016|2016/08/19
smp-SM43|Alolan Meowth|SM43|Promo|SM Black Star Promos|2017/02/03
smp-SM51|Alolan Meowth|SM51|Promo|SM Black Star Promos|2017/02/03
sm1-78|Alolan Meowth|78|Common|Sun & Moon|2017/02/03
sm3-101|Meowth|101|Common|Burning Shadows|2017/08/05
mcd17-8|Alolan Meowth|8|-|McDonald's Collection 2017|2017/11/07
sm8-118|Alolan Meowth|118|Common|Lost Thunder|2018/11/02
sm9-125|Meowth|125|Common|Team Up|2019/02/01
sm10-147|Meowth|147|Common|Unbroken Bonds|2019/05/03
mcd19-10|Alolan Meowth|10|-|McDonald's Collection 2019|2019/10/15
sm12-128|Alolan Meowth|128|Common|Cosmic Eclipse|2019/11/01
swshp-SWSH004|Meowth V|SWSH004|Promo|SWSH Black Star Promos|2019/11/15
swshp-SWSH005|Meowth VMAX|SWSH005|Promo|SWSH Black Star Promos|2019/11/15
swsh1-127|Galarian Meowth|127|Common|Sword & Shield|2020/02/07
swsh2-126|Galarian Meowth|126|Common|Rebel Clash|2020/05/01
swsh4-112|Galarian Meowth|112|Common|Vivid Voltage|2020/11/13
swsh45sv-SV086|Galarian Meowth|SV086|Rare Shiny|Shining Fates Shiny Vault|2021/02/19
swsh8-180|Galarian Meowth|180|Common|Fusion Strike|2021/11/12
swsh8-199|Meowth|199|Common|Fusion Strike|2021/11/12
swsh12pt5-84|Galarian Meowth|84|Common|Crown Zenith|2023/01/20
sv3pt5-52|Meowth|52|Common|151|2023/09/22
sv6pt5-48|Meowth|48|Common|Shrouded Fable|2024/08/02
sv10-149|Team Rocket's Meowth|149|Common|Destined Rivals|2025/05/30
sv10-203|Team Rocket's Meowth|203|Illustration Rare|Destined Rivals|2025/05/30
me2-106|Meowth|106|Illustration Rare|Phantasmal Flames|2025/11/14
me2pt5-161|Team Rocket's Meowth|161|Common|Ascended Heroes|2026/01/30
me3-62|Meowth ex|62|Double Rare|Perfect Order|2026/03/27
me3-107|Meowth ex|107|Ultra Rare|Perfect Order|2026/03/27
me3-121|Meowth ex|121|Special Illustration Rare|Perfect Order|2026/03/27
me55-89|Alolan Meowth|89|Common|30th Celebration|2026/09/16
me55-101|Galarian Meowth|101|Common|30th Celebration|2026/09/16
me55-113|Meowth|113|Common|30th Celebration|2026/09/16
me55-139|Alolan Meowth|139|Illustration Rare|30th Celebration|2026/09/16
me55-141|Galarian Meowth|141|Illustration Rare|30th Celebration|2026/09/16
me55-144|Meowth|144|Illustration Rare|30th Celebration|2026/09/16
"""
RAW["persian"] = """
base2-42|Persian|42|Uncommon|Jungle|1999/06/16
basep-17|Dark Persian|17|Promo|Wizards Black Star Promos|1999/07/01
base4-56|Persian|56|Uncommon|Base Set 2|2000/02/24
base5-42|Dark Persian|42|Uncommon|Team Rocket|2000/04/24
gym2-8|Giovanni's Persian|8|Rare Holo|Gym Challenge|2000/10/16
base6-6|Dark Persian|6|Rare Holo|Legendary Collection|2002/05/24
ecard3-42|Persian|42|Uncommon|Skyridge|2003/05/12
ex6-44|Persian|44|Uncommon|FireRed & LeafGreen|2004/09/01
ex10-116|Rocket's Persian ex|116|Rare Secret|Unseen Forces|2005/08/01
ex11-50|Persian|50|Uncommon|Delta Species|2005/10/31
ex13-48|Persian δ|48|Uncommon|Holon Phantoms|2006/05/01
dp6-68|Persian|68|Uncommon|Legends Awakened|2008/08/01
hgss1-27|Persian|27|Rare|HeartGold & SoulSilver|2010/02/10
bw4-81|Persian|81|Rare|Next Destinies|2012/02/08
xy7-62|Persian|62|Common|Ancient Origins|2015/08/12
g1-54|Persian|54|Uncommon|Generations|2016/02/22
xy11-89|Persian|89|Uncommon|Steam Siege|2016/08/03
sm1-79|Alolan Persian|79|Uncommon|Sun & Moon|2017/02/03
smp-SM182|Persian|SM182|Promo|SM Black Star Promos|2019/05/03
sm3-102|Persian|102|Rare|Burning Shadows|2017/08/05
sm8-119|Alolan Persian|119|Rare|Lost Thunder|2018/11/02
sm9-126|Persian|126|Uncommon|Team Up|2019/02/01
sm10-148|Persian|148|Rare|Unbroken Bonds|2019/05/03
sm10-149|Persian-GX|149|Rare Holo GX|Unbroken Bonds|2019/05/03
sm10-207|Persian-GX|207|Rare Ultra|Unbroken Bonds|2019/05/03
sm10-227|Persian-GX|227|Rare Rainbow|Unbroken Bonds|2019/05/03
sm12-129|Alolan Persian-GX|129|Rare Holo GX|Cosmic Eclipse|2019/11/01
sm12-219|Alolan Persian-GX|219|Rare Ultra|Cosmic Eclipse|2019/11/01
sm12-257|Alolan Persian-GX|257|Rare Rainbow|Cosmic Eclipse|2019/11/01
swsh8-200|Persian|200|Uncommon|Fusion Strike|2021/11/12
sv3pt5-53|Persian|53|Uncommon|151|2023/09/22
sv6pt5-49|Persian|49|Common|Shrouded Fable|2024/08/02
sv6pt5-78|Persian|78|Illustration Rare|Shrouded Fable|2024/08/02
sv10-150|Team Rocket's Persian ex|150|Double Rare|Destined Rivals|2025/05/30
sv10-219|Team Rocket's Persian ex|219|Ultra Rare|Destined Rivals|2025/05/30
"""
RAW["perrserker"] = """
swshp-SWSH008|Galarian Perrserker|SWSH008|Promo|SWSH Black Star Promos|2019/11/15
swsh1-128|Galarian Perrserker|128|Rare Holo|Sword & Shield|2020/02/07
swsh2-127|Galarian Perrserker|127|Rare|Rebel Clash|2020/05/01
swsh2-205|Galarian Perrserker|205|Rare Secret|Rebel Clash|2020/05/01
swsh4-113|Galarian Perrserker|113|Rare|Vivid Voltage|2020/11/13
swsh45sv-SV087|Galarian Perrserker|SV087|Rare Shiny|Shining Fates Shiny Vault|2021/02/19
swsh8-181|Galarian Perrserker|181|Uncommon|Fusion Strike|2021/11/12
swsh11-129|Galarian Perrserker V|129|Rare Holo V|Lost Origin|2022/09/09
swsh11-183|Galarian Perrserker V|183|Rare Ultra|Lost Origin|2022/09/09
swsh11-184|Galarian Perrserker V|184|Rare Ultra|Lost Origin|2022/09/09
swsh12pt5-85|Galarian Perrserker|85|Rare|Crown Zenith|2023/01/20
"""
# Les dates des promos SWSH/SM varient selon la carte : on garde celle de l'API sauf pour deux promos sorties plus tard
# (corrigées ci-dessus : XY180 en 2016, SWSH304 en 2022, SM182 en 2019).

SPECIES = {"Growlithe":("Caninos",58,"F"),"Arcanine":("Arcanin",59,"F"),"Meowth":("Miaouss",52,"C"),
           "Persian":("Persian",53,"C"),"Perrserker":("Berserkatt",863,"M")}
PREFIX = [("Team Rocket's ","de la Team Rocket"),("Rocket's ","de Rocket"),("Blaine's ","d'Auguste"),("Giovanni's ","de Giovanni"),
          ("Hisuian ","de Hisui"),("Alolan ","d'Alola"),("Galarian ","de Galar"),("Dark ","Obscur"),("Light ","Lumineux")]
HOLO_WORDS = ("Holo","Rare Secret","Ultra","Rainbow","Shiny","Illustration","Double Rare","Gallery")

def fr_name(en):
    rest, owner, forms = en, None, []
    for p, f in PREFIX:
        if rest.startswith(p):
            rest = rest[len(p):]
            if p.endswith("'s "): owner = f
            else: forms.append(f)
    m = re.match(r"(Growlithe|Arcanine|Meowth|Persian|Perrserker)(.*)", rest)
    base, suffix = m.group(1), m.group(2).strip()
    suffix = suffix.lstrip("-").strip()
    name = SPECIES[base][0]
    for f in forms:  # Obscur/Lumineux s'accolent, les formes régionales suivent
        name += " " + f
    if suffix: name += " " + suffix
    if owner: name += " " + owner
    return name, base

def img_url(cid, sid, n):
    # Les extensions Méga-Évolution (identifiants « me… », 2025-2026) ont leurs images chez Scrydex :
    # l'ancienne adresse pokemontcg.io renvoie un dos de carte pour elles.
    if sid.startswith("me"):
        return f"https://images.scrydex.com/pokemon/{cid}/small"
    return f"https://images.pokemontcg.io/{sid}/{n}.png"

def parse(key):
    rows = []
    for line in RAW[key].strip().splitlines():
        cid, en, num, rar, setname, date = line.split("|")
        fr, base = fr_name(en)
        sid, n = cid.rsplit("-", 1) if not cid.startswith("swsh11tg") else ("swsh11tg", cid.split("-",1)[1])
        sid = cid[:cid.index("-")]
        n = cid[cid.index("-")+1:]
        holo = any(w in rar for w in HOLO_WORDS) or bool(re.search(r"\b(ex|EX|GX|V|VMAX|BREAK)\b", en))
        rows.append(dict(key="EN-"+cid, en=en, fr=fr, dex=SPECIES[base][1], type=SPECIES[base][2], holo=holo,
                         set=setname, date=date.replace("/","-"), num=num, rarity=rar if rar not in "-—(none)" else "",
                         img=img_url(cid, sid, n), lang="EN"))
    return rows

# Cartes japonaises récentes pas encore sorties à l'international (images Pokellector)
JP_EXTRA = {
  "can": [
    dict(key="JP-M6-10", en="Growlithe", set="Storm Emeralda", date="2026-07-31", num="010", rarity="Common",
         img="https://den-cards.pokellector.com/437/Growlithe.M6.10.61938.png", url="https://jp.pokellector.com/Storm-Emeralda-Expansion/Growlithe-Card-10"),
    dict(key="JP-M6-11", en="Arcanine", set="Storm Emeralda", date="2026-07-31", num="011", rarity="Rare",
         img="https://den-cards.pokellector.com/437/Arcanine.M6.11.61939.png", url="https://jp.pokellector.com/Storm-Emeralda-Expansion/Arcanine-Card-11"),
    dict(key="JP-M6-78", en="Growlithe", set="Storm Emeralda", date="2026-07-31", num="078", rarity="Art Rare",
         img="https://den-cards.pokellector.com/437/Growlithe.M6.78.62006.png", url="https://jp.pokellector.com/Storm-Emeralda-Expansion/Growlithe-Card-78"),
  ],
  "mia": [],
}
def jp_extra(rows):
    out = []
    for r in rows:
        fr, base = fr_name(r["en"])
        out.append(dict(r, fr=fr, dex=SPECIES[base][1], type=SPECIES[base][2], lang="JP",
                        holo=any(w in r["rarity"] for w in HOLO_WORDS+("Art Rare",))))
    return out

THEMES = [
  dict(id="TH-CAN", name="Caninos & Arcanin", kana="ガーディ · ウインディ", species=["Growlithe","Arcanine"],
       note="Toutes les cartes Caninos et Arcanin, formes de Hisui, ex, V et BREAK comprises, de la plus ancienne à la plus récente.",
       jp=[("EXP",18),("EXP",19),("B06",27),("B06",34)], en=parse("growlithe")+parse("arcanine")+jp_extra(JP_EXTRA["can"])),
  dict(id="TH-MIA", name="Miaouss & Persian", kana="ニャース · ペルシアン", species=["Meowth","Persian","Perrserker"],
       note="Toutes les cartes Miaouss, Persian et Berserkatt, formes d'Alola et de Galar, ex, GX, V et VMAX comprises, de la plus ancienne à la plus récente.",
       jp=[("B02",36),("B02",39),("B04",47),("B04",48),("B06",63),("B06",68),("B06",71)], en=parse("meowth")+parse("persian")+parse("perrserker")+jp_extra(JP_EXTRA["mia"])),
]
for t in THEMES:
    t["en"].sort(key=lambda c: (c["date"], c["set"], c["num"].zfill(4)))
print("const THEMES=" + json.dumps(THEMES, ensure_ascii=False, separators=(",", ":")) + ";", file=open(sys.argv[1], "w"))
for t in THEMES:
    print(t["id"], len(t["en"]), "internationales +", len(t["jp"]), "jap", file=sys.stderr)
    print("  ex.", [c["fr"] for c in t["en"] if c["holo"]][:8], file=sys.stderr)

# ---------------------------------------------------------------------------
# Onglet « Baby Shiny » : shiny simples (sans GX/V/VMAX/ex) de Destins Occultes, Destinées Radieuses et Destinées de Paldea
from fr_names import FR
TYPE_CODE = {"Grass":"G","Fire":"F","Water":"W","Lightning":"L","Psychic":"P","Fighting":"Fi","Darkness":"D",
             "Metal":"M","Fairy":"Y","Dragon":"N","Colorless":"C"}
def ranges(spec):
    out = {}
    for part in spec.split(","):
        rng, t = part.split("=")
        a, b = (rng.split("-") + [rng])[:2]
        for n in range(int(a), int(b) + 1): out[n] = t
    return out
TYPES_BY_SET = {
  "sma": ranges("1-5=Grass,6-7=Fire,8-12=Water,13-14=Lightning,15-19=Psychic,20-24=Fighting,25-26=Darkness,27-33=Metal,34-36=Fairy,37-40=Dragon,41-45=Colorless"),
  "swsh45sv": ranges("1-14=Grass,15-19=Fire,20-37=Water,38-46=Lightning,47-62=Psychic,63-75=Fighting,76-85=Darkness,86-92=Metal,93-104=Colorless"),
  "sv4pt5": ranges("92-108=Grass,109-115=Fire,116-130=Water,131-146=Lightning,147-168=Psychic,169-179=Fighting,180-190=Darkness,191-193=Metal,194-195=Dragon,196-211=Colorless"),
}
REGION = {"Alolan":"d'Alola","Galarian":"de Galar","Paldean":"de Paldea"}
TAUROS_RACE = {111:" (race Flamboyante)",120:" (race Aquatique)",172:" (race Combative)"}
shiny = []
for line in open("shiny_raw.txt", encoding="utf-8"):
    sid, date, setfr, items = line.strip().split("|")
    for it in items.split(","):
        num, en = it.split(":", 1)
        n = int(re.sub(r"\D", "", num))
        region = None
        m = re.match(r"(Alolan|Galarian|Paldean) (.+)", en)
        base = m.group(2) if m else en
        if m: region = REGION[m.group(1)]
        fr, dex = FR[base]
        if region: fr += " " + region
        if sid == "sv4pt5" and n in TAUROS_RACE: fr += TAUROS_RACE[n]
        total = {"sma": "", "swsh45sv": "", "sv4pt5": "/091"}[sid]
        shiny.append(dict(key=f"EN-{sid}-{num}", en=en, fr=fr, dex=dex, type=TYPE_CODE[TYPES_BY_SET[sid][n]], holo=True,
                          set=setfr, date=date, num=num + total, rarity="Shiny", img=f"https://images.pokemontcg.io/{sid}/{num}.png", lang="EN"))
# Pokémon Radieux (shiny dans un cadre simple) ajoutés à la demande
RADIANT = [
  dict(key="EN-pgo-11", en="Radiant Charizard", fr="Dracaufeu Radieux", dex=6, type="F", holo=True, set="Pokémon GO",
       date="2022-07-01", num="011/078", rarity="Radiant Rare", img="https://images.pokemontcg.io/pgo/11.png", lang="EN"),
  dict(key="EN-swsh12pt5-20", en="Radiant Charizard", fr="Dracaufeu Radieux", dex=6, type="F", holo=True, set="Zénith Suprême",
       date="2023-01-20", num="020/159", rarity="Radiant Rare", img="https://images.pokemontcg.io/swsh12pt5/20.png", lang="EN"),
]
RADIANT += [dict(key=f"EN-{sid}-{n}", en=en, fr=fr, dex=dex, type=t, holo=True, set=setfr, date=date, num=num,
                 rarity="Radiant Rare", img=f"https://images.pokemontcg.io/{sid}/{n}.png", lang="EN")
  for sid,n,en,fr,dex,t,setfr,date,num in [
  ("swsh10","27","Radiant Heatran","Heatran Radieux",485,"F","Astres Radieux","2022-05-27","027/189"),
  ("swsh10","46","Radiant Greninja","Amphinobi Radieux",658,"W","Astres Radieux","2022-05-27","046/189"),
  ("swsh10","81","Radiant Hawlucha","Brutalibré Radieux",701,"Fi","Astres Radieux","2022-05-27","081/189"),
  ("pgo","4","Radiant Venusaur","Florizarre Radieux",3,"G","Pokémon GO","2022-07-01","004/078"),
  ("pgo","18","Radiant Blastoise","Tortank Radieux",9,"W","Pokémon GO","2022-07-01","018/078"),
  ("swsh11","69","Radiant Gardevoir","Gardevoir Radieux",282,"P","Origine Perdue","2022-09-09","069/196"),
  ("swsh11","123","Radiant Hisuian Sneasler","Farfurex de Hisui Radieux",903,"D","Origine Perdue","2022-09-09","123/196"),
  ("swsh11","124","Radiant Steelix","Steelix Radieux",208,"M","Origine Perdue","2022-09-09","124/196"),
  ("swshp","SWSH230","Radiant Eevee","Évoli Radieux",133,"C","Promos Black Star EB","2022-09-30","SWSH230"),
  ("swsh12","16","Radiant Tsareena","Sucreine Radieuse",763,"G","Tempête Argentée","2022-11-11","016/195"),
  ("swsh12","59","Radiant Alakazam","Alakazam Radieux",65,"P","Tempête Argentée","2022-11-11","059/195"),
  ("swsh12","120","Radiant Jirachi","Jirachi Radieux",385,"M","Tempête Argentée","2022-11-11","120/195"),
  ("swsh12pt5","51","Radiant Charjabug","Chrysapile Radieux",737,"L","Zénith Suprême","2023-01-20","051/159"),
  ("swsh12pt5","105","Radiant Eternatus","Éthernatos Radieux",890,"D","Zénith Suprême","2023-01-20","105/159"),
  ]]
shiny += RADIANT
shiny.sort(key=lambda c: (c["date"], c["set"], c["num"].replace("SV","").zfill(8)))
THEMES.append(dict(id="TH-SHINY", name="Baby Shiny", kana="色違い · ひかるポケモン", species=[],
    note="Les shiny simples des trois extensions « Destin(ée)s » : Destins Occultes (SV1 à SV45), Destinées Radieuses (SV001 à SV104) et Destinées de Paldea (092 à 211), plus les 16 Pokémon Radieux. Sans les GX, V, VMAX ni ex.",
    jp=[], en=shiny))
print("const THEMES=" + json.dumps(THEMES, ensure_ascii=False, separators=(",", ":")) + ";", file=open(sys.argv[1], "w"))
print("TH-SHINY", len(shiny), "cartes ;", sum(1 for c in shiny if c["set"]=="Destinées de Paldea"), "Paldea", file=sys.stderr)
