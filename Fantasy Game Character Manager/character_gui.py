# character_gui.py

"""
Character creation GUI for the character management system.

This module contains the CharacterCreationGUI class which provides
a graphical user interface for creating new characters in fantasy game.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import re
from character import Character
from warrior import Warrior
from mage import Mage


class CharacterCreationGUI:
    """
    GUI class for character creation with form validation.
    Provides a graphical interface for creating characters with
    input validation,
    role-specific fields, and character object creation.
    """

    def __init__(self):
        """
        Initialize the character creation GUI window.
        Sets up all GUI components, binds events, and configures the window.
        :return: None
        """
        self.result = None
        self.root = tk.Tk()
        self.root.title("Add New Character")
        self.root.geometry("470x550")
        self.root.resizable(False, False)

        # Set up window close protocol
        self.root.protocol("WM_DELETE_WINDOW", self.cancel)

        # Make window modal and bring to front
        self.root.transient()
        self.root.grab_set()
        self.root.focus_force()

        # Bind keyboard shortcuts
        self.root.bind('<Escape>', lambda event: self.cancel())
        self.root.bind('<Return>', lambda event: self.create_character())

        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(
            main_frame, text="Create New Character", font=('Arial', 16, 'bold')
            )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Character Name
        ttk.Label(
            main_frame, text="Character Name:"
            ).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(
            main_frame, textvariable=self.name_var, width=30)
        self.name_entry.grid(
            row=1, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        # Race
        ttk.Label(
            main_frame, text="Race:"
            ).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.race_var = tk.StringVar()
        self.race_combo = ttk.Combobox(
            main_frame, textvariable=self.race_var,
            values=['Elf', 'Dwarf', 'Human'], state='readonly', width=27)
        self.race_combo.grid(
            row=2, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        # Role
        ttk.Label(main_frame, text="Role:").grid(
            row=3, column=0, sticky=tk.W, pady=5)
        self.role_var = tk.StringVar()
        self.role_combo = ttk.Combobox(
            main_frame, textvariable=self.role_var,
            values=['Warrior', 'Mage'], state='readonly', width=27)
        self.role_combo.grid(
            row=3, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        self.role_combo.bind('<<ComboboxSelected>>', self.on_role_changed)

        # Skill Level
        ttk.Label(main_frame, text="Skill Level:").grid(
            row=4, column=0, sticky=tk.W, pady=5)
        self.skill_var = tk.StringVar()
        self.skill_combo = ttk.Combobox(
            main_frame, textvariable=self.skill_var,
            values=['1', '2', '3', '4', '5'], state='readonly', width=27)
        self.skill_combo.grid(
            row=4, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        # Wealth
        ttk.Label(main_frame, text="Wealth (Gold coins):").grid(
            row=5, column=0, sticky=tk.W, pady=5)
        self.wealth_var = tk.StringVar()
        self.wealth_entry = ttk.Entry(
            main_frame, textvariable=self.wealth_var, width=30)
        self.wealth_entry.grid(
            row=5, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        # Separator
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.grid(
            row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)

        # Role-specific frame
        self.role_frame = ttk.LabelFrame(
            main_frame, text="Role-Specific Attributes", padding="10")
        self.role_frame.grid(
            row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # Warrior-specific widgets
        self.warrior_frame = ttk.Frame(self.role_frame)

        ttk.Label(self.warrior_frame, text="Weapon:").grid(
            row=0, column=0, sticky=tk.W, pady=5)
        self.weapon_var = tk.StringVar()
        self.weapon_combo = ttk.Combobox(
            self.warrior_frame, textvariable=self.weapon_var,
            values=['Sword', 'Axe'], state='readonly', width=25)
        self.weapon_combo.grid(
            row=0, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        ttk.Label(self.warrior_frame, text="Armour:").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        self.armour_var = tk.StringVar()
        self.armour_combo = ttk.Combobox(
            self.warrior_frame, textvariable=self.armour_var,
            values=['Chainmail', 'Plate'], state='readonly', width=25)
        self.armour_combo.grid(
            row=1, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        # Mage-specific widgets
        self.mage_frame = ttk.Frame(self.role_frame)

        ttk.Label(self.mage_frame, text="Spell:").grid(
            row=0, column=0, sticky=tk.W, pady=5)
        self.spell_var = tk.StringVar()
        self.spell_combo = ttk.Combobox(
            self.mage_frame, textvariable=self.spell_var,
            values=['Fireball', 'Lightning'], state='readonly', width=25)
        self.spell_combo.grid(
            row=0, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        ttk.Label(self.mage_frame, text="Mana Points (0-100):").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        self.mana_var = tk.StringVar()
        self.mana_entry = ttk.Entry(
            self.mage_frame, textvariable=self.mana_var, width=28)
        self.mana_entry.grid(
            row=1, column=1, sticky=tk.W, padx=(10, 0), pady=5)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        ttk.Button(
            button_frame, text="Create Character",
            command=self.create_character).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(
            button_frame, text="Cancel",
            command=self.cancel).pack(side=tk.LEFT)

        # Initially hide role-specific frames
        self.hide_role_frames()

    def on_role_changed(self, event=None):
        """
        Handle role selection change to show appropriate role-specific fields.
        :param event: tkinter event object, optional event parameter
        from combobox
        :return: None
        """
        role = self.role_var.get().lower()
        self.hide_role_frames()

        if role == 'warrior':
            self.warrior_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        elif role == 'mage':
            self.mage_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    def hide_role_frames(self):
        """
        Hide all role-specific frames to reset the UI state.
        :return: None
        """
        self.warrior_frame.grid_remove()
        self.mage_frame.grid_remove()

    def validate_inputs(self):
        """
        Validate all form inputs including basic character data and
        role-specific fields.
        Checks for empty fields, invalid formats, and role-specific
        validation rules.
        :return: bool, True if all inputs are valid, False otherwise
        """
        # Basic validation
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror(
                "Validation Error", "Character name cannot be empty.")
            return False
        if not re.match("^[a-zA-Z]+$", name):
            messagebox.showerror(
                "Validation Error", "Character name can only contain letters.")
            return False

        race = self.race_var.get()
        if not race:
            messagebox.showerror("Validation Error", "Please select a race.")
            return False

        role = self.role_var.get()
        if not role:
            messagebox.showerror("Validation Error", "Please select a role.")
            return False

        skill_level = self.skill_var.get()
        if not skill_level:
            messagebox.showerror(
                "Validation Error", "Please select a skill level.")
            return False

        wealth = self.wealth_var.get().strip()
        if not wealth:
            messagebox.showerror(
                "Validation Error", "Wealth cannot be empty.")
            return False
        if not wealth.isdigit():
            messagebox.showerror(
                "Validation Error", "Wealth must be a valid positive number.")
            return False
        if int(wealth) < 0:
            messagebox.showerror(
                "Validation Error", "Wealth cannot be negative.")
            return False

        # Role-specific validation
        if role.lower() == 'warrior':
            weapon = self.weapon_var.get()
            if not weapon:
                messagebox.showerror(
                    "Validation Error", "Please select a weapon.")
                return False

            armour = self.armour_var.get()
            if not armour:
                messagebox.showerror(
                    "Validation Error", "Please select armour.")
                return False

        elif role.lower() == 'mage':
            spell = self.spell_var.get()
            if not spell:
                messagebox.showerror(
                    "Validation Error", "Please select a spell.")
                return False

            mana = self.mana_var.get().strip()
            if not mana:
                messagebox.showerror(
                    "Validation Error", "Mana points cannot be empty.")
                return False
            if not mana.isdigit():
                messagebox.showerror(
                    "Validation Error", "Mana points must be a valid number.")
                return False
            if int(mana) < 0 or int(mana) > 100:
                messagebox.showerror(
                    "Validation Error", "Mana points must between 0 and 100.")
                return False

        return True

    def create_character(self):
        """
        Create character from form data after validation.
        Validates inputs, creates appropriate character object,
        and closes the window.
        :return: None
        """
        if not self.validate_inputs():
            return

        try:
            name = self.name_var.get().strip()
            race = self.race_var.get()
            role = self.role_var.get()
            skill_level = self.skill_var.get()
            wealth = self.wealth_var.get().strip()

            # Create appropriate character object
            if role.lower() == 'warrior':
                weapon = self.weapon_var.get()
                armour = self.armour_var.get()
                character = Warrior(
                    name, race, skill_level, wealth, weapon, armour)
            elif role.lower() == 'mage':
                spell = self.spell_var.get()
                mana_points = int(self.mana_var.get().strip())
                character = Mage(
                    name, race, skill_level, wealth, spell, mana_points)
            else:
                character = Character(name, race, role, skill_level, wealth)

            self.result = character
            messagebox.showinfo(
                "Success", f"Character '{name}' created successfully!")
            self.root.destroy()

        except ValueError as e:
            messagebox.showerror("Character Creation Error", str(e))

    def cancel(self):
        """
        Cancel character creation and close the window.
        Sets result to None and destroys the GUI window.
        :return: None
        """
        self.result = None
        self.root.destroy()

    def run(self):
        """
        Run the GUI and return the created character.
        Starts the main event loop and returns the character object or None
        if cancelled.
        :return: Character object or None, the created character or None
        if cancelled
        """
        self.root.mainloop()
        return self.result
