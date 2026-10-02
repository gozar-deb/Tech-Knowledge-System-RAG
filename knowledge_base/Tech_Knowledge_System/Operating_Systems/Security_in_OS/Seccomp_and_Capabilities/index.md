# Seccomp and Capabilities

**Path:** Tech_Knowledge_System/Operating_Systems/Security_in_OS/Seccomp_and_Capabilities
**Difficulty:** Advanced
**Time to Learn:** 1–2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Seccomp (Secure Computing Mode) is a Linux kernel feature that restricts the system calls a process can invoke, thereby reducing its attack surface. Linux Capabilities provide a granular way to assign specific root-like privileges to processes without granting full superuser access, enhancing the principle of least privilege.

## Key Concepts
- Seccomp → Filters and restricts system calls a process can make.
- Capabilities → Granular permissions allowing non-root processes specific privileged operations.
- Syscall Filtering → The process of controlling which system calls are permitted for an application.
- BPF → Kernel-level virtual machine used to define Seccomp's complex filtering rules.
- Least Privilege → Security principle of granting only necessary permissions to a process.
- Container Hardening → Using Seccomp and Capabilities to secure containerized applications.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| libseccomp | Library | Simplifies Seccomp profile creation and management |
| Docker | Container Platform | Utilizes Seccomp and Capabilities for container isolation |
| Kubernetes | Orchestration | Manages Seccomp profiles and capabilities for deployed workloads |
| `setcap`/`getcap` | Utility | Command-line tools for managing file capabilities |

## Retrieval Keywords
Seccomp, Capabilities, Linux security, syscall filtering, BPF, container security, privilege management, process isolation, kernel hardening, security profiles, sandboxing, attack surface reduction, `CAP_NET_ADMIN`, `CAP_SYS_ADMIN`, `libseccomp`, Docker security, Kubernetes security

## Related Nodes
- → Tech_Knowledge_System/Operating_Systems/Security_in_OS/Linux_Security_Modules (complements)
- → Tech_Knowledge_System/Operating_Systems/Security_in_OS/Container_Security (applied_in)
- → Tech_Knowledge_System/Operating_Systems/Kernel_Internals/System_Calls (fundamental_to)

## Fast Queries This Node Should Answer
- "What is Seccomp and how does it work?"
- "What are Linux Capabilities and why are they used?"
- "When should I use Seccomp or Capabilities for application security?"
- "What are the main tools for managing Seccomp profiles and Capabilities?"
- "What are common failure modes when configuring Seccomp or Capabilities?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations