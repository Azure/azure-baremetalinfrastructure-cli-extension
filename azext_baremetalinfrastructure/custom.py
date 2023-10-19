# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-many-lines

def show_baremetalinstance(client, resource_group_name, instance_name):
    return client.get(resource_group_name, instance_name)

def list_baremetalinstance(client, resource_group_name=None):
    if resource_group_name is None:
        return client.list_by_subscription()
    return client.list(resource_group_name)

def restart_baremetalinstance(client, resource_group_name, instance_name, force=False):
    # The restart baremetalinstance REST API is a POST with a body.
    # The HaaS RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {}
    force_parameter = { "forceState": "active" if force else "inactive" }
    return client.begin_restart(resource_group_name, instance_name, force_parameter, headers=custom_header)

def start_baremetalinstance(client, resource_group_name, instance_name):
    # The start baremetalinstance REST API is a POST with no body.
    # The HaaS RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {}
    custom_header['Content-Type'] = 'application/json; charset=utf-8'
    return client.begin_start(resource_group_name, instance_name, headers=custom_header)

def shutdown_baremetalinstance(client, resource_group_name, instance_name):
    # The shutdown baremetalinstance REST API is a POST with no body.
    # The HaaS RP API requires the Content-Type to be set.
    # Swagger does not add the Content-Type in the header if there is no body.
    # We need to add a custom header to force the API call to add the Content-Type.
    custom_header = {}
    custom_header['Content-Type'] = 'application/json; charset=utf-8'
    return client.begin_shutdown(resource_group_name, instance_name, headers=custom_header)

def update_baremetalinstance(client, resource_group_name, instance_name, **kwargs):
    return client.update(resource_group_name, instance_name, kwargs['parameters'].tags)

def delete_baremetalinstance(client, resource_group_name, instance_name):
    return client.begin_delete(resource_group_name, instance_name)