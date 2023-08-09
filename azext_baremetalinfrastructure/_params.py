# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.parameters import (
    resource_group_name_type,
    get_three_state_flag
)

def load_arguments(self, _):
    with self.argument_context('baremetalinstance') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('instance_name', options_list=[
                   '--instance-name', '-n'], help="The name of the BareMetalInstance", id_part='name')

    with self.argument_context('baremetalinstance restart') as c:
        c.argument('force', options_list=[
                   '--force', '-f'], arg_type=get_three_state_flag(), help="Force restart option")