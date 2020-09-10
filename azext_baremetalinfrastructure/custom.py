# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-many-lines


def show_azurebaremetalinstance(client, resource_group_name, instance_name):
    return client.get(resource_group_name, instance_name)


def list_azurebaremetalinstance(client, resource_group_name=None):
    if resource_group_name is None:
        return client.list()
    return client.list_by_resource_group(resource_group_name)

def restart_azurebaremetalinstance(client, resource_group_name, instance_name):
    # The restart azurebaremetalinstance REST API is a POST with no body.
    # The HaaS RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {}
    custom_header['Content-Type'] = 'application/json; charset=utf-8'
    return client.restart(resource_group_name, instance_name, custom_header)

def start_azurebaremetalinstance(client, resource_group_name, instance_name):
    # The start azurebaremetalinstance REST API is a POST with no body.
    # The HaaS RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {}
    custom_header['Content-Type'] = 'application/json; charset=utf-8'
    return client.start(resource_group_name, instance_name, custom_header)

def shutdown_azurebaremetalinstance(client, resource_group_name, instance_name):
    # The shutdown azurebaremetalinstance REST API is a POST with no body.
    # The HaaS RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {}
    custom_header['Content-Type'] = 'application/json; charset=utf-8'
    return client.shutdown(resource_group_name, instance_name, custom_header)

def update_azurebaremetalinstance(client, resource_group_name, instance_name, **kwargs):
    return client.update(resource_group_name, instance_name, kwargs['parameters'].tags)

def delete_azurebaremetalinstance(client, resource_group_name, instance_name):
    return client.delete(resource_group_name, instance_name)