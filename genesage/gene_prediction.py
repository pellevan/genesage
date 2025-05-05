import subprocess

def run_prodigal(fasta_file, output_prefix):
    subprocess.run([
        "prodigal", "-i", fasta_file,
        "-a", f"{output_prefix}.faa",
        "-d", f"{output_prefix}.ffn",
        "-f", "gff",
        "-o", f"{output_prefix}.gff",
        "-p", "meta"
    ], check=True)
