# SAST and DAST

**Path:** Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_SDLC/SAST_and_DAST
**Difficulty:** Intermediate
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
SAST (Static Application Security Testing) analyzes source code for vulnerabilities without execution, while DAST (Dynamic Application Security Testing) tests running applications for security flaws. They represent white-box and black-box testing approaches, respectively, and are essential for a comprehensive application security strategy within the SDLC.

## Key Concepts
- SAST → Scans static code for vulnerabilities early in the development lifecycle.
- DAST → Tests running applications for vulnerabilities in a dynamic, operational environment.
- White-box testing → SAST's approach, requiring access to source code.
- Black-box testing → DAST's approach, simulating an external attacker without code access.
- Shift-Left → The practice of integrating security testing earlier in the software development process.
- False Positives → Erroneous vulnerability reports, more common with SAST.
- Runtime vulnerabilities → Flaws detectable only when an application is executing, typically found by DAST.
- CI/CD Integration → Automating SAST and DAST scans within continuous integration/continuous delivery pipelines.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| SonarQube | SAST | Static code analysis for quality and security |
| Checkmarx | SAST | Comprehensive static analysis for various languages |
| OWASP ZAP | DAST | Open-source web application security scanner |
| Burp Suite | DAST | Industry-standard tool for web penetration testing |
| Fortify | SAST | Enterprise-grade static code analysis platform |
| Acunetix | DAST | Automated web vulnerability scanner |

## Retrieval Keywords
SAST, DAST, Static Application Security Testing, Dynamic Application Security Testing, application security, secure SDLC, vulnerability scanning, code analysis, runtime analysis, security testing, DevSecOps, white-box testing, black-box testing, security automation, software development security, CI/CD security, application vulnerabilities, web security, API security, security tools, code quality, penetration testing, security audit, software assurance, vulnerability management, security posture, risk mitigation, secure coding, application hardening

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_SDLC (parent)
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_SDLC/Threat_Modeling (related)
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_SDLC/SCA (related)
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_SDLC/DevSecOps (cross-domain)
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_SDLC/IAST (complementary)

## Fast Queries This Node Should Answer
- "What is SAST and DAST?"
- "How do SAST and DAST differ?"
- "When should I use SAST vs DAST?"
- "What are the main tools for SAST and DAST?"
- "What are common failures in SAST and DAST implementation?"
- "How do SAST and DAST fit into a secure SDLC?"
- "What are the security implications of using SAST and DAST?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations