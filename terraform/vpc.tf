resource "aws_vpc" "theguardian" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "the-guardian"
    Environment = "development"
    Team = "engineering"
    Used_for = "everything_nigerian_news"
 }
}
