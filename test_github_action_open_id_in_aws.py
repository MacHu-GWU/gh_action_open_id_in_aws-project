# -*- coding: utf-8 -*-

"""
This script tests the AWS permission in GitHub action without showing the
AWS Account id.
"""

import boto3

# print the current AWS principal ARN (AWS account id masked)
res = boto3.client("sts").get_caller_identity()
parts = res["Arn"].split(":")
parts[4] = parts[4][:2] + "********" + parts[4][-2:]
arn = ":".join(parts)
print(arn)
