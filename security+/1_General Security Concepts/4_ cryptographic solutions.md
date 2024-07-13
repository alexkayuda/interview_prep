# Cryptographic Solutions

<br>

## Key Concepts

- Symmetric Encryption
  - <b> Symmetric encryption is the most suitable method for ensuring efficient and secure transmission of large volumes of data. It uses a single shared key (private key) for both encryption and decryption, enabling faster processing and reducing computational overhead.</b>
  - Symmetric Algorithms:
    - AES
    - DES / Triple DES
    - IDEA
    - Blowfish / Twofish
    - Rivest Cipher
- Asymmetric Encryption
  - Uses a pair of keys:
    - Public key for encryption
    - Private key for decryption and digital signatures.
  - Provides confidentiality, integrity, authentication, and non-repudiation
  - Slower compared to symmetric encryption but solves key distribution challenges
  - Asymmetric Algorithms:
    - Diffie-Hellman
    - RSA
    - Elliptic Curve Cryptography
- Hashing
  - One-way cryptographic function that produces a unique message digest from an input
  - Hash Digest
    - Like a digital fingerprint for the original data
    - Always of the same length regardless of the input's length
  - Increasing Hash Security
    - Key Stretching
      - Technique that is used to mitigate a weaker key by creating longer, more secure keys (at least 128 bits) to increases the time needed to crack the key
      - Used in systems like Wi-Fi Protected Access, Wi-Fi Protected Access version 2, and Pretty Good Privacy
    - Salting
      - Adds random data (salt) to passwords before hashing
      - Ensures distinct hash outputs for the same password due to different salts
      - Prevents dictionary attacks, brute-force attacks, and rainbow tables
  - Nonces (Number Used Once)
    - Adds unique, often random numbers to password-based authentication processes
    - Prevents attackers from reusing stolen authentication data
    - Adds an extra layer of security against replay attacks
  - Hashing Algorithms:
    - MD5
    - SHA Family
    - RIPEMD
    - HMAC
- Digital Signature
  - Uses a hash digest encrypted with a private key
  - Sender hashes the message and encrypts the hash with their private key
  - Recipient decrypts the digital signature using the sender's public key
  - Verifies integrity of the message and ensures non-repudiation
  - Example: A hash digest of a message encrypted with the sender’s private key to let the recipient know the document was created and sent by the person claiming to have sent it

<br>

## Key Concepts Related to Digital Certificates

- Root of Trust
  - <b> The root of trust establishes trust in digital certificates and cryptographic operations </b>
  - Highest level of trust in certificate validation
  - Trusted third-party providers like Google, etc.
- Certificate Authority (CA)
  - Trusted third party that issues digital certificates
  - Certificates contain Certificate Authority's information and digital signature
  - Validates and manages certificates
- Registration Authority (RA)
  - Requests identifying information from the user and forwards certificate request up to the CA to create a digital certificate
  - Collects user information for certificates
  - Assists in the certificate issuance process
- Certificate Signing Request (CSR)
  - A block of encoded text with information about the entity requesting the
    certificate
  - Includes the public key
  - Submitted to Certificate Authority for certificate issuance
  - Private key remains secure with the requester
- Certificate Revocation List (CRL)
  - Maintained by Certificate Authorities
  - List of all digital certificates that the certificate authority has already revoked
  - Checked before validating a certificate
- Online Certificate Status Protocol (OCSP)
  - <b> OCSP is a protocol that verifies the validity of digital certificates. </b>
  - Determines certificate revocation status or any digital certificate using the certificate's serial number
  - Faster but less secure than CRL
- OCSP Stapling
  - Alternative to OCSP
  - Allows the certificate holder to get the OCSP record from the server at
    regular intervals
  - Includes OCSP record in the SSL/TLS handshake
  - Speeds up the secure tunnel creation
- Public Key Pinning
  - Allows an HTTPS website to resist impersonation attacks from users who
    are trying to present fraudulent certificates
  - Presents trusted public keys to browsers
  - Alerts users if a fraudulent certificate is detected
- Key Escrow Agents
  - Securely store copies of private keys
  - Ensures key recovery in case of loss
  - Requires strong access controls
- Key Recovery Agents
  - Specialized type of software that allows the restoration of a lost or or corrupted key to be performed
  - Acts as a backup for certificate authority keys

<br>

## Public key infrastructure (PKI) is based on <b> ASYMMETRIC ENCRYPTION </b>

- PKI is a framework managing digital keys and certificates for secure data transfer.
- Facilitates secure data transfer, authentication, and encrypted communications. <b> Used by HTTPS </b>

#### How Secure Connection is Established

- User connects to a website via HTTPS
- Web browser contacts a trusted certificate authority for the web server's public key
- A random shared secret key is generated for symmetric encryption
- The shared secret is securely transmitted using public key encryption
- The web server decrypts the shared secret with its private key
- Both parties use the shared secret for symmetric encryption (e.g., AES) to create a secure tunnel

### Key escrow

- Storage of cryptographic keys in a secure, third-party location (escrow)
- Enables key retrieval in cases of key loss or for legal investigations
- Relevance in PKI
  - In PKI, key escrow ensures that encrypted data is not permanently
    inaccessible
  - Useful when individuals or organizations lose access to their encryption
    keys
- Security Concerns
  - Malicious access to escrowed keys could lead to data decryption
  - Requires stringent security measures and access controls

<br>

## Digital Certificates

- Digitally signed electronic documents
- Bind a public key with a user's identity
- Used for individuals, servers, workstations, or devices
- Use the X.509 Standard
  - Commonly used standard for digital certificates within PKI
  - Contains owner's/user's information and certificate authority details

### Types of Digital Certificates

- Wildcard Certificate
  - Allows multiple subdomains to use the same certificate
  - Easier management, cost-effective for subdomains
  - If compromised - ALL subdomains are affected
- SAN (Subject Alternate Name) field
  - Certificate that specifies what additional domains and IP addresses are going to be supported
  - Used when domain names don’t have the same root domain
- Single-sided Certificates
  - Only requires the server to be validated
- Dual-sided Certificates
  - Both server and user validate each other
  - Dual-sided for higher security, requires more processing power
- Self-Signed Certificates
  - Digital certificate that is signed by the same entity whose identity it it certifies
  - Provides encryption but lacks third-party trust
  - Used in testing or closed systems
- Third-Party Certificates
  - Digital certificate issued and signed by trusted certificate authorities (CAs)
  - Trusted by browsers and systems
  - <b> Preferred for public-facing websites </b>

<br>

## Blockchain

- Shared immutable ledger for transactions and asset tracking
- Builds trust and transparency
- Is essentially a really long series of information with each block containing information in it
- Block Structure
  - Chain of blocks, each containing
    - Previous block's hash
    - Timestamp
    - Root transactions (hashes of individual transactions)
  - Blocks are linked together in a chronological order
- Public Ledger
  - Secure and anonymous record-keeping system
  - Maintains participants' identities
  - Tracks cryptocurrency balances
  - Records all genuine transactions in a network

<br>

## Encryption Tools

- TPM (Trusted Platform Module)
  - Dedicated microcontroller for hardware-level security
  - Protects digital secrets through integrated cryptographic keys
  - Used in BitLocker drive encryption for Windows devices
  - Adds an extra layer of security against software attacks
  - Example: TMP is a cryptoprocessor implemented as a module <b> within the CPU </b> on a computer or mobile device.
- HSM (Hardware Security Module)
  - Physical device for safeguarding and managing digital keys
  - Ideal for mission-critical scenarios like financial transactions
  - Performs encryption operations in a tamper-proof environment
  - Ensures key security and regulatory compliance
  - Example: An HSM is a cryptoproccessor that implements hardware through a removable or dedicated form factor, such as plug-in peripheral component interconnect express (PCIe) adaptor cards.
- Key Management System (KMS)
  - Manages, stores, distributes, and retires cryptographic keys
  - Centralized mechanism for key lifecycle management
  - Crucial for securing data and preventing unauthorized acces
  - Automates key management tasks in complex environments
- Secure Enclaves
  - <b> A secure enclave enhances security by providing an isolated environment for executing sensitive operations and protecting critical data. Furthermore, it achieves trusted code isolation and prevention of unauthorized access through hardware or software mechanisms. </b>
  - Coprocessor integrated into the main processor of some devices
  - Isolated from the main processor for secure data processing and storage
  - Safeguards sensitive data like biometric information
  - Enhances device security by preventing unauthorized access

<br>

## Obfuscation

- Steganography
  - Conceals a message within another to hide its very existence
  - Involves altering image or data elements to embed hidden information
  - Primary goal is to prevent the suspicion that there’s any hidden data at all
  - Detection is challenging due to hiding data in plain sight
- Tokenization
  - Substitutes sensitive data with non-sensitive tokens
  - Original data securely stored elsewhere
  - Tokens have no intrinsic value
  - Reduces exposure of sensitive data during transactions
  - Commonly used for payment systems to comply with security standards
- Data Masking (Data Obfuscation)
  - Disguises original data to protect sensitive information
  - Maintains data authenticity and usability
  - Common in industries handling personal data
  - Masks portions of sensitive data for privacy, e.g., credit card digits, social security numbers

<br>
