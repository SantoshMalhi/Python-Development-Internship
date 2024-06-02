import difflib

def load_text(file_path, encoding='utf-8'):
    """Load text from a file."""
    with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
        return file.read()

def check_plagiarism(text1, text2, threshold=0.8):
    """Check plagiarism between two texts."""
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    if similarity_ratio >= threshold:
        return True, similarity_ratio
    else:
        return False, similarity_ratio

def main():
    print("Welcome to the Python Plagiarism Checker!")

    # Load text documents
    file1_path = input("Enter the file path of the first text document: ")
    file2_path = input("Enter the file path of the second text document: ")

    text1 = load_text(file1_path)
    text2 = load_text(file2_path)

    # Check plagiarism
    is_plagiarized, similarity_ratio = check_plagiarism(text1, text2)

    if is_plagiarized:
        print("Plagiarism Detected!")
        print(f"Similarity Ratio: {similarity_ratio:.2f}")
    else:
        print("No Plagiarism Detected.")
        print(f"Similarity Ratio: {similarity_ratio:.2f}")

if __name__ == "__main__":
    main()
