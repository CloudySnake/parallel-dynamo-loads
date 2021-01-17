bucket         = "holyport-consulting-sandbox-terraform-state"
dynamodb_table = "terraform-lock"
encrypt        = true
key            = "parallel-dynamo-loads/terraform.tfstate"
region         = "eu-west-2"