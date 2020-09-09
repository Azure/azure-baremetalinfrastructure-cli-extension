# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def _azurebaremetal_instance_client_factory(cli_ctx, *_):
    from azext_baremetalinfrastructure.modules_sdk import BareMetalInfrastructurelManagementClient
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, BareMetalManagementClient)

def cf_azurebaremetalinstance_groups(cli_ctx, *_):
    return _azurebaremetal_instance_client_factory(cli_ctx).baremetal_instances