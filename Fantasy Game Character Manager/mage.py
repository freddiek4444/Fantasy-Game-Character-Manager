# mage.py

"""
Mage class for the character management system.

This module defines the Mage class which inherits from Character
and adds mage-specific attributes like spell and mana points.
"""

from character import Character
from validators import validate_spell, validate_mana_points


class Mage(Character):
    """
    Mage character class with spell and mana points attributes.
    Inherits from Character and adds mage-specific properties like
    spell and mana points.
    """

    def __init__(self, name, race, skill_level, wealth, spell, mana_points):
        """
        Initialize a Mage object with inherited and specific attributes.
        :param name: str, the mage's name (letters only)
        :param race: str, the mage's race (Elf, Dwarf, or Human)
        :param skill_level: str, the mage's skill level (1-5)
        :param wealth: str, the mage's wealth in gold coins
        :param spell: str, the mage's spell (Fireball or Lightning)
        :param mana_points: int, the mage's mana points (0-100)
        """
        # Call parent constructor with role set to 'Mage'
        super().__init__(name, race, 'Mage', skill_level, wealth)
        self._spell = None
        self._mana_points = None

        # Use setters for validation
        self.set_spell(spell)
        self.set_mana_points(mana_points)

    # Getter methods for mage-specific attributes
    def get_spell(self):
        """
        Get the mage's spell.
        :return: str, the mage's spell (Fireball or Lightning)
        """
        return self._spell

    def get_mana_points(self):
        """
        Get the mage's mana points.
        :return: int, the mage's mana points (0-100)
        """
        return self._mana_points

    # Setter methods for mage-specific attributes
    def set_spell(self, spell):
        """
        Set the mage's spell with validation.
        :param spell: str, the mage's spell (Fireball or Lightning)
        :return: None
        """
        self._spell = validate_spell(spell)

    def set_mana_points(self, mana_points):
        """
        Set the mage's mana points with validation.
        :param mana_points: int, the mage's mana points (0-100)
        :return: None
        """
        self._mana_points = validate_mana_points(mana_points)

    def __str__(self):
        """
        String representation of the mage character.
        :return: str, formatted string containing all mage details
        including inherited attributes
        """
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Spell          : {self._spell}\n"
                f"Mana Points    : {self._mana_points} MP")
