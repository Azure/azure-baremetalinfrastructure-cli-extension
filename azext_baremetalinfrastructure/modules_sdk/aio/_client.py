# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.6, generator: @autorest/python@6.7.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import BareMetalInfrastructureClientConfiguration
from .operations import AzureBareMetalInstancesOperations, AzureBareMetalStorageInstancesOperations, Operations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class BareMetalInfrastructureClient:  # pylint: disable=client-accepts-api-version-keyword
    """The Bare Metal Infrastructure Management client.

    :ivar azure_bare_metal_instances: AzureBareMetalInstancesOperations operations
    :vartype azure_bare_metal_instances:
     azure.mgmt.baremetalinstances.aio.operations.AzureBareMetalInstancesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.baremetalinstances.aio.operations.Operations
    :ivar azure_bare_metal_storage_instances: AzureBareMetalStorageInstancesOperations operations
    :vartype azure_bare_metal_storage_instances:
     azure.mgmt.baremetalinstances.aio.operations.AzureBareMetalStorageInstancesOperations
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword endpoint: Service URL. Default value is "https://management.azure.com".
    :paramtype endpoint: str
    :keyword api_version: Api Version. Default value is "2023-07-31-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        subscription_id: str,
        credential: "AsyncTokenCredential",
        *,
        endpoint: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = BareMetalInfrastructureClientConfiguration(
            subscription_id=subscription_id, credential=credential, **kwargs
        )
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.azure_bare_metal_instances = AzureBareMetalInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.azure_bare_metal_storage_instances = AzureBareMetalStorageInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "BareMetalInfrastructureClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)