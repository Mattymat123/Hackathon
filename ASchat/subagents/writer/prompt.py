

import os

# Load concatenated_output.txt content
def load_concatenated_output():
    """Load the content from concatenated_output.txt into a string."""
    file_path = os.path.join(os.path.dirname(__file__), 'Extra_knowledge', 'concatenated_output.txt')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error loading concatenated_output.txt: {e}")
        return ""

# Load tabel_data.txt content
def load_tabel_data():
    """Load the content from tabel_data.txt into a string."""
    file_path = os.path.join(os.path.dirname(__file__), 'Extra_knowledge', 'tabel_data.txt')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error loading tabel_data.txt: {e}")
        return ""

# Load the concatenated output content
concatenated_content = load_concatenated_output()

# Load the tabel data content
tabel_data = load_tabel_data()

writer_prompt = f""" 
System Role:
Du er en AI assistent specialiseret i at aktstykker. Du er ekspert i retskrivning. Skriver kort og præcist med aktstivt sprog og dansk retskrivning inklusiv komma og andre grammatik hensyn. 
Din opgave er at skrive et aktstykke givet Aktstykkets detaljer og yderligere research. 
Du fokusere på at skrive et klart, sammenhængende og velformuleret aktstykke, der opfylder brugerens behov og krav. 
Når aktstykket er skrevet skal du outputte det. 



Additional Knowledge:
{concatenated_content}

Data til tabel 
{tabel_data}
"""
