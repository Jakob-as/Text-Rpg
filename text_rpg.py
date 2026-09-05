class Gegner:
    def __init__ (self, name, hp, attacken, mana, max_hp):
        self.name = name
        self.hp = hp
        self.attacken = attacken
        self.mana = mana
        self.max_hp = max_hp
    def vorstellen(self):
        print(f"Ich bin {self.name} und habe {self.hp} HP.")

    def heilen(self, menge, art = 1):
        x = min(menge, self.max_hp-self.hp)
        self.hp = self.hp + x
        if art == 1:
            print(f"{self.name} hat sich um {x} HP geheilt und hat jetzt {self.hp} HP.")
        elif art == 2:
            print(f"+{x} HP")            

    def schaden_nehmen(self, menge):
        self.hp = self.hp - menge
        if self.hp > 0:
            print(f"{self.name} hat {menge} Schaden genommen und jetzt noch {self.hp} HP.")
        else:
            print(f"{self.name} hat {menge} Schaden genommen und ist jetzt tot")

    def angreifen(self, target, art = "1"):
        if "schaden" in self.attacken[art]:
            print(f"{self.name} greift {target.name} an")
            target.schaden_nehmen(self.attacken[art]["schaden"])
        elif "heilung" in self.attacken[art]:
            self.heilen(self.attacken[art]["heilung"]) 
        self.mana = self.mana + self.attacken[art]["gov"]




def gewinner(option1, option2):
    if option1.hp > 0:
        print(f"{option1.name} hat gewonnen")
    else:
        print(f"{option2.name} hat gewonnen")

spieler = Gegner("Spieler", 100, {"1": {"name": "Standardangriff", "schaden": 120, "gov": 10}, #gov = Gewinn oder Verlust
                                "2":{"name": "Starker Angriff", "schaden": 35, "gov": -20},
                                "3":{"name": "Heilung", "heilung": 30, "gov": -15}}, 35, 100)

goblin = Gegner("Goblin", 70, {"1":{"name": "Standardangriff", "schaden": 30, "gov": 0}}, 9999, 70)
ritter = Gegner("Ritter", 120, {"1":{"name": "Standardangriff", "schaden": 35, "gov": 0}}, 9999, 120)
hexe = Gegner("Hexe", 90, {"1":{"name": "Standardangriff", "schaden": 20, "gov":0}}, 9999, 90)

gegner = {"1": goblin, "2": ritter, "3": hexe}


while spieler.hp > 0:
    if any(g.hp > 0 for g in gegner.values()) == False:
        break
    print ("Wähle deinen Gegner")
    for nummer, name in gegner.items():
        if name.hp > 0:
            print (f"{nummer}: {name.name} ({name.hp} HP)")
    wahl = input()
    while (wahl not in gegner.keys()) or gegner[wahl].hp <= 0:
        wahl = input("Kein Option")
    print (f"Dein Gegner ist {gegner[wahl].name}")
    while gegner[wahl].hp > 0 and spieler.hp > 0:    
        print("Welche Angriffmethode?")
        for nummer, attacke in spieler.attacken.items():
            x = attacke.get("schaden", attacke.get("heilung"))
            print (f"{nummer}: {attacke['name']} ({x}); Mana: ({attacke['gov']})")
        print (f"Mana: {spieler.mana}")
        weg = input()
        while weg not in spieler.attacken or spieler.mana + spieler.attacken[weg]["gov"] < 0:
            weg = input("Keine Option oder zu wenig Mana, nochmal: ")
        
        spieler.angreifen(gegner[wahl], weg)
        if gegner[wahl].hp <= 0:
            print("Als Belohung erhälst du: ")
            spieler.mana += gegner[wahl].attacken["1"]["schaden"]
            print (f"+{gegner[wahl].attacken["1"]["schaden"]} Mana")
            spieler.heilen(gegner[wahl].max_hp/2, 2)
            break
        gegner[wahl].angreifen(spieler)

gewinner(spieler, gegner[wahl])