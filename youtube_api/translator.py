from googletrans import Translator


# Function to read the contents of a txt file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# Function to write translated text to a txt file
def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

# Translate text to French and return translated text
def translate_to_french(text):
    translator = Translator()
    return translator.translate(text, src='en', dest='fr')

# Translate text to Spanish and return translated text
# def translate_to_spanish(text):
#     translator = Translator()
#     spanish_translation = translator.translate(text, dest='es').text
#     return spanish_translation

# Main function to translate file contents to French and Spanish
def translate_file(filename):
    # Read file contents
    try:

        text = read_file(filename)
        # print(text)
        # Translate to French
        write_file('{}_fr.txt'.format(filename), translate_to_french(text))

        # Translate to Spanish
        # spanish_translation = translate_to_spanish(text)
        # write_file(f'{filename}_es.txt', spanish_translation)

        print('Translation complete. Translated files saved as {}_fr.txt and {}_es.txt.'.format(filename, filename))
    except Exception as e:
        print('error', e)
# Example usage
translate_file('category.txt')
