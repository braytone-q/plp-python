# -------------------------------
# Interactive Superhero + Polymorphism Program
# -------------------------------

# Superhero Classes
class Superhero:
    def __init__(self, name, power, health=100):
        self.__name = name
        self.__power = power
        self.__health = health

    # Getters
    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_health(self):
        return self.__health

    # Setters
    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Health must be between 0 and 100.")

    # Methods
    def attack(self, enemy):
        print(f"{self.__name} attacks {enemy} using {self.__power}!")

    def heal(self, amount):
        self.set_health(min(100, self.__health + amount))
        print(f"{self.__name} healed to {self.__health} health.")

    def __str__(self):
        return f"{self.__name} (Power: {self.__power}, Health: {self.__health})"


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health=100, flying_speed=50):
        super().__init__(name, power, health)
        self.__flying_speed = flying_speed

    def fly(self):
        print(f"{self.get_name()} is flying at {self.__flying_speed} km/h!")


# Polymorphism Classes
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")


class Car(Vehicle):
    def move(self):
        print("Driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky.")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water.")


# -------------------------------
# Main Interactive Program
# -------------------------------

def create_superhero():
    print("\nCreate a Superhero!")
    name = input("Enter superhero name: ")
    power = input("Enter superhero power: ")
    health = int(input("Enter health (0-100): "))
    type_choice = input("Is it a flying superhero? (yes/no): ").strip().lower()
    
    if type_choice == "yes":
        flying_speed = int(input("Enter flying speed (km/h): "))
        hero = FlyingSuperhero(name, power, health, flying_speed)
    else:
        hero = Superhero(name, power, health)
    return hero


def superhero_actions(hero):
    print(f"\nYour superhero: {hero}")
    while True:
        action = input("Choose action: attack / heal / fly / quit: ").strip().lower()
        if action == "attack":
            enemy = input("Enter enemy name: ")
            hero.attack(enemy)
        elif action == "heal":
            amount = int(input("Enter heal amount: "))
            hero.heal(amount)
        elif action == "fly" and isinstance(hero, FlyingSuperhero):
            hero.fly()
        elif action == "quit":
            break
        else:
            print("Invalid action or action not available.")


def vehicle_demo():
    print("\nVehicle Polymorphism Demo:")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()


# -------------------------------
# Run Program
# -------------------------------

if __name__ == "__main__":
    hero = create_superhero()
    superhero_actions(hero)
    vehicle_demo()
