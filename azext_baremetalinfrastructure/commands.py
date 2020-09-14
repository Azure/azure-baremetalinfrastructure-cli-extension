# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.util import empty_on_404
from ._client_factory import cf_baremetalinstance_groups
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):
    custom_tmpl = 'azext_baremetalinfrastructure.custom#{}'
    custom_type = CliCommandType(operations_tmpl=custom_tmpl)
    with self.command_group('baremetalinstance', client_factory=cf_baremetalinstance_groups) as g:
        g.custom_command('list', 'list_baremetalinstance')
        g.custom_command('show', 'show_baremetalinstance', exception_handler=empty_on_404)
        g.custom_command('restart', 'restart_baremetalinstance')
        g.custom_command('start', 'start_baremetalinstance')
        g.custom_command('shutdown', 'shutdown_baremetalinstance')
        g.generic_update_command('update', getter_name='show_baremetalinstance', setter_name='update_baremetalinstance',
                                 command_type=custom_type, supports_no_wait=True)
        g.custom_command('delete', 'delete_baremetalinstance')
