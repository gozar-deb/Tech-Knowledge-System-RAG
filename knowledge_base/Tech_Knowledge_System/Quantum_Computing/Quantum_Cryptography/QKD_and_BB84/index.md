# QKD and BB84

**Path:** Tech_Knowledge_System/Quantum_Computing/Quantum_Cryptography/QKD_and_BB84
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
The BB84 protocol is a pioneering Quantum Key Distribution (QKD) method that allows two parties to securely establish a shared secret key. It relies on the quantum properties of photons, such as polarization, to detect any attempt by an eavesdropper to intercept or measure the key, thereby ensuring its unconditional security.

## Key Concepts
- Qubits → Quantum bits, often photons, used to encode information.
- Basis States → Pairs of orthogonal polarization states (e.g., rectilinear, diagonal) for encoding and measurement.
- Random Basis Selection → Alice and Bob independently choose measurement bases to ensure security.
- Sifting → Process of publicly comparing chosen bases to identify and keep matching measurements.
- Quantum Bit Error Rate (QBER) → Metric used to detect eavesdropping by quantifying discrepancies in shared bits.
- Privacy Amplification → Post-processing technique to distill a shorter, more secure key from a longer, partially known one.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Qiskit | Framework | Quantum circuit simulation and programming |
| Cirq | Framework | Quantum programming library for noisy intermediate-scale quantum (NISQ) computers |
| Amazon Braket | Infrastructure | Cloud-based quantum computing service for QKD simulations |
| Single-photon sources | Hardware | Generate individual photons for quantum key transmission |
| Photon detectors | Hardware | Detect incoming photons and their polarization states |

## Retrieval Keywords
BB84, QKD, Quantum Key Distribution, quantum cryptography, photon polarization, secure key exchange, eavesdropping detection, quantum communication, quantum mechanics, cryptographic protocol, quantum security, information-theoretic security, quantum bit error rate, privacy amplification, quantum channel

## Related Nodes
- → Tech_Knowledge_System/Quantum_Computing/Quantum_Cryptography (parent)

## Fast Queries This Node Should Answer
- "What is the BB84 protocol?"
- "How does QKD work using BB84?"
- "When should I use quantum key distribution?"
- "What are the main tools for implementing BB84?"
- "What are common failures in QKD systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations