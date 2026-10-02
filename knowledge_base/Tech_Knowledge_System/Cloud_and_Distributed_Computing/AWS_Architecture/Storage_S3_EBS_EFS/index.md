# Storage S3 EBS EFS

**Path:** Tech_Knowledge_System/Cloud_and_Distributed_Computing/AWS_Architecture/Storage_S3_EBS_EFS
**Difficulty:** Intermediate
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
AWS Storage services (S3, EBS, EFS) offer distinct cloud-native solutions for data persistence. S3 provides scalable object storage for unstructured data, EBS delivers high-performance block storage for EC2 instances, and EFS offers shared, elastic file storage, each tailored for specific application needs and access patterns.

## Key Concepts
- Amazon S3 → Highly scalable, durable, and available object storage for diverse data types.
- Amazon EBS → Persistent block storage volumes for EC2 instances, optimized for transactional workloads.
- Amazon EFS → Scalable, shared file storage for EC2 and on-premises, supporting NFSv4 protocol.
- Storage Classes → Cost-optimization tiers within S3 based on data access frequency and retrieval needs.
- Durability → The long-term preservation of data, often expressed in terms of nines (e.g., 99.999999999%).
- Availability → The uptime and accessibility of the storage service.
- Lifecycle Policies → Automated rules for transitioning S3 objects between storage classes or expiring them.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Amazon S3 | Object Storage | Scalable, durable storage for unstructured data |
| Amazon EBS | Block Storage | High-performance, persistent block storage for EC2 |
| Amazon EFS | File Storage | Shared, elastic file system for cloud and on-premises |
| AWS CLI | Command Line Interface | Manage AWS services from the command line |
| AWS SDKs | Development Kits | Programmatic access to AWS services from various languages |

## Retrieval Keywords
AWS storage, S3, EBS, EFS, cloud storage, object storage, block storage, file storage, distributed storage, data persistence, scalability, availability, durability, performance, cost optimization, cloud architecture, data lakes, backups, archives, EC2 storage, shared file systems, NFS, storage classes, lifecycle policies, encryption, access control, disaster recovery

## Related Nodes
- → Tech_Knowledge_System/Cloud_and_Distributed_Computing/AWS_Architecture (parent)
- → Tech_Knowledge_System/Cloud_and_Distributed_Computing/AWS_Architecture/Compute_EC2_Lambda_ECS (sibling)
- → Tech_Knowledge_System/Data_Management/Data_Lakes_and_Warehouses (related)
- → Tech_Knowledge_System/DevOps/CI_CD_Pipelines (related)

## Fast Queries This Node Should Answer
- "What are the differences between AWS S3, EBS, and EFS?"
- "When should I use S3 versus EBS or EFS?"
- "How do I optimize costs for AWS storage services?"
- "What are common security best practices for S3 buckets?"
- "How can I ensure high availability and durability for data on AWS?"
- "What are the performance considerations for EBS volumes?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations