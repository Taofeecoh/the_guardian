resource "aws_instance" "theguardian_privateserver" {
  ami                    = "ami-04fcbaa2a7d55c34f"
  instance_type          = "t2.micro"
  key_name               = "theguardian"
  subnet_id              = aws_subnet.private_subnet1.id
  vpc_security_group_ids = [aws_security_group.private_SG.id]
  tags = {
    Name = "theguardian_privateserver"
  }
}