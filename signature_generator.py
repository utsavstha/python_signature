from collections import Counter

# Class responsible for generating a signature from extracted text
class SignatureGenerator:
    def __init__(self, text):
        self.__text = text

    def find_unique_marker_lines(self):
        # Split the text into individual lines
        lines = self.__text.splitlines()

        # Count the occurrences of each line using a Counter
        line_counts = Counter(lines)

        # Initialize an empty set to store unique marker lines
        unique_lines = set()

        # Iterate through each line and check its count
        for line, count in line_counts.items():
            if count == 1:
                # If a line appears only once, add it to the set of unique marker lines
                unique_lines.add(line)

        # Return the set of unique marker lines
        return unique_lines

