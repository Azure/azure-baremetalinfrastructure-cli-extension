# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class AzureBareMetalInstance(Resource):
    """AzureBareMetal instance info on Azure (ARM properties and AzureBareMetal
    properties).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :ivar tags: Resource tags
    :vartype tags: dict[str, str]
    :param hardware_profile: Specifies the hardware settings for the
     AzureBareMetal instance.
    :type hardware_profile:
     ~microsoft.baremetalinfrastructure.models.HardwareProfile
    :param storage_profile: Specifies the storage settings for the
     AzureBareMetal instance disks.
    :type storage_profile:
     ~microsoft.baremetalinfrastructure.models.StorageProfile
    :param os_profile: Specifies the operating system settings for the
     AzureBareMetal instance.
    :type os_profile: ~microsoft.baremetalinfrastructure.models.OSProfile
    :param network_profile: Specifies the network settings for the
     AzureBareMetal instance.
    :type network_profile:
     ~microsoft.baremetalinfrastructure.models.NetworkProfile
    :ivar azure_bare_metal_instance_id: Specifies the AzureBareMetal instance
     unique ID.
    :vartype azure_bare_metal_instance_id: str
    :ivar power_state: Resource power state. Possible values include:
     'starting', 'started', 'stopping', 'stopped', 'restarting', 'unknown'
    :vartype power_state: str or
     ~microsoft.baremetalinfrastructure.models.AzureBareMetalInstancePowerStateEnum
    :ivar proximity_placement_group: Resource proximity placement group
    :vartype proximity_placement_group: str
    :ivar hw_revision: Hardware revision of an AzureBareMetal instance
    :vartype hw_revision: str
    :param partner_node_id: ARM ID of another AzureBareMetalInstance that will
     share a network with this AzureBareMetalInstance
    :type partner_node_id: str
    :ivar provisioning_state: State of provisioning of the
     AzureBareMetalInstance. Possible values include: 'Accepted', 'Creating',
     'Updating', 'Failed', 'Succeeded', 'Deleting', 'Migrating'
    :vartype provisioning_state: str or
     ~microsoft.baremetalinfrastructure.models.AzureBareMetalProvisioningStatesEnum
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'azure_bare_metal_instance_id': {'readonly': True},
        'power_state': {'readonly': True},
        'proximity_placement_group': {'readonly': True},
        'hw_revision': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'hardware_profile': {'key': 'properties.hardwareProfile', 'type': 'HardwareProfile'},
        'storage_profile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'os_profile': {'key': 'properties.osProfile', 'type': 'OSProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'azure_bare_metal_instance_id': {'key': 'properties.azureBareMetalInstanceId', 'type': 'str'},
        'power_state': {'key': 'properties.powerState', 'type': 'str'},
        'proximity_placement_group': {'key': 'properties.proximityPlacementGroup', 'type': 'str'},
        'hw_revision': {'key': 'properties.hwRevision', 'type': 'str'},
        'partner_node_id': {'key': 'properties.partnerNodeId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, hardware_profile=None, storage_profile=None, os_profile=None, network_profile=None, partner_node_id: str=None, **kwargs) -> None:
        super(AzureBareMetalInstance, self).__init__(location=location, **kwargs)
        self.hardware_profile = hardware_profile
        self.storage_profile = storage_profile
        self.os_profile = os_profile
        self.network_profile = network_profile
        self.azure_bare_metal_instance_id = None
        self.power_state = None
        self.proximity_placement_group = None
        self.hw_revision = None
        self.partner_node_id = partner_node_id
        self.provisioning_state = None