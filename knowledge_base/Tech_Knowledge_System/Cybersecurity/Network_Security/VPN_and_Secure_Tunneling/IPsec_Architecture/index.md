# IPsec Architecture

**Path:** Tech_Knowledge_System/Cybersecurity/Network_Security/VPN_and_Secure_Tunneling/IPsec_Architecture
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
IPsec Architecture is a suite of protocols that provides cryptographic security services at the Internet Protocol (IP) layer. It ensures data confidentiality, integrity, and authenticity for IP communications, forming the backbone for secure network connections like Virtual Private Networks (VPNs).

## Key Concepts
- Authentication Header (AH) → Provides data integrity and authentication for IP packets.
- Encapsulating Security Payload (ESP) → Offers confidentiality, integrity, and authentication for IP packet payloads.
- Internet Key Exchange (IKE) → Establishes and manages Security Associations (SAs) between IPsec peers.
- Security Association (SA) → A logical connection defining security parameters and keys for IPsec protocols.
- Security Policy Database (SPD) → A database that dictates how IP traffic should be protected by IPsec.
- Security Association Database (SAD) → Stores the operational parameters for active Security Associations.
- Tunnel Mode → Encrypts and authenticates the entire original IP packet.
- Transport Mode → Encrypts and authenticates only the payload of the IP packet.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| strongSwan | Implementation | Open-source IPsec-based VPN solution |
| Libreswan | Implementation | Free software implementation of IPsec for Linux |
| OpenSwan | Implementation | Fork of FreeS/WAN, providing IPsec for Linux |
| IKEv2 | Protocol | Modern key exchange protocol for IPsec, offering improved efficiency and resilience |
| AES | Algorithm | Symmetric encryption standard used for data confidentiality in ESP |
| SHA-2 | Algorithm | Hashing algorithm used for data integrity and authentication in AH and ESP |

## Retrieval Keywords
IPsec, Internet Protocol Security, VPN, network security, secure tunneling, cryptography, AH, ESP, IKE, Security Association, SPD, SAD, tunnel mode, transport mode, data integrity, confidentiality, authentication, secure communication, IPsec VPN, network layer security, strongSwan, Libreswan, IKEv2, AES, SHA-2

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Network_Security/VPN_and_Secure_Tunneling (parent)
- → Tech_Knowledge_System/Cybersecurity/Network_Security/Encryption_Protocols (related)
- → Tech_Knowledge_System/Cybersecurity/Network_Security/Authentication_Methods (related)

## Fast Queries This Node Should Answer
- "What is IPsec Architecture?"
- "How does IPsec work to secure network communication?"
- "When should I use IPsec for network security?"
- "What are the main components of IPsec?"
- "What are common vulnerabilities in IPsec implementations?"
- "What is the difference between IPsec tunnel mode and transport mode?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations