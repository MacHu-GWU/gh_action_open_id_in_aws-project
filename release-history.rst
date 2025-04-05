.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.0.1 (205-04-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**💥Breaking Changes**

- Rework the ``setup_github_action_open_id_connection_in_aws`` function and update the underlying AWS CloudFormation template.
- Allow to fully control the ``github_repo_patterns``.
- Allow to create OIDC provider only or IAM role only.

**Miscellaneous**

- Rework documentation.


0.1.3 (2023-12-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- fix inaccurate doc string of the ``oidc_provider_arn`` parameter in the ``setup_github_action_open_id_connection_in_aws`` function.
- improve document.


0.1.2 (2023-11-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- Add ``tech:cloudformation_stack`` AWS resource tag.

**Bugfixes**

- Removed the unused ``fire`` Python dependency.


0.1.1 (2023-11-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add the ``setup_github_action_open_id_connection_in_aws`` function to public API.
