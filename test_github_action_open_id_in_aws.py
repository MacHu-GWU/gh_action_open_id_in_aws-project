# -*- coding: utf-8 -*-

import boto3

res = boto3.client("sts").get_caller_identity()
parts = res["Arn"].split(":")
parts[4] = parts[4][:2] + "********" + parts[4][-2:]
arn = ":".join(parts)
print(arn)
