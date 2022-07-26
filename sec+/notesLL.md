# Lesson Notes : Linkedin Learning 

<h2>Table of Contents</h2>

<!-- TOC -->

- [Lesson Notes : Linkedin Learning](#lesson-notes--linkedin-learning)
  - [CompTIA Security+ (SY0-601) Cert Prep: 2 Secure Code Design and Implementation](#comptia-security-sy0-601-cert-prep-2-secure-code-design-and-implementation)
    - [Software Assurance:](#software-assurance)
      - [Code Security test](#code-security-test)
      - [Fuzzing](#fuzzing)
      - [Code repository](#code-repository)
      - [Application Control](#application-control)
      - [Third-party code](#third-party-code)
    - [Application Attacks](#application-attacks)
      - [OWASP Top 10](#owasp-top-10)
      - [Application Security](#application-security)
      - [Request Forgery](#request-forgery)
      - [Defend against Directory Traversal](#defend-against-directory-traversal)
      - [Overflow Attacks](#overflow-attacks)
      - [Cookies and Attachments](#cookies-and-attachments)
      - [Session Hijacking](#session-hijacking)
      - [Code Execution attacks](#code-execution-attacks)
      - [privillege escalation](#privillege-escalation)
      - [Driver Manipulation](#driver-manipulation)
      - [Memory vulnerabilities](#memory-vulnerabilities)
      - [Race condition vulnerabilities](#race-condition-vulnerabilities)
    - [Secure Code Practices](#secure-code-practices)
      - [Input validation](#input-validation)
      - [Parameterized queries](#parameterized-queries)
      - [Authentication and session management issues](#authentication-and-session-management-issues)
      - [Output encoding](#output-encoding)
      - [Error and exception handling](#error-and-exception-handling)
      - [Code signing](#code-signing)
      - [Database security](#database-security)
      - [Data deidentification](#data-deidentification)
    - [Data obfuscation](#data-obfuscation)
  - [CompTIA Security+ (SY0-601) Cert Prep: 3 Cryptography Design and Implementation](#comptia-security-sy0-601-cert-prep-3-cryptography-design-and-implementation)
    - [Encryption](#encryption)
      - [Undestanding Encrption](#undestanding-encrption)
      - [Symmetric and Asymmetric](#symmetric-and-asymmetric)
      - [Goals of Cryptography](#goals-of-cryptography)
      - [Codes and Ciphers](#codes-and-ciphers)
      - [Cryptographic math](#cryptographic-math)
      - [Choosing encryption algorithms](#choosing-encryption-algorithms)
      - [the perfect encryption algorithm](#the-perfect-encryption-algorithm)
      - [The cryptographic lifecycle](#the-cryptographic-lifecycle)
    - [Symmetric Cryptography](#symmetric-cryptography)
    - [Asymmetric Cryptography](#asymmetric-cryptography)
    - [Key Mananagement](#key-mananagement)
    - [Public Infrastructure](#public-infrastructure)
    - [Cryptanalytic Attacks](#cryptanalytic-attacks)
    - [Cryptographic Applications](#cryptographic-applications)
  - [CompTIA Security+ (SY0-601) Cert Prep: 4 Identity and Access Management Design and Implementation](#comptia-security-sy0-601-cert-prep-4-identity-and-access-management-design-and-implementation)
    - [Identification](#identification)
    - [Authentication](#authentication)
    - [Authorization](#authorization)
    - [Account Management](#account-management)
  - [CompTIA Security+ (SY0-601) Cert Prep: 5 Physical Security Design and Implementation](#comptia-security-sy0-601-cert-prep-5-physical-security-design-and-implementation)
    - [Data Center Protection](#data-center-protection)
    - [Hardware and Data Security](#hardware-and-data-security)
    - [Business Continuity](#business-continuity)
    - [Disater Recovery](#disater-recovery)
  - [CompTIA Security+ (SY0-601) Cert Prep: 6 Cloud Security Design and Implementation](#comptia-security-sy0-601-cert-prep-6-cloud-security-design-and-implementation)
    - [Cloud Computing](#cloud-computing)
    - [Virtualization](#virtualization)
    - [Cloud Building Blocks](#cloud-building-blocks)
    - [Cloud Reference Architecture](#cloud-reference-architecture)
    - [Cloud Security Controls](#cloud-security-controls)

<!-- /TOC -->

## CompTIA Security+ (SY0-601) Cert Prep: 2 Secure Code Design and Implementation
### Software Assurance:
  * Code Review : Use peer analysis to access code
  * Verifcation and Validation
  * UAT : Usability test
  * Beta Testing / Regression testing

#### Code Security test
  * Static code tests : does not run the code like code review
  * Dynamic Test : Run the code

#### Fuzzing
  * Fuzz testing input sources
    * Developer-supplied input
    * Developer-supplied script
    * Generation fuzzing 
    * Mutation fuzzing
  * ZAP software - OWASP Zed Attack Proxy - code testing tool

#### Code repository
  * Why?
    * version control
    * repository
    * coordinate among other developers
    * Perform control
    * Code resuse
  * Avoid Dead Code
  * Github
  * Integrity Measurement - Provision and decomission according to management process

#### Application Control
  * restrict softwre that may run that does not meet the policy
  * Whitelisting
  * Blacklisting 
  * Windows have applocker
  * Host softwre baselining

#### Third-party code
  * Libraries - contain shared software code
    * Programing libraries (opensource or paid)
  * SDKs - programing resources
  * APIs - services available for interaction to another platform or users

[Back to Top](#comptia-security)
<br/><br/>

### Application Attacks
#### OWASP Top 10
  * Broken access conterol - allows unauthorized access
  * Cryptographic Failure - Allow access to sensitive data
  * Injection Flas - Insers unwanted code
  * Insecure Design - Fails to meet security requirements
  * Security Misconfigurations - firewalls, OS settings etc
  * Vulnerable COmponents  related to apps
  * Authentication Failure - 
  * Integrity Failure - alloes insertion of insecure code
  * Monitoring and log failure - can deprive analyst of needed data
  * Request forgery - trickls servers into requesting URLS 
  * Check out Center for internet security website

#### Application Security
  * Tpes of softwares
    * Purchased Software
    * Developed Software
  * Application Hardening
    * use proper authentication
    * encrypt sentisitive data
    * validate user input
    * avois and remediate known expoits
    * deploy obfuscation and camoufladge - hide details of the code for reverse engineering
    * prompt patching is critical
  * Application COnfiguration
    * Type and scopre of encryption
    * Users with acess to the application
    * Access granted to autjprised users
    * Security of underlysing inferastructure
    * Recommendation : Configuration baseline
  * Prevent SQLi
    * database-driven Authentication are exploited through SQL queries
    * Prevent with:
      * Inout validation
      * Parameterized SQL Request
  * Cross-Site Scripting (XSS)
    * Occurs when an attacker embeds malicious scripts in a third-party website that are later run by innocent visitors to that site.
    * Recommendation : Use input validation, do not allow ```<script>``` tags in user-supplied input
  
#### Request Forgery
  * aka CSRF, XSRF
  * Attacks leverage that the users users are often logged into multiple sites at the same time and use one site to trick the browser into sending malicioiys request to another site without the user's knowledge.
  * Ofthen using image tags
  * Defending : 
    * Rearchitect web application
    * Prevent web applications
    * Prevent the use of HTTP GET requests
    * Advise users to log out of sites
    * Authomatically log out users afer an idle period
  * Client-side Attack
  * SSRF - Request forgery attack that targetrs servers rather than users by manipulating servers into retrieving malicious data from what it believes to be a trusted source.

#### Defend against Directory Traversal
  * Uses navigation system to check contents of server from web application
  * Recommendation:
    * input validation
    * strict system files access control
  
#### Overflow Attacks
  * Buffer over flow on memory

#### Cookies and Attachments
  * Privacy risk
    * cookies can used accross different websites
    * cookies can track user activity
    * if you log into one site everything is de-anonymized
  * Cookie management from browser

#### Session Hijacking
  * Cookie Guessing if not randomly generated
  * Session replay if cookie value has been knowm to attacker
  * Recommendation : secure cookies sent using encryption

#### Code Execution attacks
  * Occur when an attacker exploits a vulnerability in a system that allows the attacker to run commands on that system.
  * Recommendation : Patch the system
  * Objectives:
    * Install malicious code
    * Join a system to a botnet
    * steal sensitive information
    * Create accounts for later access
  * Protection:
    * least privillege - Limit adninsitrative access
    * Patch systems and applications 

#### privillege escalation
  * When hacker gains administrative access
  * Mitigation strategies:
    * Input validation
    * Patch OS, paltforms and application
    * Enforce least privilege principle.
    * Use DEP (Data execution Protection) and ASLR (address space layout randomization) technologies
  
#### Driver Manipulation
  * Refactoring :
    * Mofiying a driver to carry malicious activities
    * Requires acces to the source code
  * Shimming
    * Wraps a legit driver with malicious shim
    * Does not require accezss to the legit driver's source code
  * Recommendation : Code signing 
  
#### Memory vulnerabilities
  * Resource exhaustion may slow down or disable system.
  * Memorry leak - fails to release memry for reuse. may crash the machine.
  * Memory pointers - folowing a pointer is know as pointer dereferencing. If referenced a null pointer may cause crash or by pass security controls.
  * DLL Injection - tricks an application into loading malicious code
  * Recommendation : proper meomry mabnagement in development
  
#### Race condition vulnerabilities
  * Occurs when the proper functioning of a security control depends upon the timing of actions performed by the user of computer.
  * Uncontrolled race conditions can be significant security vulnerabilities. Excample:
    * Time of check / Time of Use - time elapsing between authorizatrion and action
    * Prevention : Locks prevent simulataneous transactions from causing race conditions.


[Back to Top](#comptia-security)
<br/><br/>

### Secure Code Practices
#### Input validation
* Filters user-supplied input
* Approaches
  * Whitelisting - specifies which is allowed
  * Blacklisting - specified which is not allowed
  
#### Parameterized queries
  * In a parameterized query, the client does not directly send SQL code to the database server. Instead, the client sends arguments to the server, which then inserts those arguments into a pre-compiled query template.
  * Like Stored procedures.
  
#### Authentication and session management issues
  * Never store password in plaintext form
  * Recommendation:
    * Hashing - 
    * Salting - adds random value to the password prior to hashing to protevt against rainbow table attacks
    * encrypt password in transite - use TLS
  
#### Output encoding
  * Replaces dangerous characters. like:
    * HTMl Encoding - &
    * URL Encoding - %
  * Use trusted libraries to perform output encoding
  
#### Error and exception handling
  * Inaappropriate handling of erros is acrucial security issue.
  * Unpredictanle states jeppardize application security
  * implement error handling or Exception Handling to avoid unpredictable states
  
#### Code signing
  * Digital signature to provide nonrepudiation
  * Code signing
    * Obtain cert and sign the script

#### Database security
  * Database normalization
    * Prevent data inconsistency
    * Prevent update anomalies
    * Reduce the need for restructuring existing databases
    * Make the database schema more informative
  * Normalization Rules
    * 1st normal form
      * Create separate tables for different sets of related data
      * Provide a primary key for every table
      * Records may not have multivalued fields
      * Records in a table must have the same number if fields
    * 2nd Normal form
      * Includes 1st normal form
      * every non-key field must be a fact about the entire key
    * 3rd normal form
      * includes 1st and 2nd form
      * No non-key field may be a fact about another non-key field
  * use encrytion to protect senstive data
  * Databse activity monitoring - to check access and malicious activity
  * use stored procedure whenever prossible
  
#### Data deidentification
  * Deidentification - removes obvious identifiers
  * ZIP Code + Birthday + Sex (male/female) = 87% unique
  * Anonmization - Remove the posibility of identification
  * HIPAA Deidentification Standard - Privacy rule

### Data obfuscation
  * Transforms personaly idenfuyiong infoormation into a form where it is no longer possible to tie it to an individual person
    * hasing - replaces sensitive fields
      * Weakness - vilnerable table attack - compares hash values with precomputed hasing
    * Salting - Uses randome values to defeat rainbow tables
    * Tokenization - replaces sensitive fields with a random identifier
    * masking - redact sentitive information from a file

[Back to Top](#comptia-security)
<br/><br/>

## CompTIA Security+ (SY0-601) Cert Prep: 3 Cryptography Design and Implementation
### Encryption
#### Undestanding Encrption
  * Cryptography - the use of nathematical algorithms to transfgorm information into an encrypted form that is not readable by unauthorized indiivuals.
  * Encryption
  * Decryption
  
#### Symmetric and Asymmetric
  * Symmetric - uses the same secret key for encryption and decryption
  * Asymmetric - uses diff key for encryption and decrytpion using private and public key

#### Goals of Cryptography
  * Confidentiality - no unauthorized access
    * States of data
      * Data at rest - storage
      * Data in transit - network
      * Data in use - in memmory
  * Integrity - nop unauthorized change
  * Authentication - proof of identity
  * Obfuscation - hiding sensitive data
  * Non-repudation - verification of origin
    * Digital signitures
    * possible only with asymetric cryptography

#### Codes and Ciphers
  * Code - a system that substitute one owrd or phrase for another
  * Cipers - uses mathematical algorithms
    * Stream Ciphers - operate one character or bot from a message at a time
    * Block ciphers - operate on large sements of the message at the same time
  * Substitution ciphers - change the characters in a message
  * Transposition Ciphers - rearrange the characters in a message

#### Cryptographic math
  * Exclusinve OR (XOR) - exactly one of two input values is true
  * Confusion - every bit of the ciphertext must depend upon more than one bit of the encryption key
  * Diffusion - Changing a single bit of text should change about 50% of the ciphertext bits.
  * Obfuscation - application of cryptography in software development to hide the source code from users

#### Choosing encryption algorithms
  * use established alorithms
  * security through obscurity is not ideal

#### the perfect encryption algorithm
  * One-time pad

#### The cryptographic lifecycle
  1. Initiation - Gather requiremenbts for new cryptographic system.
  2. Development and Acquisition - FInd an appropriate combination of hardware, software and algorithms that meet objectives.
  3. Implementation and Assesment - configure system for use, including test
  4. Operations and Maintenance - ensure continued secure operation
  5. Sunset - phase out the system and destroy used matrials
   

[Back to Top](#comptia-security)
<br/><br/>

### Symmetric Cryptography
  * DES - Data Encryoption Standard
    * symmetric algo
    * block cipher operating on 64-bit blocks
    * Key length of 56 bits
    * insecure
  * 3DES
    * 3x DES
    * symmetric algo
    * block cipher operating on 64-bit blocks
    * Key length of 112 bits
    * phaseout
  * AES, Blowfish and Twofish
    * AES - Advance Encryption Standard - 
      * symmetric algo
      * block cipher operating on 128-bit blocks
      * Key length of 128,192 or 256 bits
      * Secure
    * Blowfish
      * Public domain algo
  * RC4
    * Uses a pseudorandom keystream
    * Applications:
      * WEP
      * WPA
      * SSL
      * TLS
  * Cipher Modes
    * Describes how an alforithm encrypts and decrypts data
    * Electronic Codebook mode (ECB)
    * Cipher Block Chaining (CBC) Mode
    * Counter Mode (CTR)
  * Steganography


[Back to Top](#comptia-security)
<br/><br/>

### Asymmetric Cryptography
  * RSA - uses private and public key
  * PGP - prettry good privacy
    * uses private and public key
    * combines both dymmetric and asymmetric cryptography
  * Elliptic curve and quantum cryptography
    * Quantum Computing - uses quantum mechnics principles
    * Elliptic curve cryptography can't protect against quantum attack
  * TOR and PFS
    * The Onion Router (TOR) is a software package that uses encryption and relay nodes to facilitate aninymous internet access.
    * Perfect Forward Secrecy (PFS) - hides node's identity from each other

[Back to Top](#comptia-security)
<br/><br/>

### Key Mananagement
  * Key Exchange
    * Out-of-band key exchange - uses a different channel that both parties trust
      * Face-to-face meeting
      * Physical mail
      * Phone call
    * In-band key Exchange - securely exchange keys digitally
      * like Diffie-Hellman
  * Diffie-Hellman Algorithm
    * Provides symmetric key exchance capability
  * Key excrow
    * Allows governmentt access to keys
    * Recovery Agents - allow internal access to lost keys.
  * Key Stretching
    * Takes a relatively insecure value, such as a password and uses mathematicak trechniques to strengthen it, making i harder to crack.
      * Salting - adds value to the encryption key to make it more complex
      * Hashing - Adds time to the verification process by requiring more math.
        * Verifying one key is fast but guessing millions of keys is slow.
        * PBKDF2 or Password-Based Key Derivation Function v2
          * Uses salting and hasing to stretch a key
          * Recommendation is it sHould be used at least 4k times.
        * bcrypt - key stretching with Blowfish
  * hardware security Modules
    * hardware Security Modules (HSMs) - Manage encruption and perform cryptographiv operations
      * Expensive
      * Complies with FIPS 140-2 Security
  

[Back to Top](#comptia-security)
<br/><br/>

### Public Infrastructure
* Trust Modes
  * No an Imposter and no one else is evesdropping to key exchange
  * Asymmetric Cryptography
    * Dont neec to share private keys
    * Public keys can and should be shared freely
    * No need for evesdropping protection during exchange
    * Still need to prevent imposters via:
      * Personal key exchange
      * Web of trust (WOT)
        * Relies on indirect relationships
        * You know somebody who know somebody that know that person.
        * participans digitally sign the public keys of people they know personally
        * Issues:
          * Decetralized appraoch
          * High barrier to entry
          * Requires technical knowledge
      * Public key infrastructure (PKI)
* PKI and Digital certificates
  *  The Public key insfrastructure (PKI) depends upon highjly trusted certifiacte authorities (CAs)
  *  Certificate Authorities (CA) - verifies identities and vouch for the public key associated with that individual/organization.
* Hash Functions
  * One-way function that transform a variable length input into a unique fixed-length output
  * may fail if:
    * reversible
    * not colision resistant i.e. not unique results
  * Message Digetst 5 (MD5)
    * 128 bit hash
    * no longer secure
  * Secure hash Algorithm (SHA) by NIST
    * SHA-1 is a 160 hash bit value - not secure
    * SHA-2 is a 224,256,384 and 512 bit hash value
      * Same mathmatical appraoch as MD5  
    * SHA-3
  * RIPEMD -  Race Integrity Primitives Evaluation Message Digest
    * 128,160,256 and 320 bit hashses
    * 128 bit is not secure
  * HMAC - Hash-based Message Authentic Code
    * combines symmetric cryptography and hasing
    * provides authentication and integrity
* Digital Signatures
  * Use Assymmetric cryptography to achieve integrity, authentiation and non-repudiation
  * Depends upon
    * collision resistant
    * asymmetric cyptography
    * Digital signing message does not provide confidentiality
* Digital Signatures Standard (DSS)
  * FIPS-186-4
  * Approved DSS algorithms
    * DSA - Digital signature algorithm
    * RSA - Rivest-shamir-adelman
    * ECDSA - Elliptic curve digital signature algorithm
* Create a digital Certificate
  * Follow the x.509 standard
* Revoke a digital Certificate
  * Certificate Revocation List (CRL)
    * includes serial numbers of revoked certs
    * Inefficient sionce the list has to be consulted everytime and may cause bandwidth and it grows larger everyday
  * Online cettificate Status Protocol (OCSP)
    * Provides real-time certificate status verification
    * Most used today
* Certificate stapling
  * reduces the CA's burden for verification of certificates
  * Web server request for verification and send that information to the browser requesting the certificate
  * Stapled certificates are often valid for 24 hours
* Ceritficate Authorities
  * Thirdparty CA - for a fee
  * Internal CA - to reduce cost for internal systems
  * Certificate Chaining - Internal CA trusted by thridparty CA 
    * For offline CAs - to protect sensitive root keys
* Ceritificate suibjects
  * Owner of the public key
  * Servers - SSH, file, email etc
  * Devices, routers, switchesm VPNs Acces points
  * ibndividuals - name , email addresses
  * Developers - for code signing
  * Certificate pinning
    * use to protect false security against fraud
    * expect a certificate that is not supposed to change
* certificate types
  * Root certificates - protect CA private keys
  * Wilcard certificate - cover entire domain
    * Use for load balancers
    * *.domain.com - www.domain.com,mail.domain.com 
      * not supported www.secure.domain.com
    * Types of verification :
      * Domain Validation - verifies domain ownership
      * Organizational Validation - verifies business name
      * Extended Validation - Requires extensive investigation
* Certificate Formats
  * DER - Distinguished encoding rules
    * Binary format
    * .DER, .CRT, .CER
  * PEM - privary enhanced Mail
    * ASCII text equivalents of DER vertificates
    * Convert DER to PEM with OpenSSL
    * .DER, .CRT
  * PFX - Personal Information Exchance
    * Binary FOrmat
    * Coomonly used by window systems
    * .PFX and .P12
    * P7B Fformat
      * ASCII text equivalent of PFX certificates
      * .P7B
  
[Back to Top](#comptia-security)
<br/><br/>

### Cryptanalytic Attacks
  * Brute force attacks
    * repeatedly guess keys until they hot the right one
  * Knowledge-based attacks
    * Frequency Analysis - Detects patterns in ciphertext
      * common letters
      * digraphs
      * plaintext - attach has an access to an unencrypted message
      * chosen plaintext - create an encryopted message of their choice
      * Birthday attack - if birthdays are used
  * Linmitations of encryption algorithms
    * some algorithn are faster than others
    * longers key are secure but more computing power
    * resuing the same keys in extended time


[Back to Top](#comptia-security)
<br/><br/>

### Cryptographic Applications
  * TLS and SSL
  * Information Rights management
    * for:
      * Enforcing data rights
      * provisioning access
      * implementing access control models
    * Digiital Rights Management (DRM) 
      * Provides the owners of intellectial property witht he techical means to prevent unauthorized use of their content through the use of encryption technology
  * Specialized use cases
    * Cryptographic hardware and low power
      * Smart cards
      * Satellites
    * Momomorphic Encryption
  * Blockchain
    * Distributed, immutable ledger


[Back to Top](#comptia-security)
<br/><br/>

## CompTIA Security+ (SY0-601) Cert Prep: 4 Identity and Access Management Design and Implementation
### Identification
  *  Identification, authentication, authorization and accounting
     *  3 steps
        1. identification - individual makes a claim of an identity - Username
        2. Authentication - Proof of identity - Password
        3. Authorization  - individual is allowed of the access requested - access control list
     * Accounting - Track user activity
  *  Usernames and access cards
     *  identitiation mechanism uniquely identify each use of a system
  *  Biometrics
     *  Identification base on one or more physical characteristics
     *  Identification and authentication
  
[Back to Top](#comptia-security)
<br/><br/>

### Authentication
  * Authentication Factors
    * Something you know 
      * Passwords
      * Password keys
    * Something you are
      * Biometrics
      * Finger print
    * Something you have
      * Physical possesion of a device or fob
      * smartphone
    * Other Attribute - weak and should only be used with the main authentication factors
      * somewhere you are
      * Something you can do
      * Somthing you exhibit
      * Someone you know
    * Possible errors:
      * False Acceptance
      * False Rejection
  * Multifactor Authentication
    * Combining something you know with somethig you have
    * Passwords and smartcards
    * Fingerprint and PIN
  * Something you have
    * OTP
      * Physical token
      * software token (software based)
    * OTP
      * HOTP - HMAC-based One-time password
        * shared secret and incrementing counter to generate pin
      * TOTP -  Time-based one-time password
        * Uses time with the shared secret to generate pin
      * Smartphone app instead of SMS it uses a push notification
      * Static backup codes
      * Smartcards
  * Password authentication protocols
    * PAP - password Authentication Protocol - no encryption
    * CHAP - Challenge handshake Authentication Protocol
      * uses shared key with out sending the shared key using a secure algorithm
      * MS-CHAP and MSCHAPv2 are insecure
  * Single sign-on and federation
    * Federated identity management sysyems share identity information to reduce the number of individual identities a use must have.
    * One-way trust - Domain 1 trust domain 2, but domain 2 does nto trust domain 1
    * Two-way Trust - Domain 1 and 2 trust each other
    * Transitive trust - trust relationshop transfer across domains
    * Non-transitive trust - trust relation ships do not transfer across domains
  * RADIUS and TACACS
    * Provides centralized approaches for authentication, authorization and accounting
    * RADUIS - Remote Access Dial-In User Service
      * first used in modem pools
      * Disadvantages:
        * Uses unreliable User Datagram Protocol (UDP)
        * Doesr not encrypt the entire authentication
    * TACACS - Terminal Access Controller Access Control Systems
      * TACACS+
        * Uses similarely to RADIUS
        * Uses Transmision control protocol (TCP)
        * Encrypts full authentication session
  * Kerberos and LDAP
    * Kerberos is one the core protocols for MS Active directory
    * Kerberos - Ticker-based authentication system that allows uses to authenticate to a centralized service and then use tickets to gain access to distributed services.
    * LDAP - Lightweight Directorty Access Protocol (LDAP) provides the means to query a centralized directory service such as Microsoft Active Directory
    * Kerberos uses port 88
    * LDAP uses port 389 unencrypted
    * Secure LDAP uses port 636
    * NTLM - hash base challenge response 
      * issues:
        * weal encryption
        * vulnerable to pass the hash
  * SAML
    * Secure Asserttion markup Language (SAML) allow single sign-on within a web browser across a variety of systems
    * ACtors:
      * End user - Principal
      * providing identity organization such as school - identity
      * the service you wanted to access - service provider
      * Benefits:
        * No need for multiple authentication thus True SSO experience for end users
        * No credential access (to be provided) for service provider
  * OAuth and OpenID Connect
    * OAuth is an authentication protocol and does not does authtication on its own
    * OpenID COnnect is an authentication protocol used for providing identity
  * Certificate-based authentication
    * Key-Based Authentication


[Back to Top](#comptia-security)
<br/><br/>

### Authorization
  * Understading authorization
    * Final step in access control process
    * Least Privilege - An individual should only have the minimum set of privileges necvessary to carry out their job functions.
      * Importance:
        * Lmits the potential damage from an insider attack
        * Restrict the abiity of an external attacker to leverage a compromised account.
    * Separation of Duties - performing any critical business function should require the involvement of two or more individuals.
    * Privilege Creep - Occurs when a user accumulates excess permissions after shitfting job responsibilities once or more times.
    * Account Review - limits privilege creep
  * Mandatory access controls (MAC)
    * Access control system where the operating system restricts authorizations based upon labels and users are not permitted to modify those authorizations.
    * SELinux provides MAC functionality
  * Discretionary access controls (DAC)
    * Access control system where permission may be set by the owner of files, computers and other resources.
    * Flexibility for users to share their resources
    * New TEchnology File System (NTFS) is an example of DAC
  * Access control list
    * Resource owners set DAC permissions through the use of access control list
  * Advance authorization concepts
    * Implicit Deny - any action which is not explicitly allowed must be denied
  * Database access control (RBAC)
    * in role-based access control systems, permissions are grouped together info Functionakl roles and users are assigned to those reles.
    * ABAC is an antributted - access control (ABAC) 
  
[Back to Top](#comptia-security)
<br/><br/>

### Account Management
  * Understanding acount management and privilege management
    * Account Management tasks
      * Implement least privilege - Users should only have the minimum set of permissions necessary for their job function
      * Implement separation of duties - Sesitive functions should require action by two separate users
      * Implement job rotation - Regularly move people between jobs to prevent fraud
        * Mandatory vacation - enforce periods of time when employees have no access to system.
      * Manage the account life cycle - 
        * Provisioning - account creation
        * Modify Roles - access
        * Account Reviews - Remove unnecessary access
        * Deprovisionng - terminated user
    * Account types
      * User Account - Has sstandard permissions and stancard monitoring
      * Privilege Account - has administrative rights and require strong controls.
        * Privilege accunts managements
        * should not be used for routine roles
      * Guest Account - Has limited permissions and temporary lifetimess
      * Shared account - or generic accounts - Reduces accountatbility and should not be used.
      * Service Account - provides access for internal server provesses
    * Account Policies
      * Group Policy Object (GPO) - Applies configuration settings to users and computers
    * Password Policies
      * Passsword remain the most common authentication mechanism
        * Password lenght requirement
        * Require uppervcadse, lowercase, digits and symbols for complexity
        * Password expiration policies
        * Lockout policies - lockout accounts after many incorrect login attemps. Disable unused accounts
      * Password recovery mechanism
        * Allow users to reset passwords on a self-service basis
        * Relieve burden on help desk
        * Improve user statisfaction with IT
    * Manage Roles
      * Roles - Groups permissions to allow shared security settings
      * Windows sezcurity group - implements role-based security
      * Benefits of Roles:
        * Role simplify account management
        * Administators may assign permissions to a new users by adding a role to the user.
        * Administrator may then remove permissions from departingh user by removing the role
        * Roles replace the need for shared account
      * Account Monitoring 
        * Inaccurate Permission - blocks work and/or violates least privilege
        * Account Audits
          * Pull listing of account permissions
          * Review permissions with managers
          * Make necessary adjustments
          * Prioritize review of users with job changes
        * Attestation - formal approval of users privileges
        * Unathorized use - illegitimate actions by legitimate users
        * Contionous account monitoring
          * Watch for suspicious activity
          * Alert administrators to anomalies
            * Access Policy violations
              * Impossible travel time logins
              * Unusual network location logins
              * Unsual time-of-day logins
              * Deviation from normal behavior
              * Deviation in volume of data transferred
          * Geotagging - tags with use location
          * Geofencing - Alerts to devices leaving defned boundaries
    * Privilleged Access Management
      * Privileged access management solutions sageguard administrative accounts
        * Password Vaulting - stores adminsitrative password and no one know the actual password of the account.
        * Command Proxying - Eliminates the need for direct server access
        * Monitoring - logs administrative user activity
        * Credential Mangement - rotates password and access keys
        * Emergency access workflow in case of emergency
    * Provisioning and Deprovisioning
      * Provisioning - After onboardingm, administrators create authentication credentials and grant appropriate authorization.
      * Deprovisioning - During the offboarding proicess, administrators disable accounts and revoke authorizations at the appropriate time.
        * Prompt termination is critiacal:
          * Prevents users from accessing resources without permission
          * Is espacially critical when a user leaves under adverse circumstances
        * Routine Workflow - disables accounts on a scheduled basis for planned departures.
        * Emergency workflow - immediately suspends access when user is unexpectedly terminated.
          * Incorrect timed account revocations:
            * May inform a user in advance pending the termination (may retaliate)
            * May allow a user access to resources after termination

[Back to Top](#comptia-security)
<br/><br/>


## CompTIA Security+ (SY0-601) Cert Prep: 5 Physical Security Design and Implementation
### Data Center Protection
  * Site and facility design
    * Datacenter - server location
    * server rooms - server locations
    * Media storage facilities
    * Evidence storage loacation
    * Wiring closets
    * Cable distribution / Cabling
    * Operation ceners and other sensitive locations
  * Data center environmental controls
    * Environment stable for electronic equipment
      * Air temperature to reduce too much heat
        * Expanded Envelope - between 64.4 F and 80.6 F
      * Humidity
        * High - leads to condensation that may damage electronic equipment
        * Low - leads to static electricity that may damage electronic equipment
        * Dew point range - 41.9 F and 50.0 F
    * HVAC systems
      * Heating, ventilating and Air conditioning
    * Hot aisle / Cold aisle approache makes cooling data centers more efficient
  * Data center environmental protection
    * Fire, flooding and electromagnetic interference
    * Fire detection and prevention
      * Deprive fire Oxygen, Heat and Fuel
      * Fire Extinguishers - Class C
      * Wet pipe - contain water in the pipes ready to deploy when fire strikes
      * Dry pipe do not contain water untile valve opens during fire alerm
      * Chemical systems deprive fire of oxygen
      * Fire detection systems
        * high temperature
        * smoke detectors
        * Incipient detectors
    * Flooding:
      * use moisture systems
    * Electromagnetic Interference
      * Generated by all electronic equiment
      * Interfere with normal operation of other equiment
      * Enables eavesdripping attacks / keystrokes fthat generated those signals
      * Faraday cages protect against electromagnetic interference
  * Physical access control
    * Protect perimeter
    * Locks - restrict entry through portals
    * Ciper locks - electronic locks with keypads
    * Biometric locks
    * card based locks
    * maintain accesslist carefully
    * Facility monitoring
      * Motion detection - acts a both deterrent and detective controls
      * Fences
      * Cages - for equipment
      * Barricade
      * Proper lighting
      * Industrial camouflage
  * Visitor Managemnent
    * Describe allowable visit purposes
    * Explain visit approval authority
    * Describe requirements for unescortred access
    * Explain role of visitor escorts
    * Logbook
    * ID badges
    * Cameras
  * Physical security personel
    * human security guards
    * revceptionist can also acts as security guards
    * uniform guards
    * Robot sentry
    * Two-person integrity - two people must enter sensitive areas together
    * Two-person Control - two people must jointly approva sensitive actions

[Back to Top](#comptia-security)
<br/><br/>

### Hardware and Data Security
  * Data Lifecycle
    * Create -> Store -> Use -> Share -> Archive -> Destroy
    * Data Sanitization Techniques
      * Clearing - overwrites sensitive information to frsutrate casual analysis
      * Purging - uses more afvance techniques might include encryption and degaussing
      * Destroy - shred/ burn
      * Paper document
        * Shredding 
        * Pulping - removing ink on paper
        * Burning
  * Hardware Physical security
    * Mobile devices are valuable and easy to steal.
    * Encryption to protect data in theft situations
    * USB datablockes
    * Laptop cable lock
    * Vaults
    * latop locking cabinet
    * Security tag
  
[Back to Top](#comptia-security)
<br/><br/>

### Business Continuity
  * Business continuity planning (BCP)
    * The set of controls designed to keep a busness running in the face of adversity whether natual or man-made.
    * Focus is Continuity Of Operations Planning (COOP)
    * suopports availability of CIA
    * PrioritizationQuestions:
      * What business activities will the plan cover?
      * What systems will it cover?
      * WHat controls will it consider?
    * Business Impact Assesment (BIA)
      * Identifies and prioritizes risks
      * includes annual cost of lost expected if it occurs
  * Business continuity controls
    * Redunduncy
    * Single Point of failure (SPOF) analysis 
      * identify and remove single point of failure
      * SPOF analysis continues until the cost of addressing risjs outweights the benefit.
    * IT Contingency Scenario Examples
      * Sudden bankruptcy of a key vendor
      * Insufficient storage ot compute capacity
      * Failure of untility service
      * Personel skills and team management, and succession planning
  * High availability and fault tolerance
    * Uses nultiple systems to protect agains service failure
    * Have operationally redundant systems
    * Fault Tolerance - makes a single system resilient against technical failures
    * Load balancing is related but not same goals. Load balancing dpreads demain across systems
    * Common points of failure:
      * Power supply - Reduntdant power supply
      * Storage - RAID is fault tolerance
      * Networking - multiple ISP and multiple NIC (NIC Teaming)

[Back to Top](#comptia-security)
<br/><br/>

### Disater Recovery
  * Disaster Reovery
    * Disaster recovery capabilities are dfisgined to restore a business to normal operations as quickly as possible. Disaster reveovery is a subset of business continuity.
      * Triggers:
        * Environmental Disaster
        * Man-made disaster
      * Initial Response
        * Contain the damage caused by the disaster
        * Recover whatever capabiltiies may be immediately restored
        * Include a variety of activities depending upon the nature of the disaster.
      * Disaster Communications
        * intial activation of the disaster recovery team
        * Regular status updates
        * Tactival communications
      * Disaster Recovery Metrics
        * The Receovery Time Objectives (RTO) is the maximum amount of time that it should take to recover a service after a disaster
        * The Recovery Point Objective (RPO) is the maximum time period from which data may be lost in the wake of the disaster.
        * The Recovery Service Level (RSL) is the percentage of a service that must be available during a disaster.
  * Backups
    * backups provide a data safety net
    * backup Media
      * Tape backups
      * disk to disk backups
      * Cloud backups
    * Full backups - include a complete copy of all data
      * Snapshots and images are type of full backups
    * Differential backups - include all data modified since the last full backup
    * Incremental backups - include all data modified since the last full or incremental backup
  * Restoring backups
  * Disaster Recovery Sites
    * Provide alternate data processing
    * Facility Types
      * Hot site 
        * FUlly operation datacenter
        * Stocked with equipment and data
        * Available at a moment's notice
        * Very expensive
      * Cold site
        * Empty data centers
        * Stocked with core equipments, network and environmental controls
        * Relativelyu inexpensive
        * Operationa in weeks or months
      * Warm site
        * Stocked with all necessary equipment and data
        * Not maintained in a parallel fasion
        * Similar in expense to hot sites
        * Available in hours or days
      * Offsite storage 
        * Georaphically distant
        * Site resiliency
        * Maniual transfer or site replication through SAN or VM
        * Online or offline backups
  * Testing BC/DR Plans
    * Goals
      * Validate the plan function correctly
      * Identify necessary plan updates
    * Disaster recovery test types
      * Read-through -a sk each team member to review their role in disaster receiovery process and provide feedback.
      * Walk-through - aka table top excercixse - gather the team together for a formal review of the disaster recovery plan.
      * Simulation - uses a practivec scenario to trest the disaster receovery plan.
      * Parallel test - activate the disaster recovery environment but do not swtich operationals there.
      * Full-interruption test - switch primary operations to the alternate environment and can be very disruptive to business.
  * After Action Reports (AAR)
    * create a formal record of the disaster recovery (DR) or business continuity (BC) event.
    * Contents:
      * Executive summary
      * back ground information leading to the event. 
      * Answer factual questions around the event. What? where? when? why?
      * Lessons Learned
      * Conclusion and next steps


[Back to Top](#comptia-security)
<br/><br/>

## CompTIA Security+ (SY0-601) Cert Prep: 6 Cloud Security Design and Implementation
### Cloud Computing
  * What is Cloud
    * Deliveriung computing respirces to a remote customer over a network
    * NIST Definition - A model for enabling ubiquitous, convinient, on-deman network access to a shared pool of configuratble computing resources (eg networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.
  * Cloud computing roles
    * Cloud service provider
    * Cloud customer
    * Cloud service partner - provides add-on services
    * Cloud access Security Broker (CASB) - Provides Identity Access Management (IAM) services.
  * Drivers for cloud computing
    * On-demand self-service - available when you need it
    * Scalability - increase capacity with demand
      * Horizontal scaling - adds more servers to the pool to meet increased demand
      * Vertical Scaling - adds more resources (for example, CPU or memory) to existing servers to meet increased demand.
    * Elasticity - Expanding and contracting quickly
    * Broad Network Access - Anytime, anywhere access
    * Measured Service - paying only for what you consume
  * Multitenant computing
    * Shared computing resources
    * Isolation - Users don't impact each other
    * Resource Pooling - CPU and memory shared among users
  * Cost-benefit analysis
    * is it worth it?
    * On-premise cost vs Cloud cost
      * Factors to scale:
        * Electricity
        * Data center facility rental, aquisition, maintenance
        * Trainign Cost
        * Consulting services
        * Staff time
      * Intangible benfits
        * Increase productivity and agility
        * Improved scalability and elasticity
        * Faster access to emerging technologies
        * Transition from captital to operational expenditures
        * Fun
  * Security service providers
    * Managed Service Providers (MSPs) offer information technology services to customers.
    * Service example:
      * Manage an entire security infrastructure
      * Monitoring system logs
      * Manage firewalls or networks
      * Perfoem identity and access management
    * Cloud Access Security Brokers (CASBs) add a third-party security layer to the interactions that users have with other cloud services.
      * Network-vbasedd CASB
        * Broker intercepts trafficv between users ans the cloud service, monitoring for security issues
        * Broker can block requests
      * API-based CASB
        * The broker queries the cloud service via API
        * Broker may not be able to block request depending upon API capabilities
  

[Back to Top](#comptia-security)
<br/><br/>

### Virtualization
  *  Virtualization
     * Host machines run on a physical hardware
     * Host machine provide services to several virtualized guest machines
     * The hypervisor tricks each guest into thinking it is running on dedicated hardware
     * Types of hypervisor:
       * Type 1 hypervisor - bare metal hyopervisor
       * Type 2 Hypervisor - runs on top of operating system
     * Virtualization Security:
       * Virtuakl machine isolation is critical
       * Each server must have access to only its own memory and storage
       * VM escape attacks attempt to break out of the guest environment
     * VM Sprawl - unused and unmaintained servers
  * Virtual Desktop Infrastruture (VDI)
    * Provides network-based access to a desktop computing environment
    * Application Virtualization - Streams applications to the user's desktop

[Back to Top](#comptia-security)
<br/><br/>

### Cloud Building Blocks
  * Cloud Compute Resources
    * High Availablity - Uses resources across zones
    * Instance Awareness - Reduces Vm Sprawl
  * Cloud storage
    * Block Storage - Allocates a large chunck of storage for access as a diskj volume managed by the operating system
    * Object Storage - Stores files as individual objects managed by the cloud service provider
    * Cloud storage Cost
      * Object storage is much less expensive than block storage ion the cloud
      * Onject storage cost are incured only when used, while block strorage must be allocated and paid in drivesized blocks.
      * Cloud Security
        * Set permisions properly 
        * Make use of encryption for sensitive data
        * Replicate data to multiple data centers
  * Cloud Networking
    * Virtual Private CLouds (VPCs) - like VLANs but on cloud
    * VPC Endpoint - Provide secure VPC interconnection
    * SOftware defind networking (SDN)
    * Software-defined Visibility (SDV)
  * Cloud databases
    * Build databases on virtualized servers
      * Requires spining up a server and installing/configuring databases
      * Resembles on-premuise operations
      * Requires customer management of servers and databases
    * Managed database service
      * Request database from cloud provider using platform of choice
      * Transfer maintenance responsibility to the cloud provider
      * Incurs addional costs
    * Cloud-native database platform
      * Allow use of relational database, key-value stores, graph databasem and other options.
      * Offers high degree of cloud optimization
      * places management burden on the provider
      * Requires retooling exisiting applications
  * Cloud orchestration
    * Automates cloud management
    * Infrastructure as Code - Manages cloud programmatically
  * Containers
    * Lighweight application virtualization
      * Contain application code and dependcies only
      * Run on containerization platforms
      * use the host's operating system

[Back to Top](#comptia-security)
<br/><br/>

### Cloud Reference Architecture


[Back to Top](#comptia-security)
<br/><br/>

### Cloud Security Controls



[Back to Top](#comptia-security)
<br/><br/>


[Back to Top](#comptia-security)
<br/><br/>