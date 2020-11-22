output "database_arn" {
  value = aws_dynamodb_table.dynamodb_table.arn
}

output "database_name" {
  value = aws_dynamodb_table.dynamodb_table.name
}
