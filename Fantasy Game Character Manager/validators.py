# validators.py

"""
Validation utilities for character management system.

This module contains reusable validation functions used across
the character management application to ensure data integrity.
"""

import re


def validate_name(name):
    """
    Validate character name ensuring it contains only letters.
    :param name: str, the name to validate
    :return: str, the capitalized valid name
    """
    if not name or not isinstance(name, str):
        raise ValueError(
            "Character name cannot be empty and must be a string.")
    if not re.match("^[a-zA-Z]+$", name):
        raise ValueError("Character name can only contain letters.")
    return name.capitalize()


def validate_race(race):
    """
    Validate character race ensuring it's one of the allowed races.
    :param race: str, the race to validate (Elf, Dwarf, or Human)
    :return: str, the capitalized valid race
    """
    valid_races = ['elf', 'dwarf', 'human']
    if not race or not isinstance(race, str):
        raise ValueError(
            "Character race cannot be empty and must be a string.")
    if not re.match("^[a-zA-Z]+$", race):
        raise ValueError("Character race can only contain letters.")
    if race.lower() not in valid_races:
        raise ValueError("Race must be Elf, Dwarf, or Human.")
    return race.capitalize()


def validate_role(role):
    """
    Validate character role ensuring it's one of the allowed roles.
    :param role: str, the role to validate (Warrior or Mage)
    :return: str, the capitalized valid role
    """
    valid_roles = ['warrior', 'mage']
    if not role or not isinstance(role, str):
        raise ValueError(
            "Character role cannot be empty and must be a string.")
    if not re.match("^[a-zA-Z]+$", role):
        raise ValueError("Character role can only contain letters.")
    if role.lower() not in valid_roles:
        raise ValueError("Role must be Warrior or Mage.")
    return role.capitalize()


def validate_skill_level(skill_level):
    """
    Validate character skill level ensuring it's between 1 and 5.
    :param skill_level: str or int, the skill level to validate
    :return: str, the valid skill level as string
    """
    if isinstance(skill_level, str):
        if skill_level not in ['1', '2', '3', '4', '5']:
            raise ValueError("Skill level must be between 1 and 5.")
        return skill_level
    elif isinstance(skill_level, int):
        if skill_level < 1 or skill_level > 5:
            raise ValueError("Skill level must be between 1 and 5.")
        return str(skill_level)
    else:
        raise ValueError("Skill level must be a number between 1 and 5.")


def validate_wealth(wealth):
    """
    Validate character wealth ensuring it's a positive number.
    :param wealth: str or int, the wealth to validate (gold coins)
    :return: int, the valid wealth value
    """
    if isinstance(wealth, str):
        if not wealth.isdigit():
            raise ValueError("Wealth must be a valid positive number.")
        wealth = int(wealth)
    if not isinstance(wealth, int) or wealth < 0:
        raise ValueError("Wealth cannot be negative and must be a number.")
    return wealth


def validate_weapon(weapon):
    """
    Validate warrior weapon ensuring it's one of the allowed weapons.
    :param weapon: str, the weapon to validate (Sword or Axe)
    :return: str, the capitalized valid weapon
    """
    valid_weapons = ['sword', 'axe']
    if not weapon or not isinstance(weapon, str):
        raise ValueError("Weapon cannot be empty and must be a string.")
    if not re.match("^[a-zA-Z]+$", weapon):
        raise ValueError("Weapon can only contain letters.")
    if weapon.lower() not in valid_weapons:
        raise ValueError("Weapon must be Sword or Axe.")
    return weapon.capitalize()


def validate_armour(armour):
    """
    Validate warrior armour ensuring it's one of the allowed armour types.
    :param armour: str, the armour to validate (Chainmail or Plate)
    :return: str, the capitalized valid armour
    """
    valid_armour = ['chainmail', 'plate']
    if not armour or not isinstance(armour, str):
        raise ValueError("Armour cannot be empty and must be a string.")
    if not re.match("^[a-zA-Z]+$", armour):
        raise ValueError("Armour can only contain letters.")
    if armour.lower() not in valid_armour:
        raise ValueError("Armour must be Chainmail or Plate.")
    return armour.capitalize()


def validate_spell(spell):
    """
    Validate mage spell ensuring it's one of the allowed spells.
    :param spell: str, the spell to validate (Fireball or Lightning)
    :return: str, the capitalized valid spell
    """
    valid_spells = ['fireball', 'lightning']
    if not spell or not isinstance(spell, str):
        raise ValueError("Spell cannot be empty and must be a string.")
    if not re.match("^[a-zA-Z]+$", spell):
        raise ValueError("Spell can only contain letters.")
    if spell.lower() not in valid_spells:
        raise ValueError("Spell must be Fireball or Lightning.")
    return spell.capitalize()


def validate_mana_points(mana_points):
    """
    Validate mage mana points ensuring they're between 0 and 100.
    :param mana_points: str or int, the mana points to validate
    :return: int, the valid mana points value
    """
    if isinstance(mana_points, str):
        if not mana_points.isdigit():
            raise ValueError("Mana points must be a valid number.")
        mana_points = int(mana_points)
    if not isinstance(mana_points, int) or \
       mana_points < 0 or mana_points > 100:
        raise ValueError("Mana points must be between 0 and 100.")
    return mana_points
