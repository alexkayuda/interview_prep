# Mitigation techniques used to secure enterprises

<br>

## Important To Know

- Protecting a system from a network-based attack includes disabling unneeded logical ports, installing a host-based firewall, and updating the local antivirus software.
-

<br>

### Techniques

- Segmentation
  - Divide network into separate segments with unique security controls to limits potential damage
  - Prevent lateral movement in case of a breach
- Access control
  - Access control refers to regulating and managing the permissions granted to individuals, software, systems, and networks to access resources or information.
  - Access control lists (ACLs) enforce access control policies in computer systems and networks.
- Access control list (ACL)
  - Access control lists (ACLs) enforce access control policies.
  - Essential for securing networks from unwanted traffic
  - An ACL is a list of rules or entries that specify a user or a group's access to specific resources or ability to perform certain actions.
  - ACLs control access to operating and file systems' files, directories, or system resources. Each access control entry (ACE) typically contains a user or group identifier and the associated permissions that allow or deny actions.
  - An allow list (or approved list) will deny an execution unless it is a process that the organization explicitly authorizes.
  - Consist of allow and deny statements, often based on port numbers
  - Rule sets placed on firewalls, routers, and network infrastructure devices
  - Control the flow of traffic into and out of networks
  - May define quality of service levels inside networks but are primarily used for network security in firewalls
- Application allow list
  - An allow list (or approved list) will deny an execution unless it is a process that the organization explicitly authorizes.
- Isolation
  - increases resilience of a system by reducing the risk of system-wide failures
  - Isolation segregates individual devices within a network to limit their interaction. While isolation can help protect the network, segmentation provides better protection.
- Patching
  - Regular updates to fix known vulnerabilities in software, firmware, and applications
- Encryption
- Monitoring
- Least privilege
- Configuration enforcement
  - Ensure devices adhere to secure configurations
  - Configuration enforcement ensures that systems and devices within a network have the same configuration, allowing for easier identification of compromised systems. It is not a part of the inventory process.
- Decommissioning
  - Retire end-of-life or legacy systems posing security risks
  - The final step in the decommissioning process involves updating inventory records to reflect decommissioned devices. The decommissioning records explain why the property was on the previous inventory.
- Hardening techniques
  - Encryption
  - Installation of endpoint protection
  - Host-based firewall
  - Host-based intrusion prevention system (HIPS)
    - Host-based intrusion prevention (HIPS) describes software tools that monitor and protect individual hosts, like computers or servers, from unauthorized access and malicious activities.
    - HIPS requires deploying and configuring specialized software agents to continuously monitor and analyze endpoints.
    - HIPS systems use signature-based detection, anomaly detection, and behavior analysis to identify suspicious activities. They also detect and actively respond to threats by automatically blocking or mitigating them.
    - Host-based firewalls provide controls for incoming and outgoing network traffic and are essential for detecting potential attacks. An important technique for using them when hardening endpoints involves implementing default-deny policies to block all traffic unless explicitly allowed.
  - Disabling ports/protocols
  - Default password changes
  - Removal of unnecessary software
