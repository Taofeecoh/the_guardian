# Public security group
resource "aws_security_group" "public_SG" {
  vpc_id      = aws_vpc.theguardian.id
  name        = "public_SG"
  description = "allows ingress from any IP via TCP: SSH and egress to anywhere"

  tags = {
    Name        = "public_SG"
    Description = "allows ingress from any IP via TCP: SSH and egress to anywhere"
  }
}

# Inbound rule1
resource "aws_vpc_security_group_ingress_rule" "public_SG_ingress_1" {
  security_group_id = aws_security_group.public_SG.id

  cidr_ipv4   = "0.0.0.0/0"
  from_port   = 22
  ip_protocol = "tcp"
  to_port     = 22
}

# Inbound rule2
resource "aws_vpc_security_group_ingress_rule" "public_SG_ingress_2" {
  security_group_id = aws_security_group.public_SG.id

  cidr_ipv4   = "0.0.0.0/0"
  from_port   = 443
  ip_protocol = "tcp"
  to_port     = 443
}

# Outbound rule1
resource "aws_vpc_security_group_egress_rule" "public_SG_egress_1" {
  security_group_id = aws_security_group.public_SG.id

  cidr_ipv4   = "0.0.0.0/0"
  ip_protocol = "-1"
}


# Private security group
resource "aws_security_group" "private_SG" {
  vpc_id = aws_vpc.theguardian.id
  name   = "private_SG"
  tags = {
    Name        = "private_SG"
    Description = "allows ingress from/egress to IP on same CIDR block"
  }
}

# Inbound rule1
resource "aws_vpc_security_group_ingress_rule" "private_SG_ingress_1" {
  security_group_id = aws_security_group.private_SG.id

  cidr_ipv4   = "104.20.0.0/16"
  from_port   = 22
  ip_protocol = "tcp"
  to_port     = 22
}

# Outbound rule1
resource "aws_vpc_security_group_egress_rule" "private_SG_egress_1" {
  security_group_id = aws_security_group.private_SG.id

  cidr_ipv4   = "104.20.00/16"
  ip_protocol = "tcp"
  from_port   = 22
  to_port     = 22
}