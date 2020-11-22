resource "aws_iam_role" "lambda_iam_role" {
  force_detach_policies = true
  name                  = "${var.function_name}-role-lambda"
  assume_role_policy    = data.aws_iam_policy_document.assume_role_lambda.json
  path                  = "/parallel-loader/${var.function_name}/"
}

resource "aws_iam_policy" "inline-policy" {
  name   = "${var.function_name}-pol"
  policy = data.aws_iam_policy_document.parallel_loader_access_policy.json
}

resource "aws_iam_role_policy_attachment" "lambda_iam_to_policy_attachment" {
  policy_arn = aws_iam_policy.inline-policy.arn
  role       = aws_iam_role.lambda_iam_role.id
}
