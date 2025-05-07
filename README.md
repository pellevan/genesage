# 🧙 GeneSage

**GeneSage** is a lightweight, user-friendly command-line tool for gene prediction and annotation. It uses **Prodigal** to identify genes from genome assemblies and annotates them using **BLASTn** against custom `.ffn` gene databases.

## ✨ Features

- Gene prediction via **Prodigal**
- Annotation via **BLASTn** against `.ffn` databases
- Accepts single or multiple `.ffn` files
- Generates summary statistics

## 🔧 Installation

### Prerequisites

```bash
# Activate base environment
conda activate base

# Install dependencies
conda install -c bioconda prodigal blast biopython
```

### Clone and install

```bash
git clone https://github.com/pellevan/genesage.git
cd genesage
pip install .
```

### Optional: Environment setup (not recommended)

```bash
conda env create -f environment.yml
conda activate genesage-env
```

## 🚀 Usage

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
