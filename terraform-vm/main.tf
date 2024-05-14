terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}

module "example_instance" {
  source = "./modules"

  instance_ami    = "ami-0bb84b8ffd87024d8"  # Your AMI ID
  instance_type   = "t2.micro"               # Your instance type
}
