
class Gegner:
    def __init__ (self, name, hp, attacken):
        self.name = name
        self.hp = hp
        self.attacken = attacken

    def vorstellen(self):
        print(f"Ich bin {self.name} und habe {self.hp} HP.")

    def schaden_nehmen(self, menge):
        self.hp = self.hp - menge
        if self.hp > 0:
            print(f"{self.name} hat {menge} Schaden genommen und jetzt noch {self.hp} HP.")
        else:
            print(f"{self.name} hat {menge} Schaden genommen und ist jetzt tot")

    def angreifen(self, target, art = "1"):
        print(f"{self.name} greift {target.name} an")

        target.schaden_nehmen(self.attacken[art]["schaden"])





def gewinner(option1, option2):
    if option1.hp > 0:
        print(f"{option1.name} hat gewonnen")
    else:
        print(f"{option2.name} hat gewonnen")

spieler = Gegner("Spieler", 100, {"1": {"name": "Standardangriff", "schaden": 20},
                                "2":{"name": "Starker Angriff", "schaden": 35}})
goblin = Gegner("Goblin", 70, {"1":{"name": "Standardangriff", "schaden": 30}})




while spieler.hp > 0 and goblin.hp > 0:
    print("Welche Angriffmethode?")
    for nummer, attacke in spieler.attacken.items():
        print (f"{nummer}: {attacke['name']}")
    weg = input()
    while weg not in spieler.attacken:
        weg = input("Kein Option, nochmal: ")
    spieler.angreifen(goblin, weg)
    if goblin.hp <= 0:
        break
    goblin.angreifen(spieler)

gewinner(spieler, goblin)