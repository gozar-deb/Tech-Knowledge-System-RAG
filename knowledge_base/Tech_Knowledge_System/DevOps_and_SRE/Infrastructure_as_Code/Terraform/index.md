# Terraform

**Path:** Tech_Knowledge_System/DevOps_and_SRE/Infrastructure_as_Code/Terraform
**Difficulty:** Intermediate
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Terraform is an Infrastructure as Code (IaC) tool that allows you to define and provision cloud and on-premises resources using a declarative configuration language. It supports multi-cloud environments, enabling consistent infrastructure deployment and management across various platforms.

## Key Concepts
- Infrastructure as Code (IaC) → Managing infrastructure through machine-readable definition files.
- Declarative Configuration → Specifying the desired state of infrastructure, not the steps to achieve it.
- Providers → Plugins that interact with APIs of cloud platforms or other services.
- State File → A record of the infrastructure managed by Terraform, mapping configuration to real resources.
- Modules → Reusable, parameterized Terraform configurations for abstraction.
- HCL (HashiCorp Configuration Language) → The primary language for writing Terraform configurations.
- Resource Graph → Terraform's internal representation of dependencies between resources.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Terraform CLI | Command-line Interface | Core tool for planning, applying, and destroying infrastructure. |
| Terraform Cloud/Enterprise | Platform | Remote state management, collaboration, policy enforcement, and run automation. |
| Terragrunt | Wrapper | Provides extra tools for keeping Terraform configurations DRY (Don't Repeat Yourself). |
| Atlantis | Automation | Integrates Terraform into Git workflows for pull request automation. |

## Retrieval Keywords
Terraform, IaC, Infrastructure as Code, HashiCorp, HCL, declarative, provisioning, automation, multi-cloud, cloud infrastructure, AWS, Azure, GCP, Kubernetes, state management, modules, providers, DevOps, SRE, infrastructure orchestration, immutable infrastructure, configuration management, resource lifecycle

## Related Nodes
- → Tech_Knowledge_System/DevOps_and_SRE/Infrastructure_as_Code (Parent Node)
- → Tech_Knowledge_System/DevOps_and_SRE/Continuous_Integration_and_Delivery (Related Concept: Automation)
- → Tech_Knowledge_System/Cloud_Computing/AWS (Example Cloud Provider)

## Fast Queries This Node Should Answer
- "What is Terraform and how does it work?"
- "How does Terraform manage infrastructure state?"
- "When should I use Terraform versus other IaC tools?"
- "What are the main tools for managing Terraform deployments?"
- "What are common failures in Terraform deployments and how to prevent them?"
- "How can Terraform be used for multi-cloud deployments?"
- "What are the security best practices for Terraform configurations?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations