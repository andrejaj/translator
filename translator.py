from deep_translator import GoogleTranslator
import time

def translate_srt(input_file, output_file, source_language, destination_langiage):
    # Initialize the translator
    translator = GoogleTranslator(source=source_language, target=destination_langiage)

    # Read the input SRT file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Write the translated content to the output SRT file
    with open(output_file, 'w', encoding='utf-8') as file:
        for i, line in enumerate(lines):
            # Keep timestamps and numbering unchanged
            if line.strip().isdigit() or '-->' in line:
                file.write(line)
            else:
                try:
                    # Translate the text from Romanian (ro) to English (en)
                    translated = translator.translate(line.strip())  # Use .strip() to remove extra whitespace
                    file.write(translated + '\n')
                    print(f"Translated line {i + 1}: {line.strip()} -> {translated}")
                except Exception as e:
                    # Handle translation errors (e.g., API limits, network issues)
                    print(f"Error translating line {i + 1}: {line.strip()} - {e}")
                    file.write(line)  # Write the original line if translation fails

                # Add a delay to avoid hitting API rate limits
                time.sleep(1)

# Example usage
translate_srt('source.srt', 'destination.srt','ro','en')