# Infrastructure as Code

**Path:** Tech_Knowledge_System/DevOps_and_SRE/Infrastructure_as_Code
**Difficulty:** Intermediate
**Time to Learn:** 3-6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Infrastructure as Code (IaC) is the practice of managing and provisioning IT infrastructure using code and automation, rather than manual processes. It enables the definition, deployment, and updating of infrastructure resources through machine-readable configuration files, fostering consistency, repeatability, and version control.

## Key Concepts
- Declarative Configuration → Defines the desired end state of infrastructure.
- Idempotency → Ensures applying a configuration multiple times yields the same result.
- Version Control → Manages infrastructure definitions like application code, enabling tracking and collaboration.
- Configuration Drift → Discrepancy between actual infrastructure state and its defined IaC.
- Automation → Reduces manual effort and human error in infrastructure management.
- Immutable Infrastructure → Deploying changes by replacing existing resources rather than modifying them.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Terraform | Orchestration | Provisioning and managing infrastructure across multiple cloud providers. |
| Ansible | Configuration Management | Automating software provisioning, configuration management, and application deployment. |
| AWS CloudFormation | Orchestration | Defining and provisioning AWS infrastructure resources. |
| Pulumi | Orchestration | Using familiar programming languages to define cloud infrastructure. |

## Retrieval Keywords
Infrastructure as Code, IaC, DevOps, SRE, automation, provisioning, configuration management, declarative, imperative, Terraform, Ansible, CloudFormation, Azure Resource Manager, Google Cloud Deployment Manager, Pulumi, GitOps, desired state, idempotency, infrastructure automation, cloud infrastructure, continuous delivery, CI/CD, environment consistency, infrastructure testing, policy as code

## Related Nodes
- → Tech_Knowledge_System/DevOps_and_SRE (parent domain)
- → Tech_Knowledge_System/DevOps_and_SRE/Continuous_Integration_and_Delivery (enables automated infrastructure deployment)

## Fast Queries This Node Should Answer
- "What is Infrastructure as Code?"
- "How does IaC work?"
- "When should I use Infrastructure as Code?"
- "What are the main tools for IaC?"
- "What are common failures in IaC deployments?"
- "What is the difference between declarative and imperative IaC?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations