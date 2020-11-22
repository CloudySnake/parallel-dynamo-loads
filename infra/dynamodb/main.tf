resource "aws_dynamodb_table" "dynamodb_table" {

  billing_mode = "PAY_PER_REQUEST"

  hash_key = "PK"
  name     = "datastore"

  attribute {
    name = "PK"
    type = "S"
  }

  stream_enabled = false

  tags = {
    Environment = var.environment
  }

  point_in_time_recovery {
    enabled = false
  }
}
