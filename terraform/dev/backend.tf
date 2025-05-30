terraform {
  backend "s3" {
    bucket = "terraformbackend-theguardian"
    key    = "dev/terraform.tfstate"
    region = "eu-central-1"
    use_lockfile = true
  }
}