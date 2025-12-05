# Fantasy-Game-Character-Manager
A fantasy game management application built as my final project for a software development assignment, where the user can manage players/characters.

A professionally structured character management system featuring clean modular architecture with separated concerns and excellent maintainability.

## Features

- **Multiple Character Types**: General characters, Warriors, and Mages with specialized attributes
- **Dual Interface**: Console-based menu system and modern GUI interface
- **Data Persistence**: CSV file storage for character data
- **Comprehensive Validation**: Input validation and error handling
- **Object-Oriented Design**: Inheritance, encapsulation, and polymorphism
- **Full Test Coverage**: Comprehensive unit tests for all functionality

## Architecture

### Class Hierarchy
```
Character (Base Class)
├── Warrior (Specialized for combat)
└── Mage (Specialized for magic)
```

### Key Components
- **Character Management**: Core classes with inheritance
- **GUI Interface**: tkinter-based character creation form
- **File Operations**: CSV import/export functionality  
- **Input Validation**: Comprehensive data validation
- **Error Handling**: Exception handling for robust operation

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)

## Menu Options

1. **Add a Character** - Console-based character creation
2. **Add a Character (GUI)** - Modern GUI interface for character creation
3. **List all Characters** - Display all created characters
4. **Search for Characters by Name** - Find characters by name
5. **Total Wealth of all Characters** - Calculate combined wealth
6. **Save Characters to a File** - Export to CSV format
7. **Load Characters from a File** - Import from CSV format
0. **Exit Application** - Close the program

## Character Types

### General Character
- Name, Race (Elf/Dwarf/Human), Role, Skill Level (1-5), Wealth

### Warrior 🗡️
- All general attributes plus:
- Weapon (Sword/Axe)
- Armour (Chainmail/Plate)

### Mage
- All general attributes plus:
- Spell (Fireball/Lightning)
- Mana Points (0-100)

## GUI Features

- **Dynamic Interface**: Shows/hides specialized attributes based on character type
- **Input Validation**: Real-time validation with error dialogs
- **Professional Design**: Modern tkinter interface with organized layout
- **Dropdown Menus**: Race, role, skill level, weapon, armour, spell selections
- **Comprehensive Forms**: All character attributes in one interface

## Testing

The application includes comprehensive unit tests covering:

### Test Categories
- **Character Class Tests**: Base functionality and validation
- **Warrior Class Tests**: Specialized attributes and inheritance
- **Mage Class Tests**: Magic attributes and validation
- **File Operations Tests**: CSV handling and file I/O
- **Edge Cases Tests**: Boundary values and error conditions

### Test Results
```
Ran 17 tests in 0.001s
OK - All tests passing
```

### Coverage Areas
- Class initialization and inheritance
- Input validation for all attributes
- Boundary value testing
- Error handling and exceptions
- File operations and CSV handling
- Type checking and data integrity

## Security & Compliance

### Security Features
- **Input Validation**: Comprehensive validation prevents injection attacks
- **Error Handling**: Secure error handling without information disclosure
- **File Security**: Safe CSV operations using Python's csv module
- **Type Checking**: Strict type validation for all inputs

### Compliance Status
- **GDPR**: Partially compliant (data minimization, purpose limitation)
- **Security Standards**: Follows industry best practices
- **Code Quality**: PEP8 compliant (95/100 score)
- **Documentation**: Comprehensive documentation and risk assessment

See `SECURITY_ASSESSMENT.md` for detailed security analysis.

## Documentation

### Available Documentation
- **Source Code**: Comprehensive docstrings for all classes and methods
- **User Guide**: This README file
- **Test Documentation**: Complete test suite with descriptions
- **Security Assessment**: Risk analysis and compliance documentation
- **PEP8 Compliance**: Code style analysis and recommendations

### Code Documentation Examples
```python
class Character:
    """
    Base Character class for fantasy game characters.
    
    Represents a generic character with basic attributes common to all character types.
    Uses encapsulation with private attributes and public getter/setter methods.
    """
    
    def set_skill_level(self, skill_level):
        """Set skill level with validation (1-5)."""
        if not isinstance(skill_level, int) or skill_level < 1 or skill_level > 5:
            raise ValueError("Skill level must be an integer between 1 and 5")
        self._skill_level = skill_level
```

## Design Patterns

### Object-Oriented Principles
- **Inheritance**: Warrior and Mage inherit from Character
- **Encapsulation**: Private attributes with public getter/setter methods
- **Polymorphism**: Specialized behavior in inherited classes
- **Abstraction**: Clear separation of interface and implementation

### Code Organization
- **Single Responsibility**: Each class has a clear, single purpose
- **Open/Closed Principle**: Easy to extend with new character types
- **Liskov Substitution**: Derived classes can replace base class
- **DRY Principle**: No code duplication, shared functionality in base class

## Technical Implementation

### Data Structures
- **Classes**: Object-oriented character representation
- **Lists**: Dynamic character storage
- **Dictionaries**: CSV data handling
- **Strings**: Text processing and validation

### Error Handling
```python
try:
    # File operations with error handling
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(character_data)
except Exception as e:
    print(f"An error occurred while saving to file: {e}")
```

### Input Validation
```python
def set_race(self, race):
    """Set character race with validation."""
    valid_races = ["Elf", "Dwarf", "Human"]
    if race not in valid_races:
        raise ValueError(f"Race must be one of: {valid_races}")
    self._race = race
```

## Performance & Scalability

### Current Capabilities
- Handles hundreds of characters efficiently
- Fast CSV operations using Python's optimized csv module
- Memory-efficient object storage
- Responsive GUI interface

### Scalability Considerations
- Can be extended to database storage (SQLite/PostgreSQL)
- GUI can handle larger datasets with pagination
- Modular design allows easy feature additions

## Future Enhancements

### Potential Improvements
1. **Database Integration**: SQLite for better data management
2. **Web Interface**: Flask/Django web application
3. **Advanced Search**: Multiple criteria filtering
4. **Data Visualization**: Charts and graphs for character statistics
5. **Import/Export**: Multiple file formats (JSON, XML)
6. **User Authentication**: Multi-user support with login system


---
