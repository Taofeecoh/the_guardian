resource "aws_s3_bucket" "terraform-theguardian" {
  bucket = "terraform-theguardian"

  tags = {
    Name        = "terraform-theguardian"
    Environment = "Dev"
    Project     = "the guardian"
  }
}

resource "aws_s3_bucket_versioning" "versioning-terraform-tg" {
  bucket = aws_s3_bucket.terraform-theguardian.id
  versioning_configuration {
    status = "Enabled"
  }
}