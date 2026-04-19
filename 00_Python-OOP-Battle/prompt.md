```python
class Enemy:

    '''
        - Special attacks
        - Have them battle!
    '''

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")  

    def special_attack(self):
        print('Enemy has no special attack.')

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def last_words(self):
        print('ARRRGHH')

from Weapon import *

class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None


    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage")

from Zombie import *
from Ogre import *
from Enemy import *
from Hero import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("-------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print("-------------")

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")


def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print("-------------")
        enemy.special_attack()
        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print("-------------")

    if hero.health_points > 0:
        print(f"Hero wins!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!")


# zombie = Zombie(10, 1)
# ogre = Ogre(20, 3)
# battle(zombie, ogre)
        
zombie = Zombie(10, 1)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)


from Enemy import *
import random

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Ogre", 
            health_points=health_points, 
            attack_damage=attack_damage
            )

    def talk(self):
        print("Ogre is slamming hands all around!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre gets angry and its attack has increased by 4!")
    

class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase

from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie", 
                        health_points=health_points, 
                        attack_damage=attack_damage)

    def talk(self):
        print("*Grumbling...*")

    def spread_disease(self):
        print("The zombie is trying to spread infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50  # 50% chance for the special attack to work
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2 HP!")
    

e1 ve e1 veya hero hangisi battle ilk once basliyor e1 ve e2 hangi enemy denk geliyor? rastgelelik mi var yoksa oyunu calsitirdigimiz yrde ilk zombi objesi olusturuldugu icin mi e1 zombi mi oluyor mesela?

bu pratikdeki tum code parcalarini aciklayarak python oop mantigini acikla. polimorfizm, overrring, encapsul, inerit vs tum oop konularini bana detaylica acikla. hic birlmeyen birine aciklar gibi acikla. once boyle bir oyun olusturabilmek icin algoritmik olarak dusun tek tek parcalari tanimla, hangi adimlar var nasil calismali, python ile nasil implemente edilir. adim adim hic bilmeyen birine onretecek sekilde python konularini sadece bu ornek uzerinden acikla. 
```

# ############################################################################################

# Python OOP Kavramlarını Sıfırdan Öğrenelim - Oyun Örneği Üzerinden

Harika bir örnek seçmişsiniz! Bu kod parçasını adım adım, hiç bilmeyen birine anlatır gibi açıklayacağım.

## 🎯 Önce Genel Mantığı Anlayalım

### Oyun Nasıl Çalışmalı? (Algoritmik Düşünce)

Bir dövüş oyunu yapmak istiyorsunuz. Adımlar:

1. **Karakterler olmalı**: Kahraman (Hero), Düşmanlar (Zombie, Ogre)
2. **Her karakterin özellikleri olmalı**: Can (HP), Hasar (attack damage)
3. **Karakterler hareket etmeli**: Saldırma, konuşma, özel yetenekler
4. **Dövüş sistemi olmalı**: İki karakter karşı karşıya gelip sırayla vursun
5. **Kazanan belli olmalı**: Canı biten kaybeder

Şimdi bunu Python ile nasıl yaparız?

---

## 📦 1. CLASS (Sınıf) Nedir?

**Basit Açıklama**: Class, bir şeyin "tarifi"dir.

**Gerçek hayat örneği**:
- Kurabiye kalıbı = Class
- Kalıptan çıkan kurabiyeler = Objeler (nesneler)

```python
class Enemy:  # Bu bir tarif/kalıp
    pass
```

Bir Enemy (düşman) yaratmak için bu tarifi kullanırız.

---

## 🏗️ 2. CONSTRUCTOR (`__init__`) - Yapıcı Metod

**Ne işe yarar?**: Bir obje yaratıldığında ilk çalışan fonksiyon. Objenin başlangıç özelliklerini ayarlar.

```python
def __init__(self, type_of_enemy, health_points, attack_damage):
    self.__type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attack_damage = attack_damage
```

**Satır satır açıklama**:

- `def __init__`: "Bu obje yaratılırken şunları yap" demek
- `self`: "Bu objenin kendisi" demek (her obje kendi değişkenlerine `self` ile erişir)
- `type_of_enemy, health_points, attack_damage`: Dışarıdan alınan parametreler
- `self.health_points = health_points`: Bu objenin can değerini ayarla

**Örnek kullanım**:
```python
zombie = Zombie(10, 1)
# health_points = 10, attack_damage = 1 olarak bir zombie yaratıldı
```

---

## 🔒 3. ENCAPSULATION (Kapsülleme)

**Ne demek?**: Bazı bilgileri gizlemek, dışarıdan doğrudan erişimi engellemek.

```python
self.__type_of_enemy = type_of_enemy  # İki alt çizgi (__) = GİZLİ
self.health_points = health_points    # Tek alt çizgi yok = AÇIK
```

**Neden önemli?**:
- `__type_of_enemy`: Dışarıdan değiştirilemez (korumalı)
- `health_points`: Dışarıdan değiştirilebilir

**Gizli değere nasıl erişiriz?**:
```python
def get_type_of_enemy(self):
    return self.__type_of_enemy
```

Bu fonksiyona **getter** denir. Gizli değeri okumamızı sağlar ama değiştirmemizi engelleyen bir kontrol noktasıdır.

**Pratik örnek**:
```python
zombie = Zombie(10, 1)
print(zombie.health_points)  # ✅ Çalışır: 10
# print(zombie.__type_of_enemy)  # ❌ HATA! Gizli değişken
print(zombie.get_type_of_enemy())  # ✅ Çalışır: "Zombie"
```

---

## 👨‍👦 4. INHERITANCE (Kalıtım)

**Ne demek?**: Bir class, başka bir class'ın özelliklerini miras alabilir.

**Gerçek hayat**: 
- Baba'nın özellikleri → Çocuğa geçer
- Enemy class'ı → Zombie ve Ogre'ye geçer

```python
class Zombie(Enemy):  # Zombie, Enemy'nin çocuğu
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage
        )
```

**`super()` ne demek?**:
- "Anne/baba class'ın fonksiyonunu çağır" demek
- Burada Enemy'nin `__init__` fonksiyonu çağrılıyor

**Ne kazandık?**:
- Zombie, Enemy'nin tüm metodlarını kullanabilir: `talk()`, `walk_forward()`, `attack()`
- Kod tekrarı yapmadık!

---

## 🎭 5. POLYMORPHISM (Çok Biçimlilik)

**Ne demek?**: Aynı isimli fonksiyon, farklı class'larda farklı davranabilir.

### a) Method Overriding (Metod Ezme)

```python
# Enemy class'ında:
def talk(self):
    print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

# Zombie class'ında:
def talk(self):
    print("*Grumbling...*")  # ÜZERİNE YAZILDI!

# Ogre class'ında:
def talk(self):
    print("Ogre is slamming hands all around!")  # ÜZERİNE YAZILDI!
```

**Ne oldu?**:
- Her düşman `talk()` metoduna sahip
- Ama her biri farklı şey söylüyor!
- Bu **override** (üzerine yazma) örneği

**Pratik kullanım**:
```python
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

zombie.talk()  # Çıktı: *Grumbling...*
ogre.talk()    # Çıktı: Ogre is slamming hands all around!
```

### b) Polymorphism'in Gücü

```python
def battle(e1: Enemy, e2: Enemy):
    e1.talk()  # Hangi düşman olursa olsun, kendi konuşmasını yapar
    e2.talk()
```

**Güzellik**: 
- `battle()` fonksiyonu, hangi düşman gelirse gelsin çalışır
- Zombie vs Ogre, Zombie vs Zombie, Ogre vs Ogre... hepsi!

---

## 🎲 6. SPECIAL ATTACK - Özel Yetenekler

Her düşmanın kendine özgü özel hareketi var:

### Zombie'nin Özel Yeteneği:
```python
def special_attack(self):
    did_special_attack_work = random.random() < 0.50  # %50 şans
    if did_special_attack_work:
        self.health_points += 2
        print("Zombie regenerated 2 HP!")
```

**Nasıl çalışır?**:
- `random.random()`: 0 ile 1 arası rastgele sayı üretir
- `< 0.50`: %50 ihtimalle True döner
- Başarılıysa: Zombie 2 can kazanır!

### Ogre'nin Özel Yeteneği:
```python
def special_attack(self):
    did_special_attack_work = random.random() < 0.20  # %20 şans
    if did_special_attack_work:
        self.attack_damage += 4
        print("Ogre gets angry and its attack has increased by 4!")
```

**Fark**: Ogre can kazanmaz, saldırı gücü artar!

---

## ⚔️ 7. WEAPON CLASS - Silah Sistemi

