# warrior.py

"""
Warrior class for the character management system.

This module defines the Warrior class which inherits from Character
and adds warrior-specific attributes like weapon and armour.
"""

from character import Character
from validators import validate_weapon, validate_armour


class Warrior(Character):
    """
    Warrior character class with weapon and armour attributes.
    Inherits from Character and adds warrior-specific
    properties like weapon and armour.
    """

    def __init__(self, name, race, skill_level, wealth, weapon, armour):
        """
        Initialize a Warrior object with inherited and specific attributes.
        :param name: str, the warrior's name (letters only)
        :param race: str, the warrior's race (Elf, Dwarf, or Human)
        :param skill_level: str, the warrior's skill level (1-5)
        :param wealth: str, the warrior's wealth in gold coins
        :param weapon: str, the warrior's weapon (Sword or Axe)
        :param armour: str, the warrior's armour (Chainmail or Plate)
        """
        # Call parent constructor with role set to 'Warrior'
        super().__init__(name, race, 'Warrior', skill_level, wealth)
        self._weapon = None
        self._armour = None

        # Use setters for validation
        self.set_weapon(weapon)
        self.set_armour(armour)

    # Getter methods for warrior-specific attributes
    def get_weapon(self):
        """
        Get the warrior's weapon.
        :return: str, the warrior's weapon (Sword or Axe)
        """
        return self._weapon

    def get_armour(self):
        """
        Get the warrior's armour.
        :return: str, the warrior's armour (Chainmail or Plate)
        """
        return self._armour

    # Setter methods for warrior-specific attributes
    def set_weapon(self, weapon):
        """
        Set the warrior's weapon with validation.
        :param weapon: str, the warrior's weapon (Sword or Axe)
        :return: None
        """
        self._weapon = validate_weapon(weapon)

    def set_armour(self, armour):
        """
        Set the warrior's armour with validation.
        :param armour: str, the warrior's armour (Chainmail or Plate)
        :return: None
        """
        self._armour = validate_armour(armour)

    def __str__(self):
        """
        String representation of the warrior character.
        :return: str, formatted string containing all warrior details
        including inherited attributes
        """
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Weapon         : {self._weapon}\n"
                f"Armour         : {self._armour}")
