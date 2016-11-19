# Vproxy v1.0
Forward HTTP/S Traffic To Proxy Instance

#Description
>The WIFI proxy option in your mobile device doesn't make you capture all of the HTTP/S traffic using your favorite proxy program ?
use Vproxy to solve this issue and capture the whole HTTP/S traffic

#System Requirements
>This script was built and test on Kali-Linux and should work on any linux distribution

#Prerequisites
>pip install termcolor

#Usage
>Setup VPN server on localip and redirect traffic sent from the clients (80,443) to proxy 192.168.1.10:8080 

```sh
$sudo python vproxy.py -localip 192.168.1.9 -phost 192.168.1.10 -pport 8080 -port 80,443
```

#Configuring VPN Videos
> IOS - https://www.youtube.com/watch?v=TC-xJ9rCTXU

> Android - https://www.youtube.com/watch?v=bFeJZKX4O3A

#Limitations
>Certificate Pinning
