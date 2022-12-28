# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_streams import schemas  # noqa: F401


class Log(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "topic1",
            "topic2",
            "address",
            "logIndex",
            "topic0",
            "data",
            "topic3",
            "transactionHash",
        }
        
        class properties:
            logIndex = schemas.StrSchema
            transactionHash = schemas.StrSchema
            address = schemas.StrSchema
            data = schemas.StrSchema
            
            
            class topic0(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'topic0':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class topic1(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'topic1':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class topic2(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'topic2':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class topic3(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'topic3':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class triggers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TriggerOutput']:
                        return TriggerOutput
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TriggerOutput'], typing.List['TriggerOutput']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'triggers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TriggerOutput':
                    return super().__getitem__(i)
            __annotations__ = {
                "logIndex": logIndex,
                "transactionHash": transactionHash,
                "address": address,
                "data": data,
                "topic0": topic0,
                "topic1": topic1,
                "topic2": topic2,
                "topic3": topic3,
                "triggers": triggers,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    topic1: MetaOapg.properties.topic1
    topic2: MetaOapg.properties.topic2
    address: MetaOapg.properties.address
    logIndex: MetaOapg.properties.logIndex
    topic0: MetaOapg.properties.topic0
    data: MetaOapg.properties.data
    topic3: MetaOapg.properties.topic3
    transactionHash: MetaOapg.properties.transactionHash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic1"]) -> MetaOapg.properties.topic1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic2"]) -> MetaOapg.properties.topic2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logIndex"]) -> MetaOapg.properties.logIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic0"]) -> MetaOapg.properties.topic0: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic3"]) -> MetaOapg.properties.topic3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionHash"]) -> MetaOapg.properties.transactionHash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triggers"]) -> MetaOapg.properties.triggers: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["topic1"], typing_extensions.Literal["topic2"], typing_extensions.Literal["address"], typing_extensions.Literal["logIndex"], typing_extensions.Literal["topic0"], typing_extensions.Literal["data"], typing_extensions.Literal["topic3"], typing_extensions.Literal["transactionHash"], typing_extensions.Literal["triggers"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic1"]) -> MetaOapg.properties.topic1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic2"]) -> MetaOapg.properties.topic2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logIndex"]) -> MetaOapg.properties.logIndex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic0"]) -> MetaOapg.properties.topic0: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic3"]) -> MetaOapg.properties.topic3: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionHash"]) -> MetaOapg.properties.transactionHash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triggers"]) -> typing.Union[MetaOapg.properties.triggers, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["topic1"], typing_extensions.Literal["topic2"], typing_extensions.Literal["address"], typing_extensions.Literal["logIndex"], typing_extensions.Literal["topic0"], typing_extensions.Literal["data"], typing_extensions.Literal["topic3"], typing_extensions.Literal["transactionHash"], typing_extensions.Literal["triggers"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        topic1: typing.Union[MetaOapg.properties.topic1, None, str, ],
        topic2: typing.Union[MetaOapg.properties.topic2, None, str, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        logIndex: typing.Union[MetaOapg.properties.logIndex, str, ],
        topic0: typing.Union[MetaOapg.properties.topic0, None, str, ],
        data: typing.Union[MetaOapg.properties.data, str, ],
        topic3: typing.Union[MetaOapg.properties.topic3, None, str, ],
        transactionHash: typing.Union[MetaOapg.properties.transactionHash, str, ],
        triggers: typing.Union[MetaOapg.properties.triggers, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Log':
        return super().__new__(
            cls,
            *_args,
            topic1=topic1,
            topic2=topic2,
            address=address,
            logIndex=logIndex,
            topic0=topic0,
            data=data,
            topic3=topic3,
            transactionHash=transactionHash,
            triggers=triggers,
            _configuration=_configuration,
        )

from openapi_streams.model.trigger_output import TriggerOutput
