resource "aws_s3_bucket" "data_store" {
  bucket = "hc-data-store"
  acl    = "private"
}
