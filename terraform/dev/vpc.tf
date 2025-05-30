resource "aws_vpc" "theguardian" {
  cidr_block = "104.20.0.0/16"

  tags = {
    Name        = "the-guardian"
    Environment = "development"
    Team        = "engineering"
    Used_for    = "everything_nigerian_news"
    Created_by  = "IAM_user_admin"
  }
}

# Internet gateway
resource "aws_internet_gateway" "theguardian_gw" {
  vpc_id = aws_vpc.theguardian.id

  tags = {
    Name = "theguardian_gw"
  }
}