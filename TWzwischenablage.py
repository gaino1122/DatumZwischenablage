import pyperclip
import time
import re
from datetime import datetime

# Funktion zum Ersetzen des Datums in einem gegebenen Text
def replace_date_in_text(text):
    # Aktuelles Datum im gewünschten Format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Regex, um ein Datum im Format yyyy-mm-dd zu finden chatgpt zauber
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    
    # Ersetzen des Datums im Text
    new_text = re.sub(date_pattern, current_date, text)
    
    return new_text

# Überwachung der Zwischenablage
def monitor_clipboard():
    recent_value = ""
    while True:
        clipboard_value = pyperclip.paste()
        if clipboard_value != recent_value:
            recent_value = clipboard_value
            if re.search(r'\d{4}-\d{2}-\d{2}', clipboard_value):
                new_value = replace_date_in_text(clipboard_value)
                pyperclip.copy(new_value)
                print(f'Zwischenablage aktualisiert: {new_value}')
        time.sleep(1)

if __name__ == "__main__":
    monitor_clipboard()

    ## Datum in der zwischenablage immer auf das akutelle Datum
