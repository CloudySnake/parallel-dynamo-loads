locals {
  service_name = "dynamo-parallel-loader"
  repo_name    = "parallel-dynamo-loads"
}

resource "aws_sqs_queue" "dynamo_loader_queue" {
  name                      = local.service_name
  message_retention_seconds = 604800
  visibility_timeout_seconds = 300
}

resource "aws_sns_topic" "dynamo_loader_topic" {
  name = "${local.service_name}-topic"
}

resource "aws_sns_topic_subscription" "channel_to_queue" {
  endpoint  = aws_sqs_queue.dynamo_loader_queue.arn
  protocol  = "sqs"
  topic_arn = aws_sns_topic.dynamo_loader_topic.arn
}
