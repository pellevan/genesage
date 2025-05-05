# 🐝 GeneSage

**GeneSage** is a lightweight CLI tool for predicting genes from genome assemblies and annotating them using known `.ffn` gene databases.

## ✨ Features
- Gene prediction via **Prodigal**
- Annotation via **BLASTn** against `.ffn` databases
- Accepts single or multiple `.ffn` files
- Generates summary statistics

## 🔧 Installation
```bash
# Prerequisites
conda install -c bioconda prodigal blast biopython

# Clone and install
git clone https://github.com/pellevan/genesage.git
cd genesage
pip install .
```

## Express Installation (not recommended) with `environment.yml`
```bash
conda env create -f environment.yml
conda activate genesage-env
```

Now you can run the tool with:
```bash
genesage --input genome.fasta --db db_folder_or_file --outdir results/
```

## 📂 Input Options
- `--input`: FASTA genome file
- `--db`: Single `.ffn` file **or** folder containing multiple `.ffn` files
- `--outdir`: Output directory

## 📄 Output Files
- `genes.gff` – Gene features
- `genes.ffn` – Gene sequences
- `genes.faa` – Protein sequences
- `annotations.tsv` – Matched annotations
- `summary_stats.txt` – Summary of annotations

## 🔍 Example
```bash
genesage \
  --input example_data/test_genome.fasta \
  --db example_data/ \
  --outdir output/
```

## 📖 License
MIT License © Pelle
