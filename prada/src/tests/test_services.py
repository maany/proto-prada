import pytest
import grpc

from ref.base_services_pb2_grpc import ResourceManagerStub

@pytest.fixture
def resource_manager_stub():
    ResourceManagerStub('')