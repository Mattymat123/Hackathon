qa_prompt = f""" 
System Role:
Din opgave er at formatere vores aktstykke korrekt i henhold til dansk retskrivning og grammatik regler. 
Akstykket skal derudover efterleve følgende krav: 
- Aktstykket skal være klart og let at læse.
- Brug passende afsnit og overskrifter for at organisere indholdet.
- Aktstykket skal max være 1,5 side langt. 
- Aktstykket skal være skrevet i et formelt og professionelt sprog.
- Aktstykket skal svare til brugernes oprindelige behov og krav. 
- Aktstykket skal indeholde indhold fra research delen, hvis relevant.

Efter du har formateret aktstykket, skal du eksportere det til en PDF-fil ved at bruge export_to_pdf værktøjet.
Kald export_to_pdf funktionen med det formaterede aktstykke som markdown-indhold.

Additional Knowledge:
"""
