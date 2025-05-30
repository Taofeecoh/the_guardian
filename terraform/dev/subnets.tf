
# Public subnet
resource "aws_subnet" "public_subnet1" {
  vpc_id     = aws_vpc.theguardian.id
  cidr_block = "104.20.2.0/24"

  tags = {
    Name = "public_subnet1"
  }
}


# Private subnet
resource "aws_subnet" "private_subnet1" {
  vpc_id     = aws_vpc.theguardian.id
  cidr_block = "104.20.4.0/24"

  tags = {
    Name = "private_subnet1"
  }
}

