# SHA Family

**Path:** Tech_Knowledge_System/Cybersecurity/Cryptography/Hash_Functions_and_MACs/SHA_Family
**Difficulty:** Intermediate
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
The SHA (Secure Hash Algorithm) family consists of cryptographic hash functions developed by NIST, including SHA-1, SHA-2 (SHA-256, SHA-512), and SHA-3. These algorithms generate fixed-size message digests from input data, primarily used for data integrity verification, digital signatures, and password storage.

## Key Concepts
- Cryptographic Hash: A one-way function producing a unique, fixed-size output from variable-size input.
- Collision Resistance: The property making it computationally infeasible to find two different inputs with the same hash output.
- SHA-2: A family including SHA-256 and SHA-512, built on the Merkle-Damgård construction.
- SHA-3 (Keccak): A distinct hash algorithm selected by NIST, based on the sponge construction, offering different security properties.
- Message Authentication Code (MAC): Often used with hash functions to provide both data integrity and authenticity.
- Digital Signature: Uses hash functions to ensure authenticity and non-repudiation of digital documents.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| OpenSSL | Library/Toolkit | Comprehensive cryptographic functions, including SHA implementations |
| Python `hashlib` | Library | Built-in module for various secure hash and message digest algorithms |
| Git | Version Control System | Uses SHA-1 (historically) and SHA-256 for commit and object integrity |
| Bitcoin | Blockchain Platform | Employs SHA-256 extensively for mining and transaction verification |

## Retrieval Keywords
SHA, Secure Hash Algorithm, SHA-1, SHA-2, SHA-3, SHA-256, SHA-512, cryptographic hash, message digest, collision resistance, preimage resistance, second preimage resistance, Merkle-Damgård, Keccak, NIST, FIPS, data integrity, digital signatures, blockchain, password hashing, cryptography, hash function family

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Hash_Functions_and_MACs (parent)
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Hash_Functions_and_MACs/MD5 (sibling)
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Digital_Signatures (related)
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Key_Management (related)

## Fast Queries This Node Should Answer
- "What is the SHA family of hash functions?"
- "How do SHA-256 and SHA-512 differ?"
- "When should I use SHA-3 instead of SHA-2?"
- "What are the main tools for implementing SHA functions?"
- "What are common vulnerabilities or failure modes in SHA implementations?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations