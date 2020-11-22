variable "function_name" {
  type    = string
  default = "dynamo-parallel-loader"
}

variable "project_name" {
  type    = string
  default = "data-loader"
}

variable "datastore_db_arn" {
  type = string
}

variable "aws_account_id" {
  type = string
}
variable "s3_bucket_arn" {
  type = string
}

variable "loader_queue_arn" {
  type = string
}