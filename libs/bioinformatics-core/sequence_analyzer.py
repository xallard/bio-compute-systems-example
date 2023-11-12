# sequence_analyzer.py
# Script for analyzing genetic sequences using Biopython

# Part of a module for analyzing genetic sequences. 
# The script would be appropriately placed in the bioinformatics-core library within the project structure.

from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.Seq import Seq


class SequenceAnalyzer:
    def __init__(self, sequence_file):
        self.sequence_file = sequence_file
        self.sequences = []

    def load_sequences(self):
        """
        Load sequences from a file using Biopython SeqIO
        """
        with open(self.sequence_file, "r") as file:
            for record in SeqIO.parse(file, "fasta"):
                self.sequences.append(record)
        print(f"{len(self.sequences)} sequences loaded.")

    def calculate_gc_content(self):
        """
        Calculate and return the GC content for each sequence
        """
        return [(seq.id, GC(seq.seq)) for seq in self.sequences]

    def find_motifs(self, motif):
        """
        Find and return positions of a given motif in each sequence
        """
        motif_seq = Seq(motif)
        results = {}
        for seq in self.sequences:
            positions = [
                pos
                for pos, _ in enumerate(seq.seq)
                if seq.seq.startswith(motif_seq, pos)
            ]
            results[seq.id] = positions
        return results


# Example usage
if __name__ == "__main__":
    analyzer = SequenceAnalyzer("path/to/your/sequence/file.fasta")
    analyzer.load_sequences()

    gc_content = analyzer.calculate_gc_content()
    print("GC Content:", gc_content)

    motif_positions = analyzer.find_motifs("ATG")
    print("Motif Positions:", motif_positions)

# In this script:

# Biopython's SeqIO is used for reading sequence data from a file.
# The SequenceAnalyzer class offers functionalities to load sequences, calculate GC content, and find specific motifs within the sequences.
# The example usage at the bottom demonstrates how to use the class and its methods.
# This script, as part of the bioinformatics-core library in the BioComputeSystems project, would serve as a foundational tool for more complex genetic sequence analysis and could be further integrated into larger workflows or applications within the project.
