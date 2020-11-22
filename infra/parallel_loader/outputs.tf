resource "aws_ssm_parameter" "lambda_iam_role" {
  name      = "/${var.project_name}/${var.function_name}/lambda_iam_role/arn"
  type      = "String"
  value     = aws_iam_role.lambda_iam_role.arn
  overwrite = true
}
