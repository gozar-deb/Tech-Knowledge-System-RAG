# HMAC and Poly1305

**Path:** Tech_Knowledge_System/Cybersecurity/Cryptography/Hash_Functions_and_MACs/HMAC_and_Poly1305
**Difficulty:** Intermediate
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
HMAC (Hash-based Message Authentication Code) and Poly1305 are cryptographic message authentication codes (MACs) used to verify data integrity and authenticity. HMAC combines a cryptographic hash function with a secret key, while Poly1305 is a fast, one-time MAC designed for high-performance applications, often paired with stream ciphers like ChaCha20.

## Key Concepts
- HMAC → A MAC constructed using a cryptographic hash function and a secret key.
- Poly1305 → A high-speed, one-time message authentication code.
- Message Authentication Code (MAC) → A small piece of information used to authenticate a message.
- Data Integrity → Assurance that data has not been altered during transit or storage.
- Data Authenticity → Assurance that data originates from a trusted source.
- Secret Key → A cryptographic key known only to authorized parties, used for encryption and authentication.
- Cryptographic Hash Function → A one-way function that produces a fixed-size output (hash) from variable-size input.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| OpenSSL | Library | Provides implementations of HMAC and Poly1305. |
| libsodium | Library | A modern, easy-to-use cryptographic library including Poly1305. |
| Go crypto/hmac | Library | Standard library for HMAC in Go. |
| Python hmac module | Library | Built-in module for HMAC in Python. |

## Retrieval Keywords
HMAC, Poly1305, Message Authentication Code, MAC, data integrity, data authenticity, cryptographic hash, secret key, keyed hash, authentication, cryptography, cybersecurity, ChaCha20-Poly1305, SHA-256, SHA-512, RIPEMD-160, one-time authenticator, keyed-hash message authentication code, digital signatures.

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Hash_Functions_and_MACs (Parent Node)
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Symmetric_Key_Cryptography/ChaCha20 (Related Cipher)

## Fast Queries This Node Should Answer
- "What is HMAC?"
- "How does Poly1305 work?"
- "When should I use HMAC vs Poly1305?"
- "What are the main tools for HMAC and Poly1305?"
- "What are common failures in HMAC and Poly1305 implementations?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations