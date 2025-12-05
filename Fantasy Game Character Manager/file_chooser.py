# file_chooser.py

from tkinter.filedialog import askopenfilename, asksaveasfilename


def choose_open_file(message="Choose a file"):

    """
    Display a file chooser dialog for opening files.
    :param message: str, the title text for the dialog box
    :return: str, the chosen file name, or empty string if "Cancel" is pressed
    """

    FILETYPE = (
        ('Comma Separated Values', '*.csv'),
        ('All Files', '*.*')
    )

    filename = askopenfilename(title=message, filetypes=FILETYPE)
    return filename


def choose_save_file(message="Save file as"):
    """
    Display a file chooser dialog for saving files.
    :param message: str, the title text for the dialog box
    :return: str, the chosen file name for saving, or empty string
    if "Cancel" is pressed
    """

    FILETYPE = (
        ('Comma Separated Values', '*.csv'),
        ('All Files', '*.*')
    )

    filename = asksaveasfilename(
        title=message,
        filetypes=FILETYPE,
        defaultextension='.csv'
    )
    return filename
