# character.py
"""
Base Character class for the character management system.

This module defines the Character class which serves as the base class
for all character types in the game.
"""

from validators import (
    validate_name, validate_race, validate_role,
    validate_skill_level, validate_wealth
)


class Character:
    """
    Base character class with common attributes and methods.
    Represents a fantasy game character with basic properties like
    name, race, role, skill level, and wealth.
    All character attributes are validated upon creation and modification.
    """

    def __init__(self, name, race, role, skill_level, wealth):
        """
        Initialize a Character object with validated attributes.
        :param name: str, the character's name (letters only)
        :param race: str, the character's race (Elf, Dwarf, or Human)
        :param role: str, the character's role/class
        :param skill_level: str, the character's skill level (1-5)
        :param wealth: str,
        the character's wealth in gold coins (positive number)
        """
        self._name = None
        self._race = None
        self._role = None
        self._skill_level = None
        self._wealth = None

        # Use setters for validation
        self.set_name(name)
        self.set_race(race)
        self.set_role(role)
        self.set_skill_level(skill_level)
        self.set_wealth(wealth)

    # Getter methods
    def get_name(self):
        """
        Get the character's name.
        :return: str, the character's name
        """
        return self._name

    def get_race(self):
        """
        Get the character's race.
        :return: str, the character's race (Elf, Dwarf, or Human)
        """
        return self._race

    def get_role(self):
        """
        Get the character's role.
        :return: str, the character's role/class
        """
        return self._role

    def get_skill_level(self):
        """
        Get the character's skill level.
        :return: str, the character's skill level (1-5)
        """
        return self._skill_level

    def get_wealth(self):
        """
        Get the character's wealth.
        :return: int, the character's wealth in gold coins
        """
        return self._wealth

    # Setter methods with validation
    def set_name(self, name):
        """
        Set the character's name with validation.
        :param name: str, the character's name (letters only)
        :return: None
        """
        self._name = validate_name(name)

    def set_race(self, race):
        """
        Set the character's race with validation.
        :param race: str, the character's race (Elf, Dwarf, or Human)
        :return: None
        """
        self._race = validate_race(race)

    def set_role(self, role):
        """
        Set the character's role with validation.
        :param role: str, the character's role/class
        :return: None
        """
        self._role = validate_role(role)

    def set_skill_level(self, skill_level):
        """
        Set the character's skill level with validation.
        :param skill_level: str, the character's skill level (1-5)
        :return: None
        """
        self._skill_level = validate_skill_level(skill_level)

    def set_wealth(self, wealth):
        """
        Set the character's wealth with validation.
        :param wealth: str,
        the character's wealth in gold coins (positive number)
        :return: None
        """
        self._wealth = validate_wealth(wealth)

    def __str__(self):
        """
        String representation of the character.
        :return: str, formatted string containing all character details
        """
        return (f"Character Name : {self._name}\n"
                f"Race           : {self._race}\n"
                f"Role           : {self._role}\n"
                f"Skill Level    : {self._skill_level}\n"
                f"Wealth         : {self._wealth} Gold coins")
