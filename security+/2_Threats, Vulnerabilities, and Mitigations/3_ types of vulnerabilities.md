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

#### Application Vulnerabilities

- Memory injection
  - Act of exploiting vulnerabilities in a computer's software or operating system to inject malicious code into the computer's memory
- Buffer overflow
  - Occurs when a process stores data outside the memory range allocated by the developer
  - Attackers exploit the excess data written beyond buffer boundaries to manipulate program execution
  - <b> Buffer overflow attacks occur when an application receives more data than it can process, which can cause the application to crash or allow an attacker to execute arbitrary code. </b>
  - Mitigation:
    - Address Space Layout Randomization (ASLR)
      - Helps prevent attackers from guessing return pointer addresses
      - Randomizes memory addresses used by well-known programs, making it harder to predict the location of the attacker's code
- Race conditions
  - Race conditions occur when multiple threads or processes access and manipulate shared resources simultaneously
  - <b> Time-of-check (TOC) </b>
    - Attackers manipulate a resource's state after it is checked but before it is used
    - Example:
      - overdrawing a bank account due to a time delay between checking and transferring funds
  - <b> Time-of-Use (TOU) </b>
    - Attackers alter a resource's state after it is checked but before it is used
    - Focuses on the time when the resource is utilized, rather than the time of the initial check
  - <b> Time-of-Evaluation (TOE) </b>
    - Attackers manipulate data or resources during the system's decision-making or evaluation process
    - Can lead to incorrect results or unexpected behavior
- Malicious update
  - Appear as legitimate security updates but contain malware or exploits

#### OS-based Vulnerabilities

- Unpatched Systems
  - Lack the latest security updates, making them vulnerable
- Malicious Updates
  - Appear as legitimate security updates but contain malware or exploits
- Data Exfiltration
  - Involves unauthorized data transfers from an organization to an external location
- Misconfigurations

#### Web-based Vulnerabilities

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

#### Hardware Vulnerabilities

Security flaws or weaknesses in a device's physical components or design

- Firmware
  - Specialized software stored on hardware devices
  - <b> Example: BIOS or Drivers vulnerabilities include instances where processors inside the computer allow malicious programs to steal data during processing. </b>
- End-of-life
  - No updates or support will be provided from the manufacture
- Legacy
  - Outdated and superseded by newer alternatives

Example:

- Question: Which risk mitigation strategies should the corporation adopt to ensure the security of its hardware devices without unnecessarily hindering its operations?
  - Answer: Implement strict supplier vetting processes && Adopt a zero-trust network architecture.
- Question: What is the system administrator's MOST effective course of action to reduce potential security vulnerabilities caused by these legacy machines running end-of-life operating systems?
  - Answer: Isolate the legacy machines on a separate network segment

#### Virtualization Vulnerabilities

- Virtual Machine Escape (VME)
  - Attackers break out of isolated VMs to access the hypervisor
- Resource reuse
  - Improper clearing of resources may expose sensitive data
  - <b> MITIGATION: Apply secure deallocation.</b>

#### Cloud-specific Vulnerabilities

#### Supply chain Vulnerabilities

- Service provider
- Hardware provider
- Software provider

#### Cryptographic Vulnerabilities

#### Misconfiguration

#### Mobile device Vulnerabilities

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
