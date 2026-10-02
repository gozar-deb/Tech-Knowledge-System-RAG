# Hash Functions and MACs

**Path:** Tech_Knowledge_System/Cybersecurity/Cryptography/Hash_Functions_and_MACs
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Hash functions are cryptographic algorithms that map arbitrary-size data to fixed-size outputs, ensuring data integrity. Message Authentication Codes (MACs) are keyed hash functions that provide both data integrity and authenticity, verifying the message's origin and preventing unauthorized alterations.

## Key Concepts
- Hash Function → A one-way mathematical algorithm producing a fixed-size output (digest).
- Message Authentication Code (MAC) → A cryptographic checksum generated using a secret key to ensure integrity and authenticity.
- Collision Resistance → The property making it computationally infeasible to find two different inputs with the same hash output.
- Data Integrity → The assurance that data has not been modified or corrupted since it was created or transmitted.
- Message Authenticity → The verification that a message originates from the claimed sender and has not been tampered with.
- HMAC (Hash-based Message Authentication Code) → A specific construction for calculating a MAC using a cryptographic hash function and a secret key.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| SHA-256 | Algorithm | Widely used cryptographic hash function for integrity checks |
| HMAC-SHA256 | Algorithm | Standard MAC construction for message authentication and integrity |
| OpenSSL | Library | Comprehensive cryptographic toolkit for implementing hash and MAC functions |
| Python `hashlib` | Library | Built-in Python module for various hashing algorithms and HMAC |

## Retrieval Keywords
hash functions, message authentication codes, MACs, cryptography, data integrity, authentication, collision resistance, preimage resistance, second preimage resistance, HMAC, CMAC, GMAC, cryptographic primitives, digital signatures, key derivation functions, KDFs, password hashing, secure communication, cryptographic algorithms, message digest, one-way function, keyed hash, integrity verification, authenticity, security protocols

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Digital_Signatures (related mechanism)
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Key_Management (foundational concept)
- → Tech_Knowledge_System/Networking/Network_Security_Protocols (protocol integration)

## Fast Queries This Node Should Answer
- "What is the difference between a hash function and a MAC?"
- "How do hash functions ensure data integrity?"
- "When should I use HMAC instead of a simple hash?"
- "What are the main tools for implementing hash functions and MACs?"
- "What are common failure modes for hash functions and MACs?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations