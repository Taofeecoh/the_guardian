terraform {
  backend "s3" {
    bucket = "terraform-theguardian"
    key    = "dev/terraform.tfstate"
    region = "eu-central-1"
  }
}