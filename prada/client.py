import logging

import grpc
import ref.base_services_pb2_grpc as base_services_pb2_grpc
import ref.base_models_pb2 as base_models


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = base_services_pb2_grpc.ResourceManagerStub(channel)
        response = stub.create_resource(base_models.Resource(guid='asd32'))
    print("client received: " + response.guid)


if __name__ == '__main__':
    logging.basicConfig()
    run()
