#/bin/bash
protoc -I=./proto/ --python_out=./prada-py ./proto/*.proto
cp -rf prada-py prada/
touch prada/prada-py/__init__.py