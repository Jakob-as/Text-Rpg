class Gegner:
    def __init__ (self, name, hp, attacken, mana, max_hp):
        self.name = name
        self.hp = hp
        self.attacken = attacken
        self.mana = mana
        self.max_hp = max_hp
    def vorstellen(self):
        print(f"Ich bin {self.name} und habe {self.hp} HP.")

    def heilen(self, menge):
        x = min(menge, self.max_hp-self.hp)
        self.hp = self.hp + x
        print(f"{self.name} hat sich um {x} HP geheilt und hat jetzt {self.hp} HP.")

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

spieler = Gegner("Spieler", 100, {"1": {"name": "Standardangriff", "schaden": 20, "gov": 10}, #gov = Gewinn oder Verlust
                                "2":{"name": "Starker Angriff", "schaden": 35, "gov": -20},
                                "3":{"name": "Heilung", "heilung": 30, "gov": -15}}, 35, 100)
goblin = Gegner("Goblin", 70, {"1":{"name": "Standardangriff", "schaden": 30, "gov": 0}}, 9999, 70)




while spieler.hp > 0 and goblin.hp > 0:
    print("Welche Angriffmethode?")
    for nummer, attacke in spieler.attacken.items():
        x = attacke.get("schaden", attacke.get("heilung"))
        print (f"{nummer}: {attacke['name']} ({x}); Mana: ({attacke['gov']})")
    print (f"Mana: {spieler.mana}")
    weg = input()
    while weg not in spieler.attacken or spieler.mana + spieler.attacken[weg]["gov"] < 0:
        weg = input("Keine Option oder zu wenig Mana, nochmal: ")
    
    spieler.angreifen(goblin, weg)
    if goblin.hp <= 0:
        break
    goblin.angreifen(spieler)

gewinner(spieler, goblin)