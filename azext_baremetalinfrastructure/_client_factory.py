# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def _baremetal_instance_client_factory(cli_ctx, subscription_id=None):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_baremetalinfrastructure.modules_sdk import BareMetalInfrastructureClient
    return get_mgmt_service_client(cli_ctx=cli_ctx, client_or_resource_type=BareMetalInfrastructureClient, subscription_id=subscription_id, base_url_bound=False, credential= None)

def cf_baremetalinstance_groups(cli_ctx, *_):
    return _baremetal_instance_client_factory(cli_ctx=cli_ctx).azure_bare_metal_instances
