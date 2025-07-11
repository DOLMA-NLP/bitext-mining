import json
import os
import random

# Dataset files
datasets = [
	"datasets/PARME+manual+vecalign+llm.jsonl",
	"datasets/PARME+manual+vecalign.jsonl",
	"datasets/PARME-llm.jsonl",
	"datasets/PARME-manual.jsonl",
	"datasets/PARME-vecalign.jsonl",
	"datasets/PARME-manual-ZZA_LLM.jsonl"
]

# Random seeds
seeds = [42, 123, 7]

# Load JSONL file
def load_jsonl(filepath):
	data = []
	with open(filepath, 'r', encoding='utf-8') as f:
		for line in f:
			if line.strip():
				data.append(json.loads(line))
	return data

# Save JSONL file
def save_jsonl(data, filepath):
	os.makedirs(os.path.dirname(filepath), exist_ok=True)
	with open(filepath, 'w', encoding='utf-8') as f:
		for item in data:
			f.write(json.dumps(item, ensure_ascii=False) + '\n')

# Process each dataset
for dataset_path in datasets:
	# Get dataset name
	dataset_name = os.path.basename(dataset_path)
	
	# Load data
	data = load_jsonl(dataset_path)
	
	# Create shuffled versions with each seed
	for seed in seeds:
		# Set seed and shuffle
		random.seed(seed)
		shuffled_data = data.copy()
		random.shuffle(shuffled_data)
		
		# Save shuffled data
		output_path = f"datasets/seed_{seed}/{dataset_name}"
		save_jsonl(shuffled_data, output_path)

print("Completed shuffling datasets with seeds 42, 123, and 7.")