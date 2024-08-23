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
  - Worms are a type of standalone malicious software that replicate themselves to spread to other computers over a network. They do not typically collect user information.
  - Worms represent one of the first types of malware that spreads without any authorization from the user. An executable code of another process conceals a worm
- Trojans
  - Disguise as legitimate software, grant unauthorized access
  - Trojans can steal information; however, they differ from spyware in that they often create a backdoor in the system for unauthorized access.
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
  - Spyware is a type of malicious software that collects information about users' activity without their knowledge. This data can include personal information, browsing habits, or even sensitive data such as passwords.
- Bloatware
  - Bloatware refers to unwanted software that comes preinstalled on a system or bundled with other software, occupying memory and processing resources and potentially leading to system slowdowns.
- Logic bomb
  - Malicious code that's inserted into a program, and the malicious code will only execute when certain conditions have been met
  - A logic bomb refers to a string of code embedded in a software system or computer program that remains dormant until triggered by a specific logical event.

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

- Buffer overflow
- Forgery
- Directory Traversal Attacks
  - Exploiting insufficient security validation of user-supplied input file names
  - Example: http://example.com/../../../../..etc/shadow or ((%2e%2e%2f represents ../ )
- Privilege Escalation Attack
  - Exploiting system vulnerability to gain elevated access
  - Vertical Privilege Escalation
    - Going from normal user to higher privilege (e.g., admin or root)
    - Commonly associated with code execution leading to admin-level permissions
  - Horizontal Privilege Escalation
    - Accessing or modifying resources at the same level as the attacker
    - Occurs when a user attempts to access resources for which they don't have permissions at the same level
- Replay Attacks
  - Type of network-based attack where valid data transmissions are maliciously or fraudulently re-broadcast, repeated, or delayed
  - Involves intercepting data, analyzing it, and deciding whether to retransmit it later
- Session Hijacking
  - Attacker takes over a user session to gain unauthorized access
  - Example: Concurrent session usage can lead to a significant increase in resource consumption, even if the total workload on the server has not increased.
- Malicious Code Injection Attacks
  - Injection attacks involve sending untrusted data to an interpreter as part of a command or query. This data tricks the interpreter into executing unintended commands, potentially allowing unauthorized access or data retrieval.

### Types of Cryptographic attacks

- Downgrade
  - Force systems to use weaker or older cryptographic standards or protocols
  - Countermeasures include phasing out support for insecure protocols and version-intolerant checks
- Collision
  - Find two different inputs producing the same hash output
- Birthday
  - Occurs when two different messages result in the same hash digest (collision)
  - Collisions in hashes can be exploited by attackers to bypass authentication systems
  - Use longer hash output (e.g., SHA-256) to reduce collisions and mitigate the attack

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
