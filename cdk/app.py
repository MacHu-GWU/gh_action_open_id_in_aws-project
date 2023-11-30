# -*- coding: utf-8 -*-

import aws_cdk as cdk
from gh_action_open_id_in_aws.cf import Stack

app = cdk.App()
stack = Stack(app, "gh-action-open-id-in-aws")
app.synth()
