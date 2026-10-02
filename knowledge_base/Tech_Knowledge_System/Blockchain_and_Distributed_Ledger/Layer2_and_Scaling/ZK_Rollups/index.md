# ZK Rollups

**Path:** Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Layer2_and_Scaling/ZK_Rollups
**Difficulty:** Advanced
**Time to Learn:** 3–6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
ZK-Rollups are a type of Layer 2 scaling solution for blockchains that aggregate numerous off-chain transactions into a single batch. They use zero-knowledge proofs to cryptographically guarantee the validity of these transactions, enabling high throughput and reduced costs while maintaining the security of the underlying Layer 1 chain.

## Key Concepts
- Zero-Knowledge Proofs (ZKPs) → Cryptographic proofs verifying transaction validity without revealing details.
- Rollup → A Layer 2 technique bundling off-chain transactions for on-chain submission.
- Validity Proofs → Cryptographic assurances (e.g., SNARKs, STARKs) of correct state transitions.
- Sequencer → An entity that collects, orders, and batches off-chain transactions.
- Data Availability → Guarantee that all rollup transaction data is publicly accessible.
- State Root → A cryptographic commitment to the rollup's state on the Layer 1 chain.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| StarkNet | Infrastructure | General-purpose ZK-Rollup platform |
| zkSync | Infrastructure | EVM-compatible ZK-Rollup for scaling Ethereum |
| Polygon zkEVM | Infrastructure | ZK-Rollup providing EVM equivalence |
| Loopring | Real-World Use | DEX built on ZK-Rollup technology |

## Retrieval Keywords
ZK-Rollups, Zero-Knowledge Proofs, Layer 2 scaling, blockchain scalability, Ethereum scaling, transaction throughput, validity proofs, off-chain computation, state storage, cryptographic proofs, SNARKs, STARKs, rollup technology, decentralized applications, smart contracts, ZK-EVM, recursive ZKPs, StarkNet, zkSync, Polygon zkEVM, Loopring, dYdX

## Related Nodes
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Layer2_and_Scaling (parent)
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Layer2_and_Scaling/Optimistic_Rollups (sibling)
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Cryptography/Zero_Knowledge_Proofs (foundational)

## Fast Queries This Node Should Answer
- "What is a ZK-Rollup?"
- "How do ZK-Rollups work?"
- "When should I use ZK-Rollups?"
- "What are the main tools for ZK-Rollups?"
- "What are common failures in ZK-Rollup systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations