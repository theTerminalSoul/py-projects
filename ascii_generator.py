import pyfiglet
import pyperclip


def generate_ascii_art():
    print("=== ASCII Art Generator & Clipboard Copier ===")

    # 1. Get the user input text
    text = input("Enter the text you want to convert: ").strip()

    if not text:
        print("Error: Text cannot be empty.")
        return

    # 2. Get font choice (Using actual valid pyfiglet font names)
    print("\nAvailable styles: standard, slant, 3d (isometric), alphabet, banner")
    font_choice = input("Choose a style (Press Enter for standard): ").strip().lower()

    # Map "3d" to a valid 3D-style font in pyfiglet
    if font_choice == "3d":
        font_choice = "isometric1"
    elif font_choice not in ["standard", "slant", "alphabet", "banner"]:
        font_choice = "standard"

    # 3. Generate the ASCII art
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font_choice)

        # Print to console
        print("\nYour ASCII Art:")
        print("-" * 40)
        print(ascii_art)
        print("-" * 40)

        # 4. Copy to clipboard
        pyperclip.copy(ascii_art)
        print("Success! The ASCII art has been copied to your clipboard.")

    except Exception as e:
        # Improved error reporting
        print(f"An error occurred: {type(e).__name__} - {e}")


if __name__ == "__main__":
    generate_ascii_art()
