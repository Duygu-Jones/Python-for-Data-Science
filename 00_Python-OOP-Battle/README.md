# Python OOP Battle Game

A beginner-friendly Python project that teaches Object-Oriented Programming (OOP) concepts through a simple turn-based battle game. Heroes fight enemies using weapons, inheritance, and special abilities.

---

## Table of Contents

- [About the Project](#about-the-project)
- [OOP Concepts Covered](#oop-concepts-covered)
- [Project Structure](#project-structure)
- [Classes Overview](#classes-overview)
- [How the Battle Works](#how-the-battle-works)
- [Getting Started](#getting-started)
- [Example Output](#example-output)
- [What You Will Learn](#what-you-will-learn)
- [Author](#author)

---

## About the Project

This project is a hands-on OOP practice exercise built around a small text-based battle game. A `Hero` equipped with a `Weapon` faces off against enemies like `Zombie` and `Ogre`. Each enemy has its own special attack with random effects, making every battle slightly different.

The goal is not to build a full game — it is to understand **why** and **how** OOP patterns are used in real code.

---

## OOP Concepts Covered

| Concept | Description | Where It Appears |
|---|---|---|
| **Class & Object** | Blueprint and instance | All classes |
| **Constructor (`__init__`)** | Sets up an object's initial state | All classes |
| **Inheritance** | Child class inherits from parent | `Zombie(Enemy)`, `Ogre(Enemy)` |
| **Encapsulation** | Hides data with `__` prefix | `__type_of_enemy` in `Enemy` |
| **Polymorphism** | Same method name, different behavior | `talk()`, `special_attack()` |
| **Method Overriding** | Child replaces parent's method | `talk()` in `Zombie` and `Ogre` |
| **Composition** | One class holds another | `Hero` holds a `Weapon` |
| **`super()`** | Calls the parent class constructor | `Zombie.__init__`, `Ogre.__init__` |

---

## Project Structure

```
python-oop-battle/
│
├── main.py        # Entry point — creates objects and runs the battle
├── Enemy.py       # Base Enemy class (parent)
├── Zombie.py      # Zombie enemy (inherits Enemy)
├── Ogre.py        # Ogre enemy (inherits Enemy)
├── Hero.py        # Hero class (player character)
├── Weapon.py      # Weapon class (used by Hero)
└── README.md
```

---

## Classes Overview

### `Enemy` — Base Class

The parent class for all enemies. Holds shared attributes and methods.

```python
class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy  # private — hidden from outside
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):         # can be overridden by child classes
    def attack(self):       # prints attack message
    def special_attack(self):  # default: no special attack
    def get_type_of_enemy(self):  # getter for the private attribute
```

### `Zombie` — Inherits from `Enemy`

- **Special attack (50% chance):** Regenerates 2 HP each turn.
- Overrides `talk()` with its own message.

### `Ogre` — Inherits from `Enemy`

- **Special attack (20% chance):** Increases its own attack damage by 4.
- Overrides `talk()` with its own message.

### `Hero` — Player Character

- Holds a `Weapon` object (composition).
- `equip_weapon()` adds the weapon's bonus to `attack_damage`.
- Cannot equip the same weapon twice.

### `Weapon` — Item Class

```python
class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase
```

---

## How the Battle Works

There are two battle modes in `main.py`:

### `battle(e1, e2)` — Enemy vs Enemy

Both enemies take turns using their special ability, then attack each other. The second argument (`e2`) always attacks first each round.

```
Round start:
  → e1 uses special attack (if triggered)
  → e2 uses special attack (if triggered)
  → e2 attacks e1
  → e1 attacks e2
Repeat until one HP reaches 0.
```

### `hero_battle(hero, enemy)` — Hero vs Enemy

The enemy uses its special attack each turn and always strikes first. The hero attacks back. The fight continues until one side runs out of HP.

---

## Getting Started

**Requirements:** Python 3.x (no external libraries needed)

**Run the project:**

```bash
# Clone or download the repository, then run:
python main.py
```

**Change the battle scenario** by editing the bottom of `main.py`:

```python
# Hero vs Zombie (default)
zombie = Zombie(10, 1)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)

# Enemy vs Enemy (uncomment to try)
# zombie = Zombie(10, 1)
# ogre = Ogre(20, 3)
# battle(zombie, ogre)
```

---

## Example Output

```
-------------
Zombie regenerated 2 HP!
Hero: 10 HP left
Zombie: 12 HP left
Zombie attacks for 1 damage
Hero attacks for 6 damage
-------------
Hero: 9 HP left
Zombie: 6 HP left
Hero attacks for 6 damage
-------------
Hero wins!
```

---

## What You Will Learn

After studying this project, you will understand:

- How to design multiple classes that share common behavior using **inheritance**
- How to protect data using **encapsulation** (`__` prefix and getter methods)
- How the same method (`talk()`, `special_attack()`) can behave differently depending on the object — this is **polymorphism**
- How to connect classes together using **composition** (`Hero` has a `Weapon`)
- How `super()` passes arguments up to the parent constructor
- How to use `random.random()` to create probability-based outcomes

---

## Author

**Duygu Jones**
- GitHub: [@Duygu-Jones](https://github.com/Duygu-Jones)
