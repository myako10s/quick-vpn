# quick-vpn
A script that allows you to quickly enter your PassLogic one-time password to easily connect to a VPN.

# Requirements

* openconnect
* Python
* Python libs: beautifulsoup4, lxml

# Usage

1. Edit `config.py` to set your PassLogic parameters.

1. Edit `connect.sh` to change openconnect options.

1. Test if the script works well.

   ```sh
   python3 otp.py
   ```

   If the script works well, the matrix will be printed to stderr and the one-time password will be printed to stdout.

1. Run `connect.sh`

   ```sh
   chmod +x connect.sh
   ./connect.sh
   ```
