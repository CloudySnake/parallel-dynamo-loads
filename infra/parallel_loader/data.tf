data "aws_iam_policy_document" "assume_role_lambda" {
  statement {
    effect = "Allow"
    actions = [
    "sts:AssumeRole"]

    principals {
      identifiers = [
      "lambda.amazonaws.com"]
      type = "Service"
    }
  }
}

data "aws_iam_policy_document" "parallel_loader_access_policy" {

  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:CreateLogGroup",
      "logs:DescribeLogStreams",
      "logs:PutLogEvents"
    ]
    resources = [
    "arn:aws:logs:eu-west-1:${var.aws_account_id}:log-group:/aws/lambda/data-loader-*:*"]
  }

  statement {
    effect = "Allow"
    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:GetObjectTagging",
      "s3:PutObjectTagging",
      "s3:DeleteObject"
    ]
    resources = [
      "${var.s3_bucket_arn}/*"
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "dynamodb:GetItem",
      "dynamodb:PutItem",
      "dynamodb:Query",
      "dynamodb:UpdateItem",
      "dynamodb:DescribeTable",
      "dynamodb:BatchWriteItem"
    ]
    resources = [
      var.datastore_db_arn,
      "${var.datastore_db_arn}/*",
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "sqs:*"
    ]
    resources = [
      var.loader_queue_arn,
    ]
  }

}
