# main.py

"""
Fantasy Game Character Manager - Main Code
Author: Freddie Kingham
"""

import re
from character import Character
from warrior import Warrior
from mage import Mage
from character_gui import CharacterCreationGUI
from file_manager import save_characters_to_file, load_characters_from_file


# Global list to store all characters
characters = []


def display_menu():
    """
    Display the main menu options for the character management system.
    Shows all available commands including add character, search, and
    file operations.
    :return: None
    """
    print("=" * 50)
    print("CHARACTER MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add a Character")
    print("2. Add a Character (GUI)")
    print("3. List all Characters")
    print("4. Search for Characters by Name")
    print("5. Total Wealth of all the Characters")
    print("6. Save Characters to a File")
    print("7. Load Characters from a File")
    print("0. Exit Application")
    print("=" * 50)
    print("Please make a selection:", end=" ")


def get_character_name():
    """
    Get and validate character name from user input.
    Ensures name contains only letters and is not empty.
    :return: str, validated and capitalized character name
    """
    while True:
        name = input("Enter the character name: ").strip()
        if not name:
            print("Invalid input! Character name cannot be empty.")
        elif not re.match("^[a-zA-Z]+$", name):
            print("Invalid input! Character name can only contain letters.")
        else:
            return name.capitalize()


def get_character_race():
    """
    Get and validate character race from user input.
    Only accepts Elf, Dwarf, or Human as valid races.
    :return: str, validated and capitalized character race
    """
    valid_races = ['elf', 'dwarf', 'human']
    while True:
        race = input(
            "Enter the character race (Elf, Dwarf, or Human): ").strip()
        if not race:
            print("Invalid input! Character race cannot be empty.")
        elif not re.match("^[a-zA-Z]+$", race):
            print("Invalid input! Character race can only contain letters.")
        elif race.lower() not in valid_races:
            print("Invalid input! Race must be Elf, Dwarf, or Human.")
        else:
            return race.capitalize()


def get_character_role():
    """
    Get and validate character role from user input.
    Only accepts Warrior or Mage as valid roles.
    :return: str, validated and capitalized character role
    """
    valid_roles = ['warrior', 'mage']
    while True:
        role = input("Enter the character role (Warrior or Mage): ").strip()
        if not role:
            print("Invalid input! Character role cannot be empty.")
        elif not re.match("^[a-zA-Z]+$", role):
            print("Invalid input! Character role can only contain letters.")
        elif role.lower() not in valid_roles:
            print("Invalid input! Role must be Warrior or Mage.")
        else:
            return role.capitalize()


def get_character_skill_level():
    """
    Get and validate character skill level from user input.
    Only accepts values 1-5 representing different skill levels.
    :return: str, validated skill level (1-5)
    """
    while True:
        skill_level = input("Enter the character skill level (1-5): ").strip()
        if not skill_level:
            print("Invalid input! Skill level cannot be empty.")
        elif skill_level in ['1', '2', '3', '4', '5']:
            return skill_level
        else:
            print("Invalid input! Please enter a number between 1 and 5.")


def get_character_wealth():
    """
    Get and validate character wealth from user input.
    Ensures wealth is a positive number representing gold coins.
    :return: str, validated wealth amount as string
    """
    while True:
        wealth = input("Enter the character wealth (in Gold coins): ").strip()
        if not wealth:
            print("Invalid input! Wealth cannot be empty.")
        elif not wealth.isdigit():
            print("Invalid input! Please enter a valid positive number.")
        elif int(wealth) < 0:
            print("Invalid input! Wealth cannot be negative.")
        else:
            return wealth


def get_warrior_weapon():
    """
    Get and validate warrior weapon from user input.
    Only accepts Sword or Axe as valid weapons.
    :return: str, validated and capitalized weapon name
    """
    while True:
        weapon = input("Enter the warrior's weapon (Sword or Axe): ").strip()
        if not weapon:
            print("Invalid input! Weapon cannot be empty.")
        elif not re.match("^[a-zA-Z]+$", weapon):
            print("Invalid input! Weapon can only contain letters.")
        elif weapon.lower() not in ['sword', 'axe']:
            print("Invalid input! Weapon must be Sword or Axe.")
        else:
            return weapon.capitalize()


def get_warrior_armour():
    """
    Get and validate warrior armour from user input.
    Only accepts Chainmail or Plate as valid armour types.
    :return: str, validated and capitalized armour name
    """
    while True:
        armour = input(
            "Enter the warrior's armour (Chainmail or Plate): ").strip()
        if not armour:
            print("Invalid input! Armour cannot be empty.")
        elif not re.match("^[a-zA-Z]+$", armour):
            print("Invalid input! Armour can only contain letters.")
        elif armour.lower() not in ['chainmail', 'plate']:
            print("Invalid input! Armour must be Chainmail or Plate.")
        else:
            return armour.capitalize()


def get_mage_spell():
    """
    Get and validate mage spell from user input.
    Only accepts Fireball or Lightning as valid spells.
    :return: str, validated and capitalized spell name
    """
    while True:
        spell = input(
            "Enter the mage's spell (Fireball or Lightning): ").strip()
        if not spell:
            print("Invalid input! Spell cannot be empty.")
        elif not re.match("^[a-zA-Z]+$", spell):
            print("Invalid input! Spell can only contain letters.")
        elif spell.lower() not in ['fireball', 'lightning']:
            print("Invalid input! Spell must be Fireball or Lightning.")
        else:
            return spell.capitalize()


def get_mage_mana_points():
    """
    Get and validate mage mana points from user input.
    Ensures mana points are between 0 and 100.
    :return: int, validated mana points value
    """
    while True:
        mana = input("Enter the mage's mana points (0-100): ").strip()
        if not mana:
            print("Invalid input! Mana points cannot be empty.")
        elif not mana.isdigit():
            print("Invalid input! Please enter a valid number.")
        elif int(mana) < 0 or int(mana) > 100:
            print("Invalid input! Mana points must be between 0 and 100.")
        else:
            return int(mana)


def add_character():
    """
    Add a character using console input.
    Collects all character information through prompts
    and creates appropriate character object.
    Adds the created character to the global characters list.
    :return: None
    """
    print("\n--- Add New Character ---")

    # Get character details from the user
    name = get_character_name()
    race = get_character_race()
    role = get_character_role()
    skill_level = get_character_skill_level()
    wealth = get_character_wealth()

    try:
        # Create specialized character object based on role
        if role.lower() == 'warrior':
            weapon = get_warrior_weapon()
            armour = get_warrior_armour()
            character = Warrior(
                name, race, skill_level, wealth, weapon, armour)
        elif role.lower() == 'mage':
            spell = get_mage_spell()
            mana_points = get_mage_mana_points()
            character = Mage(
                name, race, skill_level, wealth, spell, mana_points)
        else:
            # Fallback to base Character class
            # (should not happen with current validation)
            character = Character(name, race, role, skill_level, wealth)

        characters.append(character)

        # Display the character information
        print("\n" + "="*50)
        print("CHARACTER CREATED SUCCESSFULLY!")
        print("="*50)
        print(character)
        print("="*50)
        print()
    except ValueError as e:
        print(f"Error creating character: {e}")
        print()


def add_character_gui():
    """
    Launch GUI for adding a character.
    Opens the character creation GUI and adds the created character
    to the system.
    :return: None
    """
    print("\nLaunching GUI for character creation...")
    gui = CharacterCreationGUI()
    character = gui.run()

    if character:
        characters.append(character)
        print(f"\nCharacter added successfully via GUI!")
        print("="*50)
        print("CHARACTER DETAILS:")
        print("="*50)
        print(character)
        print("="*50)
        print()
    else:
        print("Character creation cancelled.")
        print()


def list_all_characters():
    """
    List all characters in the system.
    Displays detailed information for each character with proper formatting.
    :return: None
    """
    if not characters:
        print("\nNo characters found.")
        print()
        return

    print(f"\n{'='*20} ALL CHARACTERS {'='*20}")
    print(f"Total Characters: {len(characters)}")
    print("="*60)

    for i, character in enumerate(characters, 1):
        print(f"\n[{i}] {character.get_name()}")
        print("-" * 40)
        # Use the __str__ method which includes specialized attributes
        character_str = str(character)
        # Indent each line for better formatting
        indented_str = '\n'.join(
            f"    {line}" for line in character_str.split('\n'))
        print(indented_str)

    print("="*60)
    print()


def search_characters_by_name():
    """
    Search for characters by name using partial matching.
    Allows case-insensitive searching for characters by name.
    :return: None
    """
    if not characters:
        print("\nNo characters found.")
        print()
        return

    search_name = input(
        "\nEnter the character name to search for: ").strip().lower()
    if not search_name:
        print("Invalid input! Search name cannot be empty.")
        print()
        return

    found_characters = [
        char for char in characters if search_name in char.get_name().lower()]

    if not found_characters:
        print(f"\nNo characters found with name containing '{search_name}'.")
        print()
        return

    print(f"\n{'='*15} SEARCH RESULTS ({'='*15}")
    print(
        f"Found {len(found_characters)} character(s) matching '{search_name}'")
    print("="*50)

    for i, character in enumerate(found_characters, 1):
        print(f"\n[{i}] {character.get_name()}")
        print("-" * 30)
        # Use the __str__ method which includes specialized attributes
        character_str = str(character)
        # Indent each line for better formatting
        indented_str = '\n'.join(
            f"    {line}" for line in character_str.split('\n'))
        print(indented_str)

    print("="*50)
    print()


def total_wealth():
    """
    Calculate and display total wealth statistics.
    Shows total wealth, average wealth, richest and poorest characters.
    :return: None
    """
    if not characters:
        print("\nNo characters found.")
        print()
        return

    total = sum(character.get_wealth() for character in characters)

    print(f"\n{'='*15} WEALTH STATISTICS ({'='*15}")
    print(f"Total Characters      : {len(characters)}")
    print(f"Total Wealth          : {total:,} Gold coins")
    print(f"Average Wealth        : {total / len(characters):,.2f} Gold coins")
    print("="*50)
    print()


def save_characters():
    """
    Save characters to file using GUI file chooser.
    Opens file dialog to allow user to choose save location.
    :return: None
    """
    print("\nSaving characters to file...")
    save_characters_to_file(characters)


def load_characters():
    """
    Load characters from file using GUI file chooser.
    Opens file dialog to allow user to choose file to load from.
    :return: None
    """
    global characters
    print("\nLoading characters from file...")
    loaded_characters = load_characters_from_file()
    if loaded_characters:
        characters.extend(loaded_characters)


def main():
    """
    Main application loop for the character management system.
    Displays menu and handles user input until user chooses to exit.
    :return: None
    """
    print("Welcome to the Character Management System!")
    print(
        "This system allows you to create, manage, and store game characters.")

    while True:
        display_menu()
        choice = input().strip()

        if choice == "1":
            add_character()
        elif choice == "2":
            add_character_gui()
        elif choice == "3":
            list_all_characters()
        elif choice == "4":
            search_characters_by_name()
        elif choice == "5":
            total_wealth()
        elif choice == "6":
            save_characters()
        elif choice == "7":
            load_characters()
        elif choice == "0":
            print("\nThank you for using Fantasy Game Character Manager!")
            print("Goodbye!")
            break
        else:
            print(f"\nInvalid selection '{choice}'. Please try again.\n")


if __name__ == "__main__":
    main()
