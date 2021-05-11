from ref.service.base_services_pb2_grpc import ResourceManagerServicer
class ResourceManager(ResourceManagerServicer):
    def create_resource(self, resource):
        print("Creating Resource")
        return resource
    

if __name__ == "__main__":
    ResourceManager.create_resource