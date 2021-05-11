#/bin/bash
# protoc -I=./proto/ --python_out=./prada-py ./proto/*.proto
# cp -rf prada-py prada/
# touch prada/prada-py/__init__.py

echo "Activating VirtualEnv"
cd prada
source ./.virtualenv/bin/activate

echo "Installing grpcio-tools"
pip install grpcio-tools

echo "Creating interface package for gRPC code"

mkdir -p interface/service interface/model
touch interface/__init__.py interface/service/__init__.py interface/model/__init__.py

echo "Building gRPC services"
python -m grpc_tools.protoc -I=../proto --python_out=./interface/model --grpc_python_out=./interface/service ../proto/*.proto

echo "Deactivating Virtualenv"
deactivate
cd ../