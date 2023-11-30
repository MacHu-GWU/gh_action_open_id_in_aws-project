# -*- coding: utf-8 -*-

"""
Setup GitHub Action AWS permission for https://github.com/MacHu-GWU/cross_aws_account_iam_role-project.
It will REUSE the existing OIDC provider in AWS IAM.
"""

from boto_session_manager import BotoSesManager
from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

aws_profile = "bmt_app_dev_us_east_1"
bsm = BotoSesManager(profile_name=aws_profile)
role_name = "cross-aws-account-iam-role-github-oidc"

setup_github_action_open_id_connection_in_aws(
    aws_profile=aws_profile,
    stack_name="cross-aws-account-iam-role-github-oidc",
    github_org="MacHu-GWU",
    github_repo="cross_aws_account_iam_role-project",
    role_name=role_name,
    oidc_provider_arn=f"arn:aws:iam::{bsm.aws_account_id}:oidc-provider/token.actions.githubusercontent.com",
)
