# Vproxy v1.7
Forward HTTP/S Traffic To Proxy Instance

#Description
>The WIFI proxy option in your mobile device doesn't make you capture all of the HTTP/S traffic using your favorite proxy program ?
use Vproxy to solve this issue and capture the whole HTTP/S traffic

#System Requirements
>Linux

>Python 2.x

#Prerequisites
>pip install termcolor

#Usage
>Setup VPN server on localip and redirect traffic sent from the device to proxy instance

>Setup VPN server on localip and monitor traffic from devices

>Setup VPN server on localip and redirect traffic sent to 192.168.1.0/24 to proxy instance

```sh
$sudo python vproxy.py -ip [LOCALIP] -port [PORTLIST] -proxy [PROXYHOST:PROXYPORT] -mode Redirect
```

```sh
$sudo python vproxy.py -ip [LOCALIP]  -port [PORTLIST] -mode Monitor
```

```sh
$sudo python vproxy.py -ip [LOCALIP] -port [PORTLIST] -proxy [PROXYHOST:PROXYPORT] -int 192.168.1.0/24 -mode Redirect
```


#Configuring VPN Videos
> IOS - https://www.youtube.com/watch?v=TC-xJ9rCTXU

> Android - https://www.youtube.com/watch?v=bFeJZKX4O3A

#Limitations
>Certificate Pinning

#Updates
>Intercept Specific Hostnames or IPs
>Updated features - Monitor vs Redirect mode is now active

#Future Work
>PIP module

>Redirect traffic to local machine ports
