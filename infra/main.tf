terraform {
  backend "s3" {}
}

provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

module "s3_buckets" {
  source       = "./s3_buckets"
  project_name = var.project_name
  aws_region   = var.aws_region
}

module "dynamodb" {
  source      = "./dynamodb"
  environment = var.environment
}

module "parallel_loader" {
  source = "./parallel_loader"
  aws_account_id = data.aws_caller_identity.current.account_id
  datastore_db_arn = module.dynamodb.database_arn
  s3_bucket_arn = module.s3_buckets.s3_bucket_arn
  loader_queue_arn = module.parallel_loader_queue.loader_queue_arn
}

module "parallel_loader_queue" {
  source = "./loader_queue"
}