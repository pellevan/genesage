import argparse
import os
import glob
from genesage.gene_prediction import run_prodigal
from genesage.annotation import run_blastn, parse_blast_output, compute_stats

def parse_args():
    parser = argparse.ArgumentParser(description="Predict and annotate genes from genome assemblies.")
    parser.add_argument('--input', required=True, help="Input genome FASTA file")
    parser.add_argument('--db', required=True, help="Path to .ffn file or folder containing .ffn files")
    parser.add_argument('--outdir', required=True, help="Output directory")
    return parser.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    prefix = os.path.join(args.outdir, "genes")

    print("[*] Running gene prediction with Prodigal...")
    run_prodigal(args.input, prefix)

    print("[*] Preparing annotation database(s)...")
    db_files = []
    if os.path.isdir(args.db):
        db_files = glob.glob(os.path.join(args.db, '*.ffn'))
    else:
        db_files = [args.db]

    combined_db = os.path.join(args.outdir, "combined_db.ffn")
    with open(combined_db, 'w') as out_f:
        for db_file in db_files:
            with open(db_file) as in_f:
                out_f.write(in_f.read())

    print("[*] Annotating predicted genes using BLASTn...")
    blast_output = os.path.join(args.outdir, "blast_results.tsv")
    run_blastn(f"{prefix}.ffn", combined_db, blast_output)

    print("[*] Generating annotation table and statistics...")
    annotation_file = os.path.join(args.outdir, "annotations.tsv")
    parse_blast_output(blast_output, annotation_file)
    stats_file = os.path.join(args.outdir, "summary_stats.txt")
    compute_stats(blast_output, stats_file)

    print(f"[\u2713] Done. Results saved in {args.outdir}")

if __name__ == "__main__":
    main()
