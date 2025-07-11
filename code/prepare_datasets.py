import json
import csv
import re
import transliterate_hac

"""
	This script reads manually aligned files and those aligned by Vecalign (using Sonar) and converts them all for training purposes into the jsonl format.
"""

def save_splits(target_file, data):
	with open(target_file, "w", encoding="utf-8") as f:
		for entry in data:
			f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def is_valid(line):
	# This pattern checks if the line contains at least one non-Latin character
	pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\u1100-\u11FF\u3040-\u309F\u30A0-\u30FF\u3400-\u4DBF\u4E00-\u9FFF\uAC00-\uD7AF]')
	
	# Return True if at least one non-Latin character is found
	return bool(pattern.search(line))

def clean_sentence(text, language_code):
	zza_map = {
			"ı": "i",
			"i": "î",
			"I": "I",
			"İ": "Î"
		}

	if language_code != "zza_Latn":
		# clean Arabic based scripts
		# normalize digits
		text = transliterate_hac.preprocessor_ckb.unify_numerals(text)

	# else:
	# 	# transliterate to Bedirxan's orthography
	# 	for i in zza_map:
	# 		text = text.replace(i, zza_map[i])

	return text

# # ========  Vecalign aligned

# vecalign_files = [
# 	("Vecalign/HAC-alignments_vecalign-1984.tsv", "hac_Arab", "novel", "George Orwell's 1984"),
# 	("Vecalign/GLK-alignments-animal-farm.tsv", "glk_Arab", "novel", "George Orwell's Animal Farm"),
# 	("Vecalign/Tuesdays-with-Morrie_alignment.tsv", "sdh_Arab", "novel", "Morrie"),
# 	("Vecalign/HAC-Alignment-the-stranger.tsv", "hac_Arab", "novel", "Stranger"),
# 	("Vecalign/HAC-Alignment-Seagul.tsv", "hac_Arab", "novel", "Seagul"),
# 	("Vecalign/HAC-alignment-petit-prince.tsv", "hac_Arab", "novel", "Le Petit Prince"),
# 	("Vecalign/HAC-Alignment-old-man.tsv", "hac_Arab", "novel", "Old Man")
# ]

# translations = list()
# for data in vecalign_files:
# 	file, language_code, genre, title = data
# 	with open(file, "r") as f:
# 		for line in f.read().splitlines():
# 			source, target = line.split("\t")[0], line.split("\t")[1]
# 			if len(source) and len(target):
# 				# translations.append(source target)
# 				translations.append({"translation": {language_code: target, "eng_Latn": source}})

# save_splits("datasets/vecalign.jsonl", translations)


# # ======== Manually aligned sentences

# manual_aligned = [
# 	("Spreadsheet/GLK.tsv", "glk_Arab"),
# 	("Spreadsheet/HAC-en-hac.tsv", "hac_Arab"),
# 	("Spreadsheet/LKI-en-lki.tsv", "lki_Arab"),
# 	("Spreadsheet/SDH-en-sdh.tsv", "sdh_Arab")
# ]

# translations = list()
# for data in manual_aligned:
# 	file, language_code = data
# 	with open(file) as f:
# 		sheet = f.read().splitlines()[1:]
# 		for line in sheet:
# 			source, target = line.split("\t")[0], line.split("\t")[1]
# 			if len(source) and len(target):
# 				# translations.append(source target)
# 				translations.append({"translation": {language_code: target, "eng_Latn": source}})

# save_splits("datasets/manual.jsonl", translations)

# ========  LLM aligned synthetic data

llm_files = [
	("LLMs/results_gilaki.csv", "glk_Arab"),
	("LLMs/results_hawrami.csv", "hac_Arab"),
	("LLMs/results_mazanderani.csv", "mzn_Arab"),
	("LLMs/results_southern_kurdish.csv", "sdh_Arab"),
	("LLMs/results_zazaki.csv", "zza_Latn")
]

lang_counter = {}
translations = list()
for data in llm_files:
	file, language_code = data
	with open(file, newline='\n') as csvfile:
		sheet = csv.reader(csvfile, delimiter=',')
		next(sheet)
		for line in sheet:
			source, target = line[0], line[1]
			if len(source) and len(target):
				source = clean_sentence(source, language_code)

				if language_code in lang_counter:
					lang_counter[language_code] += 1
				else:
					lang_counter.update({language_code: 1})

				if language_code != "zza_Latn":
					if is_valid(source):
						# translations.append(source target)
						translations.append({"translation": {language_code: source, "eng_Latn": target}})
				else:
					translations.append({"translation": {language_code: source, "eng_Latn": target}})
print(lang_counter)
# save_splits("datasets/llm.jsonl", translations)