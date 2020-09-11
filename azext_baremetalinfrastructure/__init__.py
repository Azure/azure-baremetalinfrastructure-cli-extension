# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azext_baremetalinfrastructure._help  # pylint: disable=unused-import


class BareMetalInstanceCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_baremetalinfrastructure.custom#{}')
        super(BareMetalInstanceCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                      custom_command_type=custom_type)

    def load_command_table(self, args):
        from azext_baremetalinfrastructure.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_baremetalinfrastructure._params import load_arguments
        load_arguments(self, command)

COMMAND_LOADER_CLS = BareMetalInstanceCommandsLoader