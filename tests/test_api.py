# -*- coding: utf-8 -*-

from gh_action_open_id_in_aws import api


def test():
    _ = api


if __name__ == "__main__":
    from gh_action_open_id_in_aws.tests import run_cov_test

    run_cov_test(__file__, "gh_action_open_id_in_aws.api", preview=False)
