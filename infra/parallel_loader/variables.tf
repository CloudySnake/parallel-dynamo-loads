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