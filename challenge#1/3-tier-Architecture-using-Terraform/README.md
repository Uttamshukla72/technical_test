# Challange-1

3 tier environement consist of frontend layer, backend layer and data store(database)

# Resources to create

 1. VPC
 2. Internet gateway
 3. 4 Subnets (2 public and 2 private in 2 AZ's)
 4. Create two Route tables (public for internet and private for the traffic through NAT Gateway)
 5. Create NAT Gateway
 6. ELB (Internet and the Internal Load balancer)
 7. Auto Scaling group
 8. Bastion Host (to access to private instance)

# implementation tools- Terraform

Terraform has been used to create immutable infrastructure for tier-3 environment.
