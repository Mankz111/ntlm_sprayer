# NTLM Sprayer

Python utility for **Password Spraying** attacks against NTLM authentication. Designed for security auditing and Active Directory laboratory environments.

## Demo Results
<p align="center">
  <img src="assets/ntlm.png" width="650" alt="Attack Results">
</p>

<p align="center">
  <img src="assets/results.png" width="650" alt="Attack Results">
</p>

## Features
* **Summary Report**: Consolidates all valid credentials at the end of the attack.
* **OOP Design**: Built using Object-Oriented Programming for modularity.
* **CLI Focused**: Native terminal experience using `argparse`.

## Usage
```bash
python ntlm_sprayer.py -w users.txt -p Password123 -u [http://target.local/login](http://target.local/login) -f domain.local
```

## 1. The Identity Problem (FQDN)

In a standard Active Directory (AD) environment, a standalone username such as `georgina.edwards` is often insufficient for authentication. The system must determine which authority manages that account. This is where the Fully Qualified Domain Name (FQDN) becomes essential.

Authentication protocols such as NTLM require credentials in the following format:

## 2. Defeating Account Lockout Policies

Traditional brute-force attacks — testing multiple passwords against a single user — are high-risk in modern Active Directory environments.

Most AD configurations enforce **Account Lockout Policies**, which disable an account after a defined number of failed login attempts (commonly 3–5). This not only prevents further attempts but may also trigger security alerts for the Blue Team (SOC).

### Password Spraying Strategy

Password spraying is a strategic alternative designed to bypass this limitation.

Instead of testing multiple passwords against one account, the technique tests a single commonly used password (e.g., `Summer2026!`) against a large list of users.

### Advantages

- **Single Attempt per Account**  
  Each account receives only one authentication attempt per cycle, remaining below lockout thresholds.

- **Stealth**  
  Reduces the likelihood of triggering account lockouts or detection mechanisms.

- **Efficiency**  
  Increases the probability of identifying users who rely on weak, seasonal, or predictable passwords.

---

> ⚠️ This tool is intended for authorized security testing and educational purposes only.


