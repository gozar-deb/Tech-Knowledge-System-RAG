# Asymmetric Cryptography

**Path:** Tech_Knowledge_System/Cybersecurity/Cryptography/Asymmetric_Cryptography
**Difficulty:** Advanced
**Time to Learn:** 2–4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Asymmetric cryptography, or public-key cryptography, uses distinct public and private keys for encryption/decryption and digital signatures. It enables secure communication, authentication, and non-repudiation over insecure channels, forming the backbone of modern internet security protocols like TLS.

## Key Concepts
- Public Key → Key freely shared for encryption and signature verification.
- Private Key → Secret key used for decryption and digital signing.
- Digital Signature → Verifies message authenticity and integrity using a private key.
- Key Exchange → Method to securely establish a shared secret over an insecure medium.
- RSA → Widely used algorithm for encryption and digital signatures.
- ECC (Elliptic Curve Cryptography) → Efficient alternative to RSA, offering strong security with smaller keys.
- PKI (Public Key Infrastructure) → System for managing digital certificates and public keys.
- Non-repudiation → Guarantees a sender cannot deny having sent a message.
- Trapdoor Function → One-way function with a secret shortcut for easy reversal.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| RSA | Algorithm | Encryption, digital signatures, key exchange |
| ECC | Algorithm | Efficient encryption, digital signatures |
| OpenSSL | Library | Cryptographic functions, TLS/SSL implementation |
| GnuPG | Software | Email encryption, digital signing (PGP) |
| Diffie-Hellman | Algorithm | Secure key exchange over insecure channels |
| X.509 | Standard | Defines format for public key certificates |

## Retrieval Keywords
asymmetric cryptography, public-key, private key, encryption, decryption, digital signature, key exchange, RSA, ECC, Diffie-Hellman, ElGamal, DSA, PKI, TLS, SSL, HTTPS, PGP, S/MIME, authentication, non-repudiation, confidentiality, integrity, cryptographic algorithms, key management, quantum resistance, zero-knowledge proofs, elliptic curves, prime numbers, modular arithmetic, trapdoor functions, certificate authority, secure communication, network security, cybersecurity, cryptography standards, FIPS, PKCS

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Cryptography/Symmetric_Cryptography (contrast)
- → Tech_Knowledge_System/Cybersecurity/Network_Security/TLS_SSL (application)
- → Tech_Knowledge_System/Cybersecurity/Authentication/PKI (foundation)
- → Tech_Knowledge_System/Blockchain/Cryptocurrencies (application)

## Fast Queries This Node Should Answer
- "What is asymmetric cryptography?"
- "How does public-key encryption work?"
- "When should I use RSA vs. ECC?"
- "What are the main tools for asymmetric cryptography?"
- "What are common failures in asymmetric key management?"
- "How does asymmetric cryptography enable digital signatures?"
- "What are the security implications of public-key systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations