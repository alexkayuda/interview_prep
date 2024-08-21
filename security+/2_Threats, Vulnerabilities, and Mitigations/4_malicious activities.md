# Analyze indicators of malicious activity

<br>

## Important To Know

<br>

### Types of Physical attacks

- Brute force
  - Door busting
- Radio frequency identification (RFID) cloning
  - Example: Access Badge Cloning
- Environmental
  - Example: shut off a power grid, HVAC (Heating, Ventilation, AC) system, or fire detection systems

### Types of Malware attacks

- Viruses
  - Attach to clean files, spread, and corrupt host files
- Worms
  - Standalone programs replicating and spreading to other computers
- Trojans
  - Disguise as legitimate software, grant unauthorized access
- Ransomware
  - Encrypts user data, demands ransom for decryption
- Zombies and Botnets
  - Compromised computers remotely controlled in a network for malicious purposes
- Rootkits
  - Hide presence and activities on a computer, operate at the OS level
- Backdoors
  - Backdoors allow unauthorized access
- Keyloggers
  - Record keystrokes, capture passwords or sensitive information
- Spyware
  - Spyware monitors and gathers user/system information
- Bloatware
  - Bloatware consumes resources without value
- Logic bomb
  - Malicious code that's inserted into a program, and the malicious code will only execute when certain conditions have been met

### Types of Network attacks

- Distributed denial-of-service (DDoS) <br>
  Malicious attempt to disrupt the normal functioning of a network, service, or website by overwhelming it with a flood of internet traffic

  - Types:
    - Amplified = DNS Amplification Attack
      - Specialized DDoS that allows an attacker to initiate DNS requests from a spoof IP address to flood a website
    - Reflected

- Domain Name System (DNS) attacks <br>
  DNS is a component of the internet that is responsible for translating human-friendly domain names into IP addresses that computers can understand

  - DNS Cache Poisoning (DNS Spoofing)
    - Corrupts a DNS resolver's cache with false information
    - Redirects users to malicious websites
    - Mitigation:
      - Secure DNS servers by implementing secure network configurations and firewalls.
  - DNS Amplification Attacks
    - Overwhelms a target system with DNS response traffic by exploiting the DNS resolution process
    - Spoofed DNS queries sent to open DNS servers
    - Mitigation:
      - Limit the size and rate of DNS responses
  - DNS Tunneling
    - Encapsulates non-DNS traffic (e.g., HTTP, SSH) over port 53
    - Attempts to bypass firewall rules for command and control or data exfiltration
    - Mitigation
    - Monitor and analyze DNS logs for unusual patterns indicating tunneling
  - Domain Hijacking (Domain Theft)
    - Unauthorized change of domain registration that may lead to loss of website control and redirection to malicious sites
    - Mitigation:
      - Secure registration account information
  - DNS Zone Transfer Attacks
    - Attempts to obtain an entire DNS zone data copy
    - Exposes sensitive information about a domain's network infrastructure

- Wireless
- On-path
- Credential replay
- Malicious code

### Types of Application attacks

- Injection
- Buffer overflow
- Replay
- Privilege escalation
- Forgery
- Directory traversal

### Types of Cryptographic attacks

- Downgrade
- Collision
- Birthday

### Types of Password attacks

- Spraying
- Brute force

### Indicators of Compromise (IoC)

Pieces of forensic data that identify potentially malicious activity on a network or system. Serves as digital evidence that a security breach has occurred

- Account lockout
  - Occurs when an account is locked due to multiple failed login attempts.
  - Indicates a potential <b> brute force attack </b> to gain access
- Concurrent session usage
  - Refers to multiple active sessions from a single user account
  - Indicates a possible <b> account compromise </b> when the legitimate user is also logged in
- Blocked content
  - Involves attempts to access or download content blocked by security protocols
  - Suggests a user trying to access malicious content or an attacker attempting to <b> steal data </b>
- Impossible travel
  - Detects logins from geographically distant locations within an unreasonably short timeframe
  - Indicates a likely <b> account compromise </b> as physical travel between these locations is impossible
- Resource consumption
  - Unusual spikes in resource utilization (CPU / Memory / Network bandwidth)
  - May indicate <b> malware infections or Distributed Denial of Service (DDoS) attacks </b>
- Resource inaccessibility
  - Inability to access resources like files, databases, or network services
  - Suggests a <b> ransomware attack </b>, where files are encrypted, and a ransom is demanded
- Out-of-cycle logging
  - Log entries occurring at unusual times
  - Indicates an attacker trying to <b> hide their activities </b> during off-peak hours
- Published/documented
  - Attackers publicly disclose their actions, boasting about their skills or causing reputational damage
  - Can occur on social media, hacker forums, newspaper articles, or the victim's own website
- Missing logs
  - Sign that logs have been deleted to hide attacker activities
  - May result in <b> gaps in the log data </b>, making it harder to trace the attacker's actions
