
# Public subnet stacks
resource "aws_subnet" "public_subnet1" {
  vpc_id     = aws_vpc.theguardian.id
  cidr_block = "104.20.2.0/24"

  tags = {
    Name = "public_subnet1"
  }
}

# Security group
resource "aws_security_group" "public_SG" {
  vpc_id = aws_vpc.theguardian.id
  name   = "public_SG"

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "public_SG"
    Description = "allows ingress from / egress to anywhere"
  }
}

# Private subnet stack
resource "aws_subnet" "private_subnet1" {
  vpc_id     = aws_vpc.theguardian.id
  cidr_block = "104.20.4.0/24"

  tags = {
    Name = "private_subnet1"
  }
}

resource "aws_security_group" "private_SG" {
  vpc_id = aws_vpc.theguardian.id
  name   = "private_SG"

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "public_SG"
    Description = "allows ingress from / egress to anywhere"
  }
}
