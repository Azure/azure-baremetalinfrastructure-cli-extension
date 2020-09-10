# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.help_files import helps


helps['azurebaremetalinstance'] = """
    type: group
    short-summary: (PREVIEW) Manage Azure Bare Metal Instance.
    """

helps['azurebaremetalinstance show'] = """
    type: command
    short-summary: Get the details of an Azure Bare Metal Instance.
    """

helps['azurebaremetalinstance list'] = """
    type: command
    short-summary: List Azure Bare Metal Instances.
"""

helps['azurebaremetalinstance restart'] = """
    type: command
    short-summary: Restart an Azure Bare Metal Instance.
"""

helps['azurebaremetalinstance start'] = """
    type: command
    short-summary: Start an Azure Bare Metal Instance.
"""

helps['azurebaremetalinstance shutdown'] = """
    type: command
    short-summary: Shutdown an Azure Bare Metal Instance.
"""

helps['azurebaremetalinstance update'] = """
    type: command
    short-summary: Update the tags field of an Azure Bare Metal Instance.
"""

helps['azurebaremetalinstance delete'] = """
    type: command
    short-summary: Delete an Azure Bare Metal Instance.
"""
