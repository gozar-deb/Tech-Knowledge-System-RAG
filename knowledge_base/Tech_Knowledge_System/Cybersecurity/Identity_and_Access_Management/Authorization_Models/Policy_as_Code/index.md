# Policy as Code

**Path:** Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management/Authorization_Models/Policy_as_Code
**Difficulty:** Advanced
**Time to Learn:** 2–4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Policy as Code (PaC) is an approach to managing authorization policies using declarative, machine-readable languages, enabling automation, version control, and consistent enforcement across diverse IT environments. It shifts policy definition out of application code into a centralized, auditable system.

## Key Concepts
- Declarative Policy Language → Defines *what* is allowed, not *how* to enforce it.
- Policy Enforcement Point (PEP) → Intercepts access requests and consults the PDP.
- Policy Decision Point (PDP) → Evaluates policies to make an authorization decision.
- Policy Information Point (PIP) → Provides attributes necessary for policy evaluation.
- Version Control → Policies are managed like code, with history, review, and rollback.
- Automated Deployment → Policies are deployed via CI/CD pipelines for consistency.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Open Policy Agent (OPA) | Policy Engine | General-purpose policy engine for cloud-native environments |
| Rego | Policy Language | Declarative language used by OPA for policy definition |
| AWS Verified Permissions | Service | Fine-grained authorization service using Cedar policy language |
| Google Cloud IAM | Service | Manages access to Google Cloud resources with policy-based controls |

## Retrieval Keywords
Policy as Code, PaC, authorization, access control, declarative policies, OPA, Rego, Cedar, AWS Verified Permissions, Google Cloud IAM, security automation, compliance, governance, access management, fine-grained authorization, attribute-based access control, RBAC, ABAC, policy enforcement, security policy, cloud security, microservices security, zero trust, infrastructure as code, security architecture, policy engine, PDP, PEP, PIP, GitOps for security

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management/Authorization_Models (parent_concept)
- → Tech_Knowledge_System/Cybersecurity/Cloud_Security/Infrastructure_as_Code (related_concept)
- → Tech_Knowledge_System/Cybersecurity/Compliance_and_Governance (related_domain)
- → Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management/Zero_Trust_Architecture (foundational_component)

## Fast Queries This Node Should Answer
- "What is Policy as Code?"
- "How does Policy as Code work?"
- "When should I use Policy as Code?"
- "What are the main tools for Policy as Code?"
- "What are common failures in Policy as Code?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations