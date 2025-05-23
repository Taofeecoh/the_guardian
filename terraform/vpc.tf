resource "aws_vpc" "theguardian" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    name = "the-guardian"
    environment = "development"
    team = "engineering"
    used_for = "everything_nigerian_news"
 }
}