#!/bin/bash

cd "$(dirname "$0")"

. .venv/bin/activate
otp=$(python3 otp.py)
deactivate

echo $otp | sudo openconnect -u <userid> \
    --passwd-on-stdin \
    your-vpn-server.example.com
