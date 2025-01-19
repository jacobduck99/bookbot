def main():
    path_to_file = "books/frankenstein.txt"

    # Read the file contents
    with open(path_to_file, "r") as f:
        file_contents = f.read()

    # Count words and characters
    word_count = count_words(file_contents)
    character_counts = count_characters(file_contents)

    # Convert character dictionary to a list of dictionaries
    char_list = [
        {"char": char, "num": count}
        for char, count in character_counts.items()
        if char.isalpha()  # Only include alphabetic characters
    ]

    # Sort the character list by the number of occurrences
    char_list.sort(reverse=True, key=sort_on)

    # Generate the required report
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()  # Make all characters lowercase for consistent counting
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1  # Increment count if character exists
        else:
            char_counts[char] = 1  # Initialize count if character is new
    return char_counts


def sort_on(dict):
    """Return the value of the 'num' key for sorting."""
    return dict["num"]


# Call the main function to execute the program
if __name__ == "__main__":
    main()
