# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import resource_group_name_type


def load_arguments(self, _):
    with self.argument_context('baremetalinstance') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('instance_name', options_list=['--instance-name', '-n'], help="The name of the BareMetal instance", id_part='name')
