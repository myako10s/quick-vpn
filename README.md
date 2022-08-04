# quick-vpn
A script that allows you to quickly enter your PassLogic one-time password to easily connect to a VPN.

# Requirements

* openconnect
* Python
* Python libs: beautifulsoup4, lxml

# Settings

1. Edit `config.py` to set your PassLogic parameters.

1. Test if the script works well.

   ```sh
   python3 otp.py
   ```

   If the script works well, the matrix will be printed to stderr and the one-time password will be printed to stdout.


# Usage

1. Create a script to quickly connect to your VPN.

   For example:

   ```sh
   #!/bin/bash

   cd "$(dirname "$0")"

   . .venv/bin/activate
   otp=$(python3 otp.py)
   deactivate

   echo $otp | sudo openconnect -u <userid> \
       --passwd-on-stdin \
       your-vpn-server.example.com
   ```

1. Run the script.

   ```sh
   chmod +x connect.sh
   ./connect.sh
   ```

   It might be useful to be able to run `openconnect` command without sudo password.

   ```
   $ sudo cat /etc/sudoers.d/drop-in
   # skip sudo password
   %admin    ALL = (ALL) NOPASSWD: /path/to/openconnect
   ```