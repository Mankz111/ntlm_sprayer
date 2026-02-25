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