```python
class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase
```

**Basit bir class**: Sadece silah tipi ve saldırı artışını tutar.

### Hero'ya Silah Ekleme:

```python
class Hero:
    def __init__(self, health_points, attack_damage):
        self.weapon: Weapon = None  # Başlangıçta silah yok
        self.is_weapon_equipped = False  # Silah takılmamış
```

**`self.weapon: Weapon = None` ne demek?**:
- `self.weapon`: Bu değişken bir silah tutacak
- `: Weapon`: Tip belirteci (opsiyonel, kod okunurluğu için)
- `= None`: Başlangıçta silah yok

### Silah Takma:
```python
def equip_weapon(self):
    if self.weapon is not None and not self.is_weapon_equipped:
        self.attack_damage += self.weapon.attack_increase
        self.is_weapon_equipped = True
```

**Mantık**:
1. Silah var mı? (`self.weapon is not None`)
2. Daha önce takılmamış mı? (`not self.is_weapon_equipped`)
3. İkisi de doğruysa: Saldırı gücüne silahın bonusunu ekle

**Kullanımı**:
```python
hero = Hero(10, 1)  # Can: 10, Saldırı: 1
weapon = Weapon('Sword', 5)  # Kılıç, +5 saldırı
hero.weapon = weapon  # Silahı kahramana ver
hero.equip_weapon()  # Silahı tak
# Artık hero.attack_damage = 6 (1 + 5)
```

---

## 🥊 8. BATTLE SYSTEM - Dövüş Sistemi

### Enemy vs Enemy:
```python
def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    
    while e1.health_points > 0 and e2.health_points > 0:
        print("-------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        
        e2.attack()
        e1.health_points -= e2.attack_damage
        
        e1.attack()
        e2.health_points -= e1.attack_damage
    
    # Kazanan kim?
    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")
```

**Adım adım**:
1. **İlk konuşma**: Her iki düşman konuşur
2. **Döngü**: İkisinin de canı varken devam et
3. **Özel yetenekler**: Her tur özel yetenekleri dene
4. **Can durumu**: Mevcut canları göster
5. **Karşılıklı saldırı**: 
   - e2 saldırır → e1'in canı azalır
   - e1 saldırır → e2'nin canı azalır
6. **Kazanan**: Canı kalan kazanır

### Hero vs Enemy:
```python
def hero_battle(hero: Hero, enemy: Enemy):
    # Aynı mantık, sadece hero ve enemy için
```

Aynı yapı, sadece obje isimleri farklı.

---

## 🎮 9. OYUNU ÇALIŞTIRMA

```python
zombie = Zombie(10, 1)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)
```

**Senaryo**:
1. Zombie yaratıldı: 10 can, 1 saldırı
2. Hero yaratıldı: 10 can, 1 saldırı
3. Kılıç yaratıldı: +5 saldırı bonusu
4. Kılıç hero'ya verildi ve takıldı → Hero'nun saldırısı şimdi 6
5. Dövüş başladı!

**Örnek çıktı**:
```
-------------
Zombie regenerated 2 HP!
Hero: 10 HP left
Zombie: 12 HP left
Zombie attacks for 1 damage
Hero attacks for 6 damage
-------------
...
Hero wins!
```

---

## 📊 OOP KONSEPTLERİNİN ÖZET TABLOSU

| Konsept | Ne İşe Yarar? | Örnekteki Yeri |
|---------|---------------|----------------|
| **Class** | Objelerin taslağı | `Enemy`, `Hero`, `Weapon` |
| **Object** | Class'tan yaratılan örnek | `zombie = Zombie(10, 1)` |
| **Inheritance** | Özellikleri miras alma | `Zombie(Enemy)`, `Ogre(Enemy)` |
| **Encapsulation** | Veri gizleme | `__type_of_enemy` |
| **Polymorphism** | Aynı metod, farklı davranış | `talk()` her class'ta farklı |
| **Constructor** | Obje oluştururken çalışır | `__init__()` |
| **Method** | Class içindeki fonksiyon | `attack()`, `special_attack()` |
| **Attribute** | Class içindeki değişken | `health_points`, `attack_damage` |

---

## 💡 NEDEN OOP KULLANIYORUZ?

### ❌ OOP Olmadan:
```python
zombie_health = 10
zombie_attack = 1
ogre_health = 20
ogre_attack = 3

def zombie_attack_func():
    print("Zombie attacks!")

def ogre_attack_func():
    print("Ogre attacks!")

# 10 düşman olsaydı 30+ değişken ve fonksiyon olurdu!
```

### ✅ OOP İle:
```python
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

zombie.attack()
ogre.attack()

# Her şey organize, anlaşılır, genişletilebilir!
```

---

## 🚀 İLERİ SEVİYE EKLEMELER

Oyununuzu daha da geliştirebilirsiniz:

### 1. Daha Fazla Düşman:
```python
class Dragon(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__("Dragon", health_points, attack_damage)
    
    def special_attack(self):
        print("Dragon breathes fire! All enemies lose 5 HP!")
        # Fire damage logic
```

### 2. Hero Seviyelendirme:
```python
class Hero:
    def __init__(self, health_points, attack_damage):
        self.level = 1
        self.experience = 0
    
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.health_points += 5
        self.attack_damage += 2
        print(f"Level up! Now level {self.level}!")
```

### 3. Inventory Sistemi:
```python
class Hero:
    def __init__(self):
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def use_potion(self):
        if "Health Potion" in self.inventory:
            self.health_points += 20
            self.inventory.remove("Health Potion")
```

---

## 🎯 ÖZET: OOP'nin Altın Kuralları

1. **Class = Tarif**: Objelerin nasıl olacağını tanımlar
2. **Object = Ürün**: Class'tan yaratılan gerçek örnekler
3. **Inheritance = Miras**: Kod tekrarını engeller
4. **Encapsulation = Gizlilik**: Verileri korur
5. **Polymorphism = Esneklik**: Aynı arayüz, farklı davranışlar

Bu oyun örneği, Python OOP'nin tüm temellerini içeriyor. Pratik yaparak bu konseptleri daha iyi anlayacaksınız! 🎮✨

---

Harika bir soru! Bu çok önemli bir detay. Şimdi açıklayayım:

## 🎯 Cevap: RASTGELE DEĞİL, SIRAYA BAĞLI!

### 📌 Fonksiyona Nasıl Gönderdiğiniz Önemli

```python
def battle(e1: Enemy, e2: Enemy):
    # ...

# Örnek 1:
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
battle(zombie, ogre)
```

**Bu durumda:**
- `e1` = `zombie` (ilk parametre)
- `e2` = `ogre` (ikinci parametre)

**Yani:**
- Zombie önce özel yetenek kullanır
- Ogre ikinci özel yetenek kullanır
- **AMA** saldırı sırasında `e2` (ogre) önce vurur!

---

## ⚔️ Saldırı Sırası Nasıl?

Koda tekrar bakalım:

```python
while e1.health_points > 0 and e2.health_points > 0:
    print("-------------")
    e1.special_attack()      # 1. Zombie özel yetenek dener
    e2.special_attack()      # 2. Ogre özel yetenek dener
    
    print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
    print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
    
    e2.attack()              # 3. OGRE İLK VURUR! ⚡
    e1.health_points -= e2.attack_damage
    
    e1.attack()              # 4. Zombie sonra vurur
    e2.health_points -= e1.attack_damage
```

### 🔥 ÖNEMLİ NOKTA:
**`e2` her zaman ilk saldırır!**

---

## 🧪 Pratik Örnekler

### Örnek 1: Zombie vs Ogre
```python
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
battle(zombie, ogre)
```

**Sıra:**
1. Zombie özel yetenek (belki +2 HP kazanır)
2. Ogre özel yetenek (belki +4 saldırı kazanır)
3. **Ogre saldırır** → Zombie'nin canı azalır
4. Zombie saldırır → Ogre'nin canı azalır

**İlk vuran: OGRE (e2)**

---

### Örnek 2: Ogre vs Zombie (Sıra Değişti!)
```python
ogre = Ogre(20, 3)
zombie = Zombie(10, 1)
battle(ogre, zombie)  # SıRAYI DEĞİŞTİRDİK!
```

**Sıra:**
1. Ogre özel yetenek
2. Zombie özel yetenek
3. **Zombie saldırır** → Ogre'nin canı azalır (çünkü şimdi zombie = e2)
4. Ogre saldırır → Zombie'nin canı azalır

**İlk vuran: ZOMBİE (e2)**

---

## 🎲 Peki Rastgele Yapmak İstersek?

Mevcut kodda rastgelelik YOK! Ama ekleyebiliriz:

### Yöntem 1: İlk Saldıranı Rastgele Seç

```python
import random

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    
    # Rastgele ilk saldıranı belirle
    first_attacker = random.choice([e1, e2])
    if first_attacker == e1:
        second_attacker = e2
    else:
        second_attacker = e1
    
    print(f"{first_attacker.get_type_of_enemy()} will attack first!")
    
    while e1.health_points > 0 and e2.health_points > 0:
        print("-------------")
        e1.special_attack()
        e2.special_attack()
        
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        
        # Rastgele belirlenen sıra ile saldır
        first_attacker.attack()
        if first_attacker == e1:
            e2.health_points -= e1.attack_damage
        else:
            e1.health_points -= e2.attack_damage
        
        second_attacker.attack()
        if second_attacker == e1:
            e2.health_points -= e1.attack_damage
        else:
            e1.health_points -= e2.attack_damage
```

### Yöntem 2: Her Turda Rastgele (Daha Dinamik!)

```python
import random

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    
    while e1.health_points > 0 and e2.health_points > 0:
        print("-------------")
        e1.special_attack()
        e2.special_attack()
        
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        
        # Her turda rastgele sıralama!
        attackers = [e1, e2]
        random.shuffle(attackers)  # Listeyi karıştır
        
        first = attackers[0]
        second = attackers[1]
        
        print(f"{first.get_type_of_enemy()} attacks first this turn!")
        
        first.attack()
        if first == e1:
            e2.health_points -= e1.attack_damage
        else:
            e1.health_points -= e2.attack_damage
        
        # İkinci saldıran sadece canlıysa vurur
        if second.health_points > 0:
            second.attack()
            if second == e1:
                e2.health_points -= e1.attack_damage
            else:
                e1.health_points -= e2.attack_damage
```

---

## 🎮 Hero Battle'da Durum Aynı mı?

```python
def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print("-------------")
        enemy.special_attack()  # Enemy özel yetenek kullanır
        
        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        
        enemy.attack()          # 1. ENEMY İLK VURUR! ⚡
        hero.health_points -= enemy.attack_damage
        
        hero.attack()           # 2. Hero sonra vurur
        enemy.health_points -= hero.attack_damage
```

**Evet, aynı mantık:**
- Enemy (düşman) her zaman ilk saldırır
- Hero sonra saldırır

---

## 💡 Oyun Tasarımı Açısından

### Neden e2/enemy İlk Saldırıyor?

```python
# Kodun yazarı böyle tasarlamış
# Belki düşmanların avantajlı olmasını istemiş
# Ya da bir nedeni yok, rastgele seçilmiş
```

### Daha Adil Bir Sistem:

```python
# Hız (speed) özelliği ekleyelim
class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage, speed):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.speed = speed  # YENİ!

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    
    while e1.health_points > 0 and e2.health_points > 0:
        # Hızlı olan ilk vurur!
        if e1.speed >= e2.speed:
            first, second = e1, e2
        else:
            first, second = e2, e1
        
        print(f"{first.get_type_of_enemy()} is faster and attacks first!")
        
        # Saldırılar...
```

---

## 📊 Özet Tablo

| Senaryo | İlk Vuran | Mantık |
|---------|-----------|--------|
| `battle(zombie, ogre)` | **Ogre** | e2 her zaman ilk vurur |
| `battle(ogre, zombie)` | **Zombie** | e2 her zaman ilk vurur |
| `hero_battle(hero, enemy)` | **Enemy** | enemy her zaman ilk vurur |
| Rastgele sistem | **Değişken** | `random.choice()` ile seçilir |
| Hız sistemi | **En hızlı** | `speed` özelliğine göre |

---

## 🎯 Sonuç

**Sorunuzun cevabı:**
- ❌ Rastgele değil
- ❌ Hangisinin önce oluşturulduğuna bağlı değil
- ✅ Fonksiyona hangi sırayla gönderildiğine bağlı
- ✅ Kodda **e2 her zaman ilk saldırır** diye yazılmış

**Örnek:**
```python
battle(zombie, ogre)  # Ogre ilk vurur (e2 = ogre)
battle(ogre, zombie)  # Zombie ilk vurur (e2 = zombie)
```

Bu bir **tasarım kararı**. İsterseniz rastgele veya hız bazlı sisteme çevirebilirsiniz! 🎮