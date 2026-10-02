# Kubernetes RBAC

**Path:** Tech_Knowledge_System/Cybersecurity/Cloud_Security/Serverless_and_Container_Security/Kubernetes_RBAC
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Kubernetes Role-Based Access Control (RBAC) is a security mechanism that regulates access to Kubernetes cluster resources. It allows administrators to define granular permissions based on user roles, ensuring secure and controlled interaction with the cluster API.

## Key Concepts
- Role → Defines permissions within a specific namespace.
- ClusterRole → Defines permissions across the entire cluster.
- RoleBinding → Grants a Role\'s permissions to subjects within a namespace.
- ClusterRoleBinding → Grants a ClusterRole\'s permissions to subjects cluster-wide.
- Subjects → Users, groups, or service accounts granted permissions.
- API Groups → Logical groupings of Kubernetes API resources.
- Verbs → Actions (e.g., get, create, delete) permitted on resources.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| kubectl | CLI | Manage RBAC objects (Roles, RoleBindings) |
| kube-apiserver | Infrastructure | Enforces RBAC policies |
| YAML | Language | Define RBAC configurations |
| Kubernetes API | Framework | Programmatic access for policy management |

## Retrieval Keywords
Kubernetes RBAC, Role-Based Access Control, cluster security, authorization, access management, roles, clusterroles, rolebindings, clusterrolebindings, subjects, permissions, API groups, resources, verbs, security policies, least privilege, Kubernetes API, kubectl, serverless security, container security

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Cloud_Security/Serverless_and_Container_Security (parent)
- → Tech_Knowledge_System/Cybersecurity/Cloud_Security/Serverless_and_Container_Security/Kubernetes_Security (sibling)
- → Tech_Knowledge_System/Cybersecurity/Network_Security/Authentication_and_Authorization (authorization mechanism)
- → Tech_Knowledge_System/Cybersecurity/Cloud_Security/Container_Security/Pod_Security_Policies (complementary security control)

## Fast Queries This Node Should Answer
- "What is Kubernetes RBAC?"
- "How does Kubernetes RBAC work?"
- "When should I use Kubernetes RBAC?"
- "What are the main components of Kubernetes RBAC?"
- "What are common failures in Kubernetes RBAC configurations?"
- "How do I configure a Role in Kubernetes RBAC?"
- "What is the difference between a Role and a ClusterRole?"
- "How do RoleBindings and ClusterRoleBindings function?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations