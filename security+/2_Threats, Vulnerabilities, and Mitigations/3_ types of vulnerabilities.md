# Types of Vulnerabilities

<br>

## Important To Know

- Vulnerabilities = Weaknesses
  - Weaknesses or flaws in hardware, software, configurations, or processes
  - Consequences
    - Unauthorized Access
    - Data Breaches
    - System Disruptions
- Attacks = Actions
  - Deliberate actions by threat actors to exploit vulnerabilities
  - Forms:
    - Unauthorized Access
    - Data Theft
    - Malware Infections
    - DoS Attacks
    - Social Engineering

<br>

#### Application

- Memory injection
- Buffer overflow
  - Occurs when a process stores data outside the memory range allocated by the developer
  - Attackers exploit the excess data written beyond buffer boundaries to manipulate program execution
  - Mitigation:
    - Address Space Layout Randomization (ASLR)
      - Helps prevent attackers from guessing return pointer addresses
      - Randomizes memory addresses used by well-known programs, making it harder to predict the location of the attacker's code
- Race conditions
  Race conditions occur when multiple threads or processes access and manipulate shared resources simultaneously
  - Time-of-check (TOC)
    - <b> Attackers manipulate a resource's state after it is checked but before it is used </b>
    - Example:
      - overdrawing a bank account due to a time delay between checking and transferring funds
  - Time-of-Use (TOU)
    - Attackers alter a resource's state after it is checked but before it is used
    - Focuses on the time when the resource is utilized, rather than the time of the initial check
  - Time-of-Evaluation (TOE)
    - Attackers manipulate data or resources during the system's decision-making or evaluation process
    - Can lead to incorrect results or unexpected behavior
- Malicious update

#### Operating system (OS)-based

- Unpatched Systems
  - Lack the latest security updates, making them vulnerable
- Malicious Updates
  - Appear as legitimate security updates but contain malware or exploits
- Data Exfiltration
  - Involves unauthorized data transfers from an organization to an external location
- Misconfigurations

#### Web-based

- SQL injection (SQLi)
  - Inserting malicious SQL code into input fields
    - Attackers use URL parameters, form fields, cookies, POST data, or HTTP headers for SQL injection
  - Prevention
    - Input validation
    - Sanitize user data
    - Use a web application firewall
  - Example:
    - Involves statements like " ‘ OR 1=1"
- XML Injection
  - XML Bomb (Billion Laughs Attack)
    - Consumes memory exponentially, acting like a denial-of-service attack
  - XXE (XML External Entity) Attack
    - Attempts to read local resources, like password hashes in the shadow file
- Cross-site scripting (XSS)
  - Injects a malicious script into a trusted site to compromise the site’s visitors
  - Goal:
    - Have visitors run a malicious script so your system will process it, bypassing the normal security mechanisms
  - How it works:
    1. The attacker identifies an input validation vulnerability within a trusted website
    2. The attacker crafts a URL to perform a code injection against the trusted website
    3. The trusted site will return a page containing the malicious code injected
    4. The malicious code runs in the client’s browser with permission level as the trusted site
- Cross-site Request Forgery (XSRF)
  - Malicious script is used to exploit a session started on another site within the same web browser

#### Hardware

Security flaws or weaknesses in a device's physical components or design

- Firmware
  - Specialized software stored on hardware devices
  - Example: BIOS or Drivers
- End-of-life
  - No updates or support will be provided from the manufacture
- Legacy
  - Outdated and superseded by newer alternatives

#### Virtualization

- Virtual machine (VM) escape
- Resource reuse

#### Cloud-specific

#### Supply chain

- Service provider
- Hardware provider
- Software provider

#### Cryptographic

#### Misconfiguration

#### Mobile device

- Side loading
  - Installing apps from unofficial sources bypassing the device's default app store
  - Can introduce malware; download apps from official sources with strict review processes
- Jailbreaking
  - Gives users escalated privileges but exposes devices to potential security breaches
  - Prevents installation of manufacturer updates, leaving devices vulnerable

#### Zero-day

- Zero-day Vulnerabilities
  - Discovered or exploited before vendors issue patches
- Zero-day Exploits
  - Attacks that target previously unknown vulnerabilities
