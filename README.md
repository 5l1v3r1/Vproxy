# Vproxy V1.0
Forward HTTP/S Traffic To Proxy Instance

#Description
> The WIFI proxy option in your mobile device doesn't make you capture all of the HTTP/S traffic using your favorite proxy program ? use Vproxy to solve this issue and capture the whole HTTP/S traffic

#System Requirements
> This script was built and test on Kali-Linux and should work on any linux distribution

#Usage
>Setup VPN server on localip, and redirect traffic sent from clients to destination port 80 and 443 to proxy instance

```sh
$python vproxy.py -localip 192.168.1.9 -phost 192.168.1.10 -pport 8080 -port 80,443
```
#Limitations
>Certificate Pinning
