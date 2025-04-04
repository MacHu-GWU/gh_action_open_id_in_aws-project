# -*- coding: utf-8 -*-

"""
This script creates an OpenID Connect (OIDC) provider for GitHub Actions in AWS.
The OIDC provider enables federated authentication between GitHub Actions workflows
and AWS without storing long-lived credentials.

The script only sets up the OIDC provider connection and does not create any IAM roles.
This approach lets you reuse the same OIDC provider across multiple IAM roles for
different GitHub repositories, improving security and maintainability.
"""

from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

# List your local AWS CLI profiles here, with each profile corresponding to one AWS account
# You can add multiple profiles to set up several AWS accounts in a single batch operation
aws_profile_list = [
    "bmt_app_devops_us_east_1",
    "bmt_app_dev_us_east_1",
    # "bmt_app_test_us_east_1",
    # "bmt_app_prod_us_east_1",
]
stack_name = "github-action-oidc-provider"

for aws_profile in aws_profile_list:
    deploy_stack_response = setup_github_action_open_id_connection_in_aws(
        aws_profile=aws_profile,
        stack_name=stack_name,
        github_repo_patterns=[],  # We only create OIDC provider, this value is only used for IAM role, so we can set it to empty list.
        role_name="",  # We only create OIDC provider, so no need to create IAM role for GitHub action to assume in AWS IAM.
        tags={
            "tech:project_name": "gh_action_open_id_in_aws",
            "tech:description": "The GitHub Action OIDC provider created in this stack will be reused in many IAM roles. So do not delete it.",
        },
        skip_prompt=True,
        verbose=True,
    )
