```python
import random
from typing import List, Dict
import time

class SpiritualWarrior:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.holy_water = 5
        self.qi_energy = 100
        self.level = 1
        self.experience = 0
        self.golden_essence = 3  # Traditional Daoist essence
        self.splits_remaining = 2  # Number of split techniques available
        
    def use_holy_water(self, monster) -> str:
        if self.holy_water > 0:
            damage = random.randint(20, 30)
            monster.health -= damage
            self.holy_water -= 1
            return f"{self.name} used Holy Water! Dealt {damage} damage. {self.holy_water} holy water remaining."
        return "No holy water remaining!"

    def use_qi_technique(self, monster) -> str:
        if self.qi_energy >= 20:
            damage = random.randint(15, 25)
            monster.health -= damage
            self.qi_energy -= 20
            return f"{self.name} channeled Qi energy! Dealt {damage} damage. {self.qi_energy} Qi remaining."
        return "Not enough Qi energy!"

    def meditate(self) -> str:
        qi_restored = random.randint(10, 30)
        self.qi_energy = min(100, self.qi_energy + qi_restored)
        return f"{self.name} meditated and restored {qi_restored} Qi. Current Qi: {self.qi_energy}"
        
    def use_golden_essence(self, monster) -> str:
        if self.golden_essence > 0:
            damage = random.randint(30, 40)
            monster.health -= damage
            self.golden_essence -= 1
            return f"{self.name} used Golden Essence! Dealt {damage} damage. {self.golden_essence} essence remaining."
        return "No golden essence remaining!"
        
    def split_technique(self, monster) -> str:
        if self.splits_remaining > 0:
            self.splits_remaining -= 1
            damage = random.randint(25, 35)
            monster.health -= damage
            self.health += damage // 2  # Recover half the damage dealt
            return f"{self.name} performed Split Technique! Dealt {damage} damage and recovered {damage//2} health. {self.splits_remaining} splits remaining."
        return "No split techniques remaining!"

class Monster:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.health = 50 + (level * 10)
        self.base_health = self.health
        
    def attack(self, warrior: SpiritualWarrior) -> str:
        damage = random.randint(5, 10 + self.level * 2)
        warrior.health -= damage
        return f"{self.name} attacks {warrior.name} for {damage} damage!"

class GameWorld:
    def __init__(self):
        self.monster_types = [
            "Dark Spirit", "Wandering Ghost", "Shadow Beast",
            "Corrupted Qi Entity", "Chaos Manifestation"
        ]
    
    def generate_monster(self, player_level: int) -> Monster:
        name = random.choice(self.monster_types)
        level = max(1, player_level + random.randint(-1, 1))
        return Monster(name, level)

    def battle(self, warrior: SpiritualWarrior, monster: Monster):
        print(f"\nBattle begins! {warrior.name} vs Level {monster.level} {monster.name}")
        print("=" * 50)

        while warrior.health > 0 and monster.health > 0:
            print(f"\n{warrior.name} HP: {warrior.health} | Qi: {warrior.qi_energy} | Holy Water: {warrior.holy_water}")
            print(f"{monster.name} HP: {monster.health}")
            
            # Player turn
            print("\nChoose your action:")
            print("1. Use Holy Water")
            print("2. Use Qi Technique")
            print("3. Meditate")
            print("4. Use Golden Essence")
            print("5. Split Technique")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                print(warrior.use_holy_water(monster))
            elif choice == "2":
                print(warrior.use_qi_technique(monster))
            elif choice == "3":
                print(warrior.meditate())
            elif choice == "4":
                print(warrior.use_golden_essence(monster))
            elif choice == "5":
                print(warrior.split_technique(monster))
            else:
                print("Invalid choice! Turn skipped.")
            
            if monster.health <= 0:
                print(f"\nVictory! {monster.name} has been defeated!")
                exp_gain = 10 * monster.level
                warrior.experience += exp_gain
                print(f"Gained {exp_gain} experience!")
                
                # Level up check
                if warrior.experience >= warrior.level * 100:
                    warrior.level += 1
                    warrior.experience = 0
                    warrior.holy_water += 2
                    print(f"\nLevel Up! {warrior.name} is now level {warrior.level}!")
                    print("Received 2 Holy Water as a blessing!")
                return True
            
            # Monster turn
            print("\n" + monster.attack(warrior))
            
            if warrior.health <= 0:
                print(f"\nDefeat! {warrior.name} has fallen in battle.")
                return False
            
            time.sleep(1)  # Add slight delay for better readability

def show_signature():
    signature = '''
    ===============================================
           Spiritual Monster Fighter v1.0
    -----------------------------------------------
    "Ask not what your spirit can do for you,
     but what you can do for your spirit."
                        - Inspired by JFK, 1961
    
    A fusion of Eastern and Western spiritual arts
    Blessed by holy water, empowered by golden qi
    -----------------------------------------------
    Game Design: JFK (Journey for Knowledge)
    Released: 2025
    ===============================================
    '''
    print(signature)

def main():
    show_signature()
    print("Welcome to Spiritual Monster Fighter!")
    player_name = input("Enter your warrior's name: ")
    warrior = SpiritualWarrior(player_name)
    game_world = GameWorld()
    
    while warrior.health > 0:
        monster = game_world.generate_monster(warrior.level)
        game_world.battle(warrior, monster)
        
        if warrior.health <= 0:
            print("\nGame Over!")
            break
            
        choice = input("\nContinue fighting? (y/n): ")
        if choice.lower() != 'y':
            print(f"\nFarewell, brave warrior {warrior.name}!")
            break

        # Restore some health and qi between battles
        warrior.health = min(100, warrior.health + 30)
        warrior.qi_energy = min(100, warrior.qi_energy + 50)
        print("\nRested and recovered some health and Qi.")

if __name__ == "__main__":
    main()
```
