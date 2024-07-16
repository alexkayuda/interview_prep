# Threat Vectors && Attack Surfaces

<br>

## Important To Know

- Threat Vector = "how" of an attack
  - Means or pathway by which an attacker can gain unauthorized access to a computer or network to deliver a malicious payload or carry out an unwanted action
- Attack Surface = "where" of the attack
  - Encompasses all the various points where an unauthorized user can try to enter data to or extract data from an environment

<br>

## Threat Vectors

- Message-based:
  - Email
  - Short Message Service (SMS)
  - Instant messaging (IM)
- Image-based:
  - Embedding of malicious code inside of an image file by the threat actor
- File-based:
  - The files, often disguised as legitimate documents or software, can be transferred as email attachments, through file-sharing services, or hosted on a malicious website
- Voice calls:
  - <b> Vhishing </b> = voice calls to trick victims into revealing their sensitive information to an attacker
- Removable device:
  - <b> Baiting </b> = malware-infected USB drive in a location where their target might find it
    - parking lot or the lobby of the targeted organization
- Unsecure Networks:
  - Wireless:
    - unauthorized individuals can intercept the wireless communications or gain access to the network
    - Example: A company using Wi-Fi Protected Access (WPA) wireless security on their wireless access points (WAPs) uses Lightweight Extensible Authentication Protocol (LEAP) to authenticate users to the network. LEAP is vulnerable to password cracking. What other options does the company have to mitigate this vulnerability?
      - Flexible Authentication via Secure Tunneling (EAP-FAST)
      - Protected Extensible Authentication Protocol (PEAP)
  - Wired:
    - Physical access to the network infrastructure can lead to various attacks:
      - MAC Address Cloning
      - VLAN Hopping
  - Bluetooth:
    - <b> BlueBorne </b> = set of vulnerabilities that allow an attacker to take over devices, spread malware, or even establish an on-path attack to intercept communications without any user interaction
    - <b> BlueSmack </b> = type of Denial of Service attack that targets Bluetooth-enabled devices by sending a specially crafted Logical Link Control and Adaptation Protocol packet to a target device
- Vulnerable software
  - Client-based vs. agentless

<br>

## Human Vectors && Social Engineering

Manipulative strategy exploiting human psychology for unauthorized access to systems, data, or physical spaces

- Phishing
  - fraudulent emails that appear to be from reputable sources with the aim of convincing individuals to reveal personal information
- Spear Phishing
  - Has a higher success rate campaing that tightly focused on a specific group of individuals or organizations
- Angler phishing
  - Phishing attack that targets <b> social media users. </b> Attackers disguise themselves as a customer service agent on social media in order to reach a disgruntled customer and obtain their personal information or account credentials
- Whaling
  - Form of spear phishing that targets high-profile individuals, like CEOs or CFOs
  - <b> It is like business email compromise but may not involve posing as a colleague or business partner. </b>
- Business Email Compromise (BEC)
  - Targets specific individuals, such as executives.
  - The threat actor impersonates a trusted colleague, business partner, or vendor to trick the target into performing actions or disclosing information.
- Vishing (Voice Phishing)
  - Attacker tricks their victims into sharing personal or financial information over the phone
- Smishing (SMS Phishing)
  - Use of text messages to trick individuals into providing their personal information
- Misinformation/disinformation
- Impersonation
  - Pretending to be someone else
  - Includes brand impersonation, typo-squatting, and watering hole attacks
- Brand impersonation
  - More specific form of impersonation where an attacker pretends to represent a legitimate company or brand
  - Attackers use the brand’s logos, language, and information to create deceptive communications or website
- Business email compromise
- Pretexting
  - Creating a fabricated scenario to manipulate targets by giving some amount of information that seems true so that the victim will give more information
  - Impersonating trusted figures to gain trust
- Watering hole
  - attackers compromise a specific website or service that their target is known to use
- Typosquatting (A.K.A URL hijacking or cybersquatting)
  - a domain name that is similar to a popular website but contain some kind of common typographical errors
