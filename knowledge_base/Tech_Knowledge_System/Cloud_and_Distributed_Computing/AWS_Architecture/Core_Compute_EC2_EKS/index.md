# Core Compute EC2 EKS

**Path:** Tech_Knowledge_System/Cloud_and_Distributed_Computing/AWS_Architecture/Core_Compute_EC2_EKS
**Difficulty:** Advanced
**Time to Learn:** 3-6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
AWS EC2 provides virtual servers for scalable compute capacity, while AWS EKS offers a managed Kubernetes service for deploying and managing containerized applications. Together, they form the backbone for flexible and powerful cloud-native compute solutions, enabling high availability and scalability for diverse workloads.

## Key Concepts
- EC2 Instances → Virtual servers providing on-demand compute.
- Amazon Machine Images (AMIs) → Templates for launching pre-configured EC2 instances.
- Security Groups → Virtual firewalls controlling instance traffic.
- Kubernetes Pods → Smallest deployable unit in Kubernetes, runs containers.
- Kubernetes Deployments → Manages declarative updates and scaling of Pods.
- EKS Control Plane → AWS-managed Kubernetes master components.
- Worker Nodes → EC2 instances running application containers in EKS.
- Auto Scaling Groups → Dynamically adjusts EC2 instance count based on load.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| AWS EC2 | Infrastructure | Provides virtual servers |
| AWS EKS | Infrastructure | Managed Kubernetes service |
| Docker | Containerization | Packages applications into containers |
| Kubernetes | Orchestration | Automates deployment, scaling, and management of containerized applications |
| Terraform | IaC | Defines and provisions cloud infrastructure |
| Helm | Package Manager | Manages Kubernetes applications |

## Retrieval Keywords
AWS, EC2, EKS, Kubernetes, compute, cloud, containers, virtual machines, orchestration, scalability, elasticity, microservices, infrastructure, serverless, auto-scaling, instances, pods, deployments, control plane, worker nodes, security groups, AMIs, Fargate, Spot Instances, GitOps, service mesh

## Related Nodes
- → Tech_Knowledge_System/Cloud_and_Distributed_Computing/AWS_Architecture (parent)

## Fast Queries This Node Should Answer
- "What is AWS EC2 and EKS?"
- "How does EKS leverage EC2?"
- "When should I use EC2 versus EKS?"
- "What are the main tools for managing EC2 and EKS?"
- "What are common failures in EC2 and EKS deployments?"
- "How can I optimize costs for EC2 and EKS?"
- "What are the security best practices for EC2 and EKS?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations