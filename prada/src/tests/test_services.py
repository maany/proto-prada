import pytest
import grpc_testing
import grpc
import ref.base_services_pb2 as base_services_pb2
from ref.base_models_pb2 import Resource
from src.service.resource_manager import ResourceManager


@pytest.fixture(scope='module')
def servicers():
    descriptors_to_servicers = {
        base_services_pb2.DESCRIPTOR.services_by_name['ResourceManager']: ResourceManager
    }
    return descriptors_to_servicers


@pytest.fixture(scope='module')
def test_server(servicers):
    return grpc_testing.server_from_dictionary(servicers, grpc_testing.strict_real_time())


def test_create_resource(test_server):
    request = Resource(
        guid="13u98sdbk"
    )
    create_resource_method = test_server.invoke_unary_unary(
        method_descriptor=(base_services_pb2.DESCRIPTOR
            .services_by_name['ResourceManager']
            .methods_by_name['create_resource']),
        invocation_metadata={},
        request=request, timeout=1)
    response, metadata, code, details = create_resource_method.termination()
    assert code == grpc.StatusCode.OK
