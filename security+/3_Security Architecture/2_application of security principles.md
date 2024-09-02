# Given a scenario, apply security principles to secure enterprise infrastructure.

<br>

## Important to Remember

<br>

### Infrastructure considerations

(What do we need to consider when building an infra???)

- Device placement
  - Proper placement of routers, switches, and access points is crucial for Optimal data flow and latency
- Security zones
  - Isolate devices with similar security requirements
- Screened Subnets = DMZ
  - Act as buffer zones between internal and external networks
  - Hosts public-facing services, protecting core internal networks
  - <b> Use the term "screened subnet" instead of "DMZ" </b>
- Attack surface
  - Potential points where unauthorized access or data extraction can occur
- Connectivity Methods
  - Consider factors like scalability, speed, security, and budget constraints
  - Wired (e.g., Ethernet) offers stability and speed but restricts mobility
  - Wireless (e.g., Wi-Fi) provides flexibility but may suffer from interference and security issues
- Failure modes
  - Choose between "fail-open" and "fail-closed" modes to handle device failures
  - Fail-open
    - Allows traffic to pass during a failure, maintaining connectivity but reducing security
  - Fail-closed
    - Blocks all traffic during a failure, prioritizing security over connectivity
  - The choice depends on the organization's security policy and the criticality of the
    network segment
- Device attribute
  - Active devices (e.g., intrusion prevention systems) monitor and act on network traffic.
  - Passive devices (e.g., intrusion detection systems) observe and report without altering traffic
  - Inline devices are in the path of network traffic
  - Taps and monitors capture data without disruption
- Network appliances
  <br>
  A dedicated hardware device with pre-installed software for specific networking services
  <br>
  Types of Network Appliances:

  - Jump server / Jump Box
    - Secure gateways for system administrators to access devices in different security zones
    - Control access and reduce the attack surface area
    - Offer protection against downtime and data breaches
    - Simplify logging and auditing
    - Speed up incident response during cyber-attacks
  - Proxy server
    - Act as intermediaries between clients and servers
    - Provide content caching, requests filtering, and login management
    - Enhance request speed and reduce bandwidth usage
    - Add a security layer and enforce network utilization policies
    - Protect against DDoS attacks
    - Facilitate load balancing and user authentication
    - Handle data encryption and ensure compliance with data sovereignty laws
  - Intrusion prevention system (IPS)/intrusion detection system (IDS)
  - Load balancer
    - Distribute network/application traffic across multiple servers
    - Enhance server efficiency and prevent overload
    - Ensure redundancy and reliability
    - Perform continuous health checks
    - Application Delivery Controllers (ADCs) offer advanced functionality
    - Essential for high-demand environments and high-traffic websites
  - Sensors
    - Act as the first line of defense against cyber threats
    - Monitor, detect, and analyze network traffic and data flow
    - Identify unusual activities, security breaches, and performance issues
    - Provide real-time insights for proactive network management
    - Aid in performance monitoring and alerting

- Port security
  <br> A network switch feature that restricts device access to specific ports <b> based on MAC addresses </b>
  <br> Enhances network security by preventing unauthorized devices from connecting

  - CAM Table (Content Addressable Memory)
    - Stores MAC addresses associated with switch ports
    - Vulnerable to MAC flooding attacks, which can cause the switch to fail open
  - 802.1X Authentication
    - Provides port-based authentication for wired and wireless networks
    - Prevents rogue device access
    - - Utilizes RADIUS or TACACS+ for actual authentication
    - Requires three roles
      - Supplicant
      - Authenticator
      - Authentication server
  - Extensible Authentication Protocol (EAP) is a framework for various authentication methods
    <br> Different variants:
    - EAP-MD5
      - Uses simple passwords and the challenge handshake authentication process to provide remote access authentication
      - One-way authentication process
      - Doesn’t provide mutual authentication
    - EAP-TLS
      - Uses public key infrastructure with a digital certificate which is installed on both the client and the server
      - Uses mutual authentication
    - EAP-TTLS
      - Requires a digital certificate on the server, but not on the client
      - The client uses a password for authentication
    - EAP-FAST
      - Uses protected access credential, instead of a certificate, to establish mutual authentication
    - PEAP
      - Supports mutual authentication using server certificates and Active Directory databases to authenticate a password from the client
    - EAP-LEAP
      - Cisco proprietary and limited to Cisco devices

- Firewall types
  - Web application firewall (WAF)
    - Focuses on inspecting HTTP traffic
    - Prevents common web application attacks like cross-site scripting and SQL injections
    - Can be placed
      - In-line (live attack prevention)
        - Device sits between the network firewall and the web servers
      - Out of band (detection)
        - Device receives a mirrored copy of web server traffic
  - Unified threat management (UTM)
    - Combines multiple security functions in a single device
    - Functions include firewall, intrusion prevention, antivirus, and more
    - Reduces the number of devices
    - Are a single point of failure
    - UTMs use separate individual engine
  - Next-generation firewall (NGFW)
    - Application-aware
      - distinguish between different types of traffic
    - Conduct deep packet inspection and use signature-based intrusion protection
    - Operate fast within minimal network performance impact
    - Offer full-stack traffic visibility
    - Can integrate with other security products
  - Layer 4 Firewall
    - Operates at the transport layer
    - Filters traffic based on port numbers and protocol data
  - Layer 7 Firewall
    - Operates at the application layer
    - Inspects, filters, and controls traffic based on content and data characteristics

<br>

### Secure communication / access

- Virtual private network (VPN)
- Remote access
- Tunneling
  - Transport Layer Security (TLS)
  - Internet protocol security (IPSec)
- Software-defined wide area network (SD-WAN)
- Secure access service edge (SASE)

### Selection of effective controls
