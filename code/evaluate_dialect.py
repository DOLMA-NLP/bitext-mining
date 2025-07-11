from sacrebleu.metrics import BLEU, CHRF
import json

# languages having more than one dialect
testset_path = "/home/seahma/DOLMA/datasets"
testsets = ["GLK", "HAC", "LKI", "SDH"] # Only these have more than one dialect. These don't have: ["ZZA", "BQI", "MZN", "TLY"]

# fine-tuned models
trans_path = "evaluation_results_seed_123"
translations = ["nllb_finetuned_pm",
				"nllb_finetuned_pv",
				"nllb_finetuned_pmv",
				"nllb_finetuned_pl",
				"nllb_finetuned_pmvl",
				"nllb_finetuned_pmzl",
				]# "nllb_finetuned_base", "baseline"

# zero-shot baseline models
proxy_langs = {
	"GLK": ("GLK-arab_results.json", "pes_Arab"),
	"HAC": ("HAC-arab_results.json", "ckb_Arab"),
	"LKI": ("LKI-arab_results.json", "pes_Arab"),
	"SDH": ("SDH-arab_results.json", "ckb_Arab")
	}

bleu = BLEU()


for trans in translations:
	if trans == "nllb_finetuned_base": # base model on PARME only with 20 epochs
		trans_path = "/home/seahma/DOLMA/evaluation_results/X-ENG/"
	
	for lang_code in testsets:
		with open("%s/%s-test.tsv"%(testset_path, lang_code), "r") as f:
			test = f.read().splitlines()

		if trans == "baseline":
			# baseline models
			with open("/home/seahma/DOLMA/zero-shot-eval/outputs_600M/" + proxy_langs[lang_code][0], "r") as f:
				translation = json.load(f)
		else:
			# fine-tuned models
			with open("%s/%s/%s_translations.tsv"%(trans_path, trans, lang_code), "r") as f:
				translation = f.read().splitlines()

		dialects = set([i.split("\t")[3] for i in test if "variety" not in i.split("\t")[3]])
	
		hypotheses, references = list(), list()
		for dialect in dialects:
			if trans == "baseline":
				references = translation["target"]
				hypotheses = translation["translations"][proxy_langs[lang_code][1]]["eng_Latn"]
			else:
				for t, h in zip(test, translation):
					if dialect == t.split("\t")[3]:
						references.append(h.split("\t")[1])
						hypotheses.append(h.split("\t")[2])

			bleu_score = bleu.corpus_score(hypotheses, [references])
			print("\t".join([trans, lang_code, dialect, str(bleu_score).split("BLEU = ")[1].split()[0]]))

