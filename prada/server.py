import logging
import time
from concurrent import futures

import grpc

from src.service.resource_manager import ResourceManager
import ref.base_services_pb2_grpc as base_services_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    base_services_pb2_grpc.add_ResourceManagerServicer_to_server(ResourceManager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
