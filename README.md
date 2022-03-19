# charm-static-ip

This charm will reconfigure a unit to use a static IP (via netplan). However, it depends on DHCP for the initial address.
This was created to get around some bugs related to running etcd on DHCP, where the certs had IP's set in the SAN.
