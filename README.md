# Vproxy v1.6
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
>Setup VPN server on localip and redirect traffic sent from the device to proxy
>Setup VPN server on localip for monitor traffic from devices 

```sh
$sudo python vproxy.py -ip [LOCALIP] -port [PORTLIST] -proxy [PROXYHOST:PROXYPORT]-mode redirect
```

```sh
$sudo python vproxy.py -ip [LOCALIP] -mode monitor
```

#Configuring VPN Videos
> IOS - https://www.youtube.com/watch?v=TC-xJ9rCTXU

> Android - https://www.youtube.com/watch?v=bFeJZKX4O3A

#Limitations
>Certificate Pinning

#Updates
> Updated features - Monitor vs Redirect mode is now active
> PIP module - future update
> 
