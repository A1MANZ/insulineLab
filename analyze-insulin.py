import re

def clean_text(text):
  # Remove comments
  text = re.sub(r"//.*", "", text)

  # Remove numbers
  text = re.sub(r"\d+", "", text)

  # Remove spaces
  text = re.sub(r"\s+", "", text)

  # Remove Origin
  text = re.sub(r"ORIGIN", "", text)

  return text


if __name__ == "__main__":
  text = """
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""

  with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(clean_text(text))

  with open("preproinsulin-seq-clean.txt", "r") as f:
    text = f.read()

  lsinsulin_seq = text[:24]
  binsulin_seq = text[25:54]
  cinsulin_seq = text[55:89]
  ainsulin_seq = text[90:110]

  with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin_seq)

  with open("binsulin-seq-clean.txt", "w") as f:
    f.write(binsulin_seq)

  with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin_seq)

  with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin_seq)