# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.util import empty_on_404
from ._client_factory import cf_azurebaremetalinstance_groups
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):
    custom_tmpl = 'azext_baremetalinfrastructure.custom#{}'
    custom_type = CliCommandType(operations_tmpl=custom_tmpl)
    with self.command_group('baremetalinstance', client_factory=cf_azurebaremetalinstance_groups) as g:
        g.custom_command('list', 'list_azurebaremetalinstance')
        g.custom_command('show', 'show_azurebaremetalinstance', exception_handler=empty_on_404)
        g.custom_command('restart', 'restart_azurebaremetalinstance')
        g.custom_command('start', 'start_azurebaremetalinstance')
        g.custom_command('shutdown', 'shutdown_azurebaremetalinstance')
        g.generic_update_command('update', getter_name='show_azurebaremetalinstance', setter_name='update_azurebaremetalinstance',
                                 command_type=custom_type, supports_no_wait=True)
        g.custom_command('delete', 'delete_azurebaremetalinstance')
