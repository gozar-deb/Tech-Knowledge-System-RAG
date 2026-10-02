# Reentrancy and Flash Loan Attacks

**Path:** Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Blockchain_Security/Reentrancy_and_Flash_Loan_Attacks
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Reentrancy attacks exploit a smart contract's logic by repeatedly calling a function before its state is updated. Flash loan attacks leverage uncollateralized loans, borrowed and repaid within a single transaction, to manipulate market conditions or exploit vulnerabilities in decentralized finance (DeFi) protocols.

## Key Concepts
- Reentrancy → Vulnerability allowing repeated function calls before state update.
- Flash Loan → Uncollateralized loan executed and repaid within one blockchain transaction.
- External Call → Interaction between smart contracts or with external addresses.
- State Variables → Data stored on the blockchain within a smart contract.
- The DAO Hack → Historic reentrancy exploit on Ethereum.
- Oracle Manipulation → Falsifying price feeds to trigger unfair liquidations or arbitrage.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Solidity | Language | Smart contract development |
| Hardhat | Framework | Ethereum development environment |
| Slither | Analyzer | Static analysis for smart contract vulnerabilities |
| Mythril | Analyzer | Security analysis for EVM bytecode |

## Retrieval Keywords
reentrancy, flash loan, blockchain security, smart contract vulnerability, DeFi exploit, Ethereum, DAO hack, economic attack, external calls, Solidity, EVM, security audit, price oracle, liquidity pool, decentralized finance, attack vector, smart contract best practices, vulnerability assessment

## Related Nodes
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Blockchain_Security (parent)
- → Tech_Knowledge_System/Blockchain_and_Distributed_Ledger/Smart_Contracts (related)

## Fast Queries This Node Should Answer
- "What is a reentrancy attack?"
- "How does a flash loan attack work?"
- "When should I use reentrancy guards?"
- "What are the main tools for smart contract security analysis?"
- "What are common failures in DeFi protocols due to flash loans?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations