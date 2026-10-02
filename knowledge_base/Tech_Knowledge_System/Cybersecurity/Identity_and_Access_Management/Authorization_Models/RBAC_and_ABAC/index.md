# RBAC and ABAC

**Path:** Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management/Authorization_Models/RBAC_and_ABAC
**Difficulty:** Intermediate
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Role-Based Access Control (RBAC) manages permissions by assigning users to specific roles, each with predefined access rights. Attribute-Based Access Control (ABAC) provides more dynamic and fine-grained authorization by evaluating attributes of the user, resource, action, and environment against defined policies.

## Key Concepts
- RBAC → Access based on user's organizational role.
- ABAC → Access based on dynamic evaluation of attributes.
- Role → A collection of permissions.
- Attribute → A characteristic (e.g., user department, resource sensitivity).
- Policy → Rules defining access decisions in ABAC.
- Least Privilege → Granting only necessary permissions.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Open Policy Agent (OPA) | Policy Engine | Evaluates ABAC policies across various systems. |
| AWS IAM | Cloud Service | Provides both RBAC and ABAC capabilities for AWS resources. |
| XACML | Standard | XML-based language for expressing access control policies. |
| LDAP | Directory Service | Stores and manages user and attribute information. |

## Retrieval Keywords
RBAC, ABAC, Role-Based Access Control, Attribute-Based Access Control, authorization, access control, identity management, cybersecurity, permissions, roles, attributes, policies, security models, fine-grained access, enterprise security, cloud security, microservices security, IAM, policy engine, access management strategies, dynamic authorization.

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management (Parent Domain)
- → Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management/Authorization_Models (Parent Category)
- → Tech_Knowledge_System/Cybersecurity/Identity_and_Access_Management/Authentication (Related Concept)

## Fast Queries This Node Should Answer
- "What is the difference between RBAC and ABAC?"
- "How does RBAC work?"
- "When should I use ABAC instead of RBAC?"
- "What are the main tools for implementing ABAC?"
- "What are common security risks in RBAC and ABAC implementations?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations