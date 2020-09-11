# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.help_files import helps


helps['baremetalinstance'] = """
    type: group
    short-summary: (PREVIEW) Manage Bare Metal Instances.
    """

helps['baremetalinstance show'] = """
    type: command
    short-summary: Get the details of a Bare Metal Instance.
    """

helps['baremetalinstance list'] = """
    type: command
    short-summary: List Bare Metal Instances.
"""

helps['baremetalinstance restart'] = """
    type: command
    short-summary: Restart a Bare Metal Instance.
"""

helps['baremetalinstance start'] = """
    type: command
    short-summary: Start a Bare Metal Instance.
"""

helps['baremetalinstance shutdown'] = """
    type: command
    short-summary: Shutdown a BareMetal Instance.
"""

helps['baremetalinstance update'] = """
    type: command
    short-summary: Update the tags field of a Bare Metal Instance.
"""

helps['baremetalinstance delete'] = """
    type: command
    short-summary: Delete a Bare Metal Instance.
"""
