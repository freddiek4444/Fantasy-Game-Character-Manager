# file_manager.py

"""
File management utilities for character data persistence.

This module handles saving and loading character data to/from CSV files.
It provides functions to serialize character objects to CSV format and
deserialize CSV data back to character objects.
"""

import csv
from character import Character
from warrior import Warrior
from mage import Mage
from file_chooser import choose_open_file, choose_save_file


def save_characters_to_file(characters):
    """
    Save character list to CSV file using GUI file chooser.
    :param characters: list, list of Character objects to save to file
    :return: bool, True if save was successful, False if cancelled or failed
    """
    if not characters:
        print("No characters to save.")
        print()
        return False

    # Use GUI file chooser
    filename = choose_save_file("Save Characters to File")
    if not filename:
        print("Save cancelled.")
        print()
        return False

    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = [
                'name',
                'race',
                'role',
                'skill_level',
                'wealth',
                'weapon',
                'armour',
                'spell',
                'mana_points'
                ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Convert Character objects to dictionaries for CSV writing
            character_dicts = []
            for character in characters:
                character_dict = {
                    'name': character.get_name(),
                    'race': character.get_race(),
                    'role': character.get_role(),
                    'skill_level': character.get_skill_level(),
                    'wealth': character.get_wealth(),
                    'weapon': '',
                    'armour': '',
                    'spell': '',
                    'mana_points': ''
                }

                # Add specialized attributes based on character type
                if isinstance(character, Warrior):
                    character_dict['weapon'] = character.get_weapon()
                    character_dict['armour'] = character.get_armour()
                elif isinstance(character, Mage):
                    character_dict['spell'] = character.get_spell()
                    character_dict['mana_points'] = character.get_mana_points()

                character_dicts.append(character_dict)

            writer.writerows(character_dicts)
        print(f"Characters saved successfully to {filename}")
        print()
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        print()
        return False


def load_characters_from_file():
    """
    Load characters from CSV file using GUI file chooser.
    :return: list, list of loaded Character objects, empty list
    if cancelled or failed
    """
    # Use GUI file chooser
    filename = choose_open_file("Load Characters from File")
    if not filename:
        print("Load cancelled.")
        print()
        return []

    try:
        loaded_characters = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Create specialized character objects from CSV data
                    if row['role'].lower() == 'warrior' and \
                            row['weapon'] and row['armour']:
                        character = Warrior(
                            row['name'],
                            row['race'],
                            row['skill_level'],
                            int(row['wealth']),
                            row['weapon'],
                            row['armour']
                        )
                    elif row['role'].lower() == 'mage' and \
                            row['spell'] and row['mana_points']:
                        character = Mage(
                            row['name'],
                            row['race'],
                            row['skill_level'],
                            int(row['wealth']),
                            row['spell'],
                            int(row['mana_points'])
                        )
                    else:
                        # Fallback to base Character class for incomplete
                        character = Character(
                            row['name'],
                            row['race'],
                            row['role'],
                            row['skill_level'],
                            int(row['wealth'])
                        )
                    loaded_characters.append(character)
                except ValueError as e:
                    print(f"Error loading character from file: {e}")
                    continue

        print(f"Characters loaded successfully from {filename}")
        print(f"Loaded {len(loaded_characters)} characters.")
        print()
        return loaded_characters
    except FileNotFoundError:
        print(f"File {filename} not found.")
        print()
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        print()
        return []
