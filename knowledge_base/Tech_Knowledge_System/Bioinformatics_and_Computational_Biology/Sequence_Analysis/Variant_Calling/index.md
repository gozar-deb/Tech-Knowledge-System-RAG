# Variant Calling

**Path:** Tech_Knowledge_System/Bioinformatics_and_Computational_Biology/Sequence_Analysis/Variant_Calling
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Variant calling is the computational process of identifying genetic differences, such as single nucleotide polymorphisms (SNPs) and small insertions/deletions (indels), between a sample's sequencing data and a reference genome. It is a fundamental step in genomic analysis, crucial for understanding genetic variation and its implications.

## Key Concepts
- **SNP (Single Nucleotide Polymorphism)** → A variation at a single base pair in a DNA sequence.
- **Indel (Insertion/Deletion)** → Small insertions or deletions of nucleotides in a DNA sequence.
- **Reference Genome** → A representative, complete DNA sequence used as a standard for comparison.
- **Alignment** → Mapping sequencing reads to positions on a reference genome.
- **Genotyping** → Determining the specific alleles an individual possesses at a particular locus.
- **Quality Score (QUAL)** → A measure of the confidence in a variant call, indicating the probability of error.
- **VCF (Variant Call Format)** → Standard file format for storing gene sequence variations.
- **Somatic Variant Calling** → Identification of mutations in non-reproductive cells, often associated with disease.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| GATK | Framework | Comprehensive toolkit for variant discovery and genotyping |
| BCFtools | Command-line | Manipulating VCF/BCF files and performing variant calling |
| FreeBayes | Caller | Bayesian genetic variant detector for SNPs, indels, and complex events |
| VarScan2 | Caller | Detects somatic mutations and germline variants from NGS data |
| DeepVariant | Deep Learning | Google's deep learning-based variant caller for highly accurate calls |

## Retrieval Keywords
Variant calling, SNP, indel, genomics, bioinformatics, sequence analysis, genetic variation, reference genome, alignment, genotyping, GATK, BCFtools, FreeBayes, DeepVariant, somatic mutations, germline variants, VCF, next-generation sequencing, NGS, population genetics, disease association, genomic medicine

## Related Nodes
- → Tech_Knowledge_System/Bioinformatics_and_Computational_Biology/Sequence_Analysis: parent (provides context on sequence analysis)
- → Tech_Knowledge_System/Bioinformatics_and_Computational_Biology/Genomics: broader domain (genomics principles)
- → Tech_Knowledge_System/Bioinformatics_and_Computational_Biology/Data_Analysis/Statistical_Genetics: related (statistical methods for variant interpretation)

## Fast Queries This Node Should Answer
- "What is Variant Calling?"
- "How does Variant Calling work?"
- "When should I use Variant Calling?"
- "What are the main tools for Variant Calling?"
- "What are common failures in Variant Calling?"
- "What is the difference between germline and somatic variant calling?"
- "How are variant calls quality controlled?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations