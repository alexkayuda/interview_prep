# Cryptographic Solutions

<br>

## Public key infrastructure (PKI) is based on <b> ASYMMETRIC ENCRYPTION </b>

- PKI is a framework managing digital keys and certificates for secure data transfer.
- Facilitates secure data transfer, authentication, and encrypted communications. <b> Used by HTTPS </b>

### Establishing a Secure Connection

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
