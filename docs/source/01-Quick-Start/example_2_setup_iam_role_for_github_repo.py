# -*- coding: utf-8 -*-

"""
This script reuse the OIDC provider created in the first example to create an IAM role
that can be assumed by GitHub Actions workflows in the specified repository.
"""

from boto_session_manager import BotoSesManager
from aws_cloudformation.api import remove_stack
from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

aws_profile = "bmt_app_devops_us_east_1"
project_name = "gh_action_open_id_in_aws"
project_name_slug = project_name.replace("_", "-")
stack_name = f"{project_name_slug}-test-role"
bsm = BotoSesManager(profile_name=aws_profile)


def setup():
    """
    NOTE: this script only create the IAM Role without any permissions. You need to
    add the permissions yourself.
    """
    deploy_stack_response = setup_github_action_open_id_connection_in_aws(
        aws_profile=aws_profile,
        stack_name=stack_name,
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


def teardown():
    remove_stack(
        bsm=bsm,
        stack_name=stack_name,
        skip_prompt=True,
        verbose=True,
    )


setup()
# teardown()
