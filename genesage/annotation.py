import subprocess
from Bio import SeqIO

def run_blastn(query_ffn, db_ffn, output_file):
    subprocess.run(["makeblastdb", "-in", db_ffn, "-dbtype", "nucl"], check=True)
    subprocess.run([
        "blastn", "-query", query_ffn, "-db", db_ffn,
        "-outfmt", "6 qseqid sseqid pident length evalue bitscore",
        "-out", output_file, "-max_target_seqs", "1", "-perc_identity", "80"
    ], check=True)

def parse_blast_output(blast_file, output_tsv):
    annotations = {}
    with open(blast_file) as bf:
        for line in bf:
            qid, sid, ident, length, evalue, score = line.strip().split("\t")
            annotations[qid] = {
                "subject": sid, "identity": ident, "evalue": evalue, "bitscore": score
            }

    with open(output_tsv, "w") as out:
        out.write("Query_ID\tBest_Hit_ID\tIdentity\tE-value\tBitscore\n")
        for qid, info in annotations.items():
            out.write(f"{qid}\t{info['subject']}\t{info['identity']}\t{info['evalue']}\t{info['bitscore']}\n")

def compute_stats(fasta_file, annotation_file, output_txt):
    # Count total predicted genes
    with open(fasta_file) as f:
        total = sum(1 for line in f if line.startswith(">"))

    # Count unique annotated genes
    annotated_genes = set()
    with open(annotation_file) as f:
        for line in f:
            if line.strip():
                query_id = line.split('\t')[0]
                annotated_genes.add(query_id)

    annotated = len(annotated_genes)

    # Write stats
    with open(output_txt, 'w') as out:
        out.write(f"Total genes predicted: {total}\n")
        out.write(f"Annotated genes: {annotated}\n")