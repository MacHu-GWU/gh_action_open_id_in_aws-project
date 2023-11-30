# -*- coding: utf-8 -*-

from gh_action_open_id_in_aws.impl import setup_github_action_open_id_connection_in_aws

setup_github_action_open_id_connection_in_aws(
    aws_profile="bmt_app_dev_us_east_1",
    stack_name="gh-action-open-id-in-aws",
    github_org="MacHu-GWU",
    github_repo="gh_action_open_id_in_aws-project",
    role_name="gh_action_open_id_in_aws",
)
