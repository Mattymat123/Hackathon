


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

# Load the concatenated output content
concatenated_content = load_concatenated_output()

writer_prompt = f""" 
System Role:
Du er en AI Assistant til at skrive tekniske blogindlæg, der altid svarer på dansk.

Additional Knowledge:
{concatenated_content}
"""
