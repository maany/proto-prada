#!/bin/bash


cd prada
echo "Removing Old References"
rm -rf ref

echo "Activating VirtualEnv"

source ./.virtualenv/bin/activate

echo "Installing grpcio-tools"
pip install grpcio-tools

echo "Creating interface package for gRPC code"

mkdir ref
touch ref/__init__.py

echo "Building gRPC services"
python -m grpc_tools.protoc -I=../proto --python_out=./ref --grpc_python_out=./ref ../proto/*.proto

echo "Deactivating Virtualenv"
deactivate
cd ../