import re

def remove_spaces_quotes(text):
  """Removes spaces and quotation marks (single or double) from a string.

  Args:
      text: The string to process.

  Returns:
      str: The string with spaces and quotation marks removed.
  """
  return re.sub(r'[ "\']', '', text)

def remove_surrounding_spaces(filename):
  """Removes leading, trailing, and repeated spaces around the filename using regex.

  Args:
      filename: The filename string with potential surrounding spaces.

  Returns:
      The filename string with surrounding spaces removed.
  """
  pattern = r"(^\"|\'$|^ |\s+$|\"$|\'$)"  # Matches leading, trailing, or multiple spaces
  return re.sub(pattern, "", filename).strip()  # Substitute matches with empty string and remove extra spaces