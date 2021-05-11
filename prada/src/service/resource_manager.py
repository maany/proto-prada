from ref.base_services_pb2_grpc import ResourceManagerServicer
from ref.base_models_pb2 import Resource


class ResourceManager(ResourceManagerServicer):

    def create_resource(self, request, context):
        print("Creating Resource ")
        return request
