# -*- coding: utf-8 -*-

"""
This script
This script creates an OpenID Connect (OIDC) provider for GitHub Actions in AWS.
The OIDC provider enables federated authentication between GitHub Actions workflows
and AWS without storing long-lived credentials.

The script only sets up the OIDC provider connection and does not create any IAM roles.
This approach lets you reuse the same OIDC provider across multiple IAM roles for
different GitHub repositories, improving security and maintainability.
"""

from boto_session_manager import BotoSesManager
from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

aws_profile = "bmt_app_devops_us_east_1"
project_name = "gh_action_open_id_in_aws"
project_name_slug = project_name.replace("_", "-")
bsm = BotoSesManager(profile_name=aws_profile)
deploy_stack_response = setup_github_action_open_id_connection_in_aws(
    aws_profile=aws_profile,
    stack_name=f"{project_name_slug}-test-role",
    # This time we reuse the existing OIDC provider in AWS IAM.
    oidc_provider_arn=f"arn:aws:iam::{bsm.aws_account_id}:oidc-provider/token.actions.githubusercontent.com",
    # We allow all branches in the repo to assume the role.
    github_repo_patterns=["repo:MacHu-GWU/gh_action_open_id_in_aws-project:*"],
    role_name=f"{project_name}_test_role",
    tags={
        "tech:project_name": project_name,
    },
    skip_prompt=True,
    verbose=True,
)

# NOTE: this script only create the IAM Role without any permissions. You need to
# add the permissions yourself.
