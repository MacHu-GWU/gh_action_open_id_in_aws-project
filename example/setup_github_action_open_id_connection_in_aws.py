# -*- coding: utf-8 -*-

"""
Setup GitHub Action Open ID Connection in AWS for "bmt_app_dev_us_east_1" AWS account.
It will create the OIDC provider in AWS IAM.
"""

from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

for aws_profile in [
    "bmt_app_dev_us_east_1",
    "bmt_app_test_us_east_1",
    "bmt_app_prod_us_east_1",
]:
    setup_github_action_open_id_connection_in_aws(
        aws_profile=aws_profile,
        stack_name="gh-action-open-id-in-aws",
        github_org="MacHu-GWU",
        github_repo="gh_action_open_id_in_aws-project",
        role_name="gh_action_open_id_in_aws",
    )
