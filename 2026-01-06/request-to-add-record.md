# DNS Records Required for EC2 Hosted Website

## Purpose
Point the custom domain to the EC2 instance hosting the website using a static Elastic IP.

## Elastic IP Details

 Domain Name   : [NEW_DOMAIN]         
 Record Type   : A
 Value (Elastic IP / CNAME)     : 3.215.189.47 
 TTL (seconds)  : 300
 Notes         : Points directly to the EC2 instance                


## Instructions for DNS Update

1. Log in to the DNS provider managing the domain.
2. Navigate to **DNS Records / Zone File** management.
3. Add an **A record** for `[NEW_DOMAIN]` with the allocated Elastic IP 3.215.189.47
4. Set **TTL** to 300 seconds.
5. Save the changes.

Once these records are added, the domain will point to the EC2 instance and the website will be accessible.
