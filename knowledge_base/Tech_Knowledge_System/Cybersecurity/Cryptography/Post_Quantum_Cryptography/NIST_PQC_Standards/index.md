# NIST PQC Standards

**Path:** Tech_Knowledge_System/Cybersecurity/Cryptography/Post_Quantum_Cryptography/NIST_PQC_Standards
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
The NIST Post-Quantum Cryptography (PQC) Standards are a set of cryptographic algorithms selected and standardized by the National Institute of Standards and Technology (NIST) to resist attacks from future quantum computers, ensuring long-term data security.

## Key Concepts
- Post-Quantum Cryptography (PQC) → Cryptographic systems designed to be secure against attacks by quantum computers.
- Standardization Process → NIST's rigorous, multi-round competition and evaluation process for selecting quantum-resistant algorithms.
- Quantum Resistance → The ability of a cryptographic algorithm to maintain its security against attacks from quantum computers.
- CRYSTALS-Kyber (ML-KEM) → A key encapsulation mechanism (KEM) selected by NIST for standardization, based on lattice-based cryptography.
- CRYSTALS-Dilithium (ML-DSA) → A digital signature algorithm (DSA) selected by NIST for standardization, also based on lattice-based cryptography.
- Sphincs+ → A stateless hash-based digital signature scheme selected by NIST, offering strong security guarantees.
- FALCON → A lattice-based digital signature algorithm selected by NIST, known for its efficiency.
- HQC → A code-based key encapsulation mechanism selected in the fourth round of the NIST PQC standardization process.
- FIPS 203, 204, 205 → Federal Information Processing Standards documents for ML-KEM, ML-DSA, and Sphincs+, respectively.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| OpenSSL | Library | Implementation of cryptographic protocols and algorithms, including PQC candidates |
| liboqs | Library | Open-source C library for quantum-safe cryptography, supporting NIST PQC algorithms |
| Bouncy Castle | Library | Java and C# cryptographic APIs, including PQC algorithms |
| Custom Hardware Security Modules (HSMs) | Hardware | Secure storage and processing of cryptographic keys and operations, adapted for PQC |

## Retrieval Keywords
NIST, Post-Quantum Cryptography, PQC, Quantum-Resistant Algorithms, Cryptography Standards, Quantum Computing, ML-KEM, CRYSTALS-Kyber, ML-DSA, CRYSTALS-Dilithium, Sphincs+, FALCON, HQC, FIPS, Quantum Security, Cryptographic Transition, Lattice-based Cryptography, Hash-based Signatures, Code-based Cryptography, Quantum Safe, Cybersecurity, Cryptographic Agility, Quantum Threat, Standardization Process, NIST IR 8545

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Post_Quantum_Cryptography: Parent node, foundational concepts of PQC
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Symmetric_Key_Cryptography: Related to underlying cryptographic primitives
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Asymmetric_Key_Cryptography: Related to traditional public-key cryptography being replaced
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Cryptographic_Agility: Concept of transitioning between cryptographic algorithms

## Fast Queries This Node Should Answer
- "What are the NIST Post-Quantum Cryptography Standards?"
- "How does the NIST PQC standardization process work?"
- "When should I use NIST PQC Standards?"
- "What are the main algorithms selected by NIST for PQC?"
- "What are common challenges in implementing NIST PQC Standards?"
- "What is ML-KEM?"
- "What is ML-DSA?"
- "What is Sphincs+?"
- "What is FALCON?"
- "What is HQC?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations