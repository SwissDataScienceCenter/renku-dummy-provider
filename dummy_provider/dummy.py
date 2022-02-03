# -*- coding: utf-8 -*-
#
# Copyright 2022 - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
from typing import Any, Dict

import networkx as nx

from renku.core import errors
from renku.core.models.workflow.provider import IWorkflowProvider
from renku.core.plugins import hookimpl


class DummyProvider(IWorkflowProvider):
    """A dummy workflow executor provider plugin."""

    @hookimpl
    def workflow_provider(self):
        """Workflow provider name."""
        return (self, "dummy")

    @hookimpl
    def workflow_execute(self, dag: nx.DiGraph, basedir: Path, config: Dict[str, Any]):
        raise errors.ParameterError(
            "Dummy provider is never meant to be used for executing workflows."
        )

        return None


dummy_plugin = DummyProvider()
