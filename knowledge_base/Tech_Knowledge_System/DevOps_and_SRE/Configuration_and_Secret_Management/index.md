# Configuration and Secret Management

**Path:** Tech_Knowledge_System/DevOps_and_SRE/Configuration_and_Secret_Management
**Difficulty:** Advanced
**Time to Learn:** 3–6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Configuration management systematically defines and maintains the operational state of systems and applications. Secret management focuses on the secure handling, storage, and access of sensitive credentials and data. Both are foundational for automated, secure, and scalable infrastructure.

## Key Concepts
- Desired State Configuration → Declaratively defines the target state of a system, automatically enforcing it.
- Idempotence → Ensures that applying a configuration multiple times yields the same result without side effects.
- State Drift → Unintended deviations of a system's actual configuration from its defined desired state.
- Vaulting → Centralized, encrypted storage and access control for sensitive information like API keys.
- Least Privilege → A security principle dictating that users and systems should only have access to resources absolutely necessary for their function.
- Secret Rotation → Periodically changing secrets to reduce the window of exposure if a secret is compromised.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Ansible | Configuration Management | Automates software provisioning, configuration management, and application deployment. |
| Terraform | Infrastructure as Code | Defines and provisions infrastructure using declarative configuration files. |
| HashiCorp Vault | Secret Management | Securely stores, tightly controls access to, and audits secrets. |
| Kubernetes ConfigMaps/Secrets | Orchestration | Manages configuration data and sensitive information for containerized applications. |

## Retrieval Keywords
Configuration management, secret management, desired state, state drift, infrastructure as code, IaC, Ansible, Terraform, HashiCorp Vault, Kubernetes secrets, environment variables, credential security, access control, policy as code, compliance, audit, security best practices, DevOps, SRE, immutable infrastructure, dynamic secrets, secret rotation, key management.

## Related Nodes
- → Tech_Knowledge_System/DevOps_and_SRE/Infrastructure_as_Code (foundational_dependency)
- → Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management (related_domain)
- → Tech_Knowledge_System/DevOps_and_SRE/CI_CD_Pipelines (integration_point)

## Fast Queries This Node Should Answer
- "What is configuration management?"
- "How does secret management work?"
- "When should I use Ansible vs Terraform for configuration?"
- "What are the main tools for secret management?"
- "What are common failures in configuration and secret management?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations