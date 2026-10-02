# Injection Attacks

**Path:** Tech_Knowledge_System/Cybersecurity/Application_Security/OWASP_Top_10/Injection_Attacks
**Difficulty:** Advanced
**Time to Learn:** 3-6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Injection attacks are a class of vulnerabilities where an attacker can supply untrusted input that is then interpreted as part of a command or query by an application. This allows the attacker to execute arbitrary commands, access unauthorized data, or manipulate application logic.

## Key Concepts
- SQL Injection → Manipulating database queries through malicious input.
- Command Injection → Executing operating system commands via application input.
- XSS (Cross-Site Scripting) → Injecting client-side scripts into web pages.
- LDAP Injection → Exploiting applications that build LDAP queries from user input.
- XXE Injection → Attacking XML parsers by referencing external entities.
- Parameterized Queries → A secure method to separate code from data in database interactions.
- Input Validation → Verifying that user-supplied data conforms to expected formats and safety rules.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| OWASP ZAP | DAST | Automated vulnerability scanner for web applications |
| Burp Suite | Proxy/DAST | Intercepting proxy for manual and automated security testing |
| SQLMap | Exploitation | Automated SQL injection and database takeover tool |
| WAF (Web Application Firewall) | Network Security | Filters and monitors HTTP traffic between a web application and the Internet |
| ORMs (e.g., SQLAlchemy, Hibernate) | Framework | Object-Relational Mappers that inherently prevent SQL injection |
| ESLint Security Plugin | SAST | Static analysis for JavaScript code to find security vulnerabilities |

## Retrieval Keywords
injection, SQL injection, command injection, XSS, XXE, LDAP injection, NoSQL injection, code injection, OS command injection, data injection, web security, application security, OWASP Top 10, vulnerability, exploit, prevention, mitigation, input validation, parameterized queries, stored procedures, least privilege, context separation, secure coding, DAST, SAST, WAF

## Related Nodes
- → Tech_Knowledge_System/Cybersecurity/Application_Security/OWASP_Top_10 (parent)
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Input_Validation (related)
- → Tech_Knowledge_System/Cybersecurity/Application_Security/Secure_Coding_Practices (related)

## Fast Queries This Node Should Answer
- "What is an injection attack?"
- "How does SQL injection work?"
- "When should I use parameterized queries?"
- "What are the main tools for preventing injection attacks?"
- "What are common failure modes in injection vulnerabilities?"
- "How can I prevent command injection?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations