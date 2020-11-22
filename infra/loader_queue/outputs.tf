resource "aws_ssm_parameter" "sqs_queue_arn" {
  name  = "/${local.repo_name}/${local.service_name}/sqs_queue/arn"
  type  = "String"
  value = aws_sqs_queue.dynamo_loader_queue.arn
}

output "loader_queue_arn" {
  value = aws_sqs_queue.dynamo_loader_queue.arn
}