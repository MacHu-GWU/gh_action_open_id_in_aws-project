# -*- coding: utf-8 -*-


"""
Setup GitHub Action Open ID Connection in AWS for the given AWS account.
It will create a new OIDC provider and an IAM role for GitHub action to assume
in AWS IAM. Note that the IAM role won't have any permission.

This is useful when it is the first time you set up GitHub Action Open ID Connection
for the given AWS account. Since you may have multiple GitHub repositories,
you should intentionally leave this IAM role without any permission. Then, you can
reuse the OIDC provider to create more roles for each GitHub repository.
"""

from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

for aws_profile in [
    "bmt_app_devops_us_east_1",
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
