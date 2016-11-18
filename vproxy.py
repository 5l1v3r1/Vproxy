#/usr/bin/python

import sys
import time
import os
import argparse
import re
import subprocess
from termcolor import colored

def write_conf(proxyhost,proxyport,ports,isr):
	if (os.path.exists('vproxy.sh')):
				os.remove('vproxy.sh')
	f = open('vproxy.sh','w')
	f.write('apt-get -y install pptpd || {echo "Could not install pptpd" exit 1}\n')
	f.write('iptables -t nat -F\n')
	if(isr):
		for port in ports:
			f.write('iptables -t nat -A PREROUTING -p tcp -s 192.168.2.0/24 --dport '+port+' -j DNAT --to-destination '+proxyhost+':'+proxyport+'\n')
	f.write('sysctl -w net.ipv4.ip_forward=1\n')
	f.write('iptables -t nat -A POSTROUTING -j MASQUERADE\n')
	f.write('cat >/etc/ppp/chap-secrets <<END\n')
	f.write('Vproxy pptpd Vproxy123 *\n')
	f.write('END\n')
	f.write('cat >/etc/pptpd.conf <<END\n')
	f.write('option /etc/ppp/options.pptpd\n')
	f.write('localip 192.168.2.1\n')
	f.write('remoteip 192.168.2.10-100\n')
	f.write('END\n')
	f.write('cat >/etc/ppp/options.pptpd <<END\n')
	f.write('name pptpd\n')
	f.write('refuse-pap\n')
	f.write('refuse-chap\n')
	f.write('refuse-mschap\n')
	f.write('require-mschap-v2\n')
	f.write('require-mppe-128\n')
	f.write('ms-dns 8.8.4.4\n')
	f.write('proxyarp\n')
	f.write('lock\n')
	f.write('nobsdcomp \n')
	f.write('novj\n')
	f.write('novjccomp\n')
	f.write('mtu 1490\n')
	f.write('mru 1490\n')
	f.write('nologfd\n')
	f.write('END\n')
	f.write('sleep 4\n')
	f.write('service pptpd restart\n')
	f.close() 
	subprocess.Popen("bash vproxy.sh", shell=True, stdout=subprocess.PIPE).stdout.read()

def cleanup():
	subprocess.Popen("service pptpd stop", shell=True, stdout=subprocess.PIPE).stdout.read()
	subprocess.Popen("iptables -t nat -F", shell=True, stdout=subprocess.PIPE).stdout.read()

def main():
	print """

 /$$    /$$                                                 
| $$   | $$                                                 
| $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$
|  $$ / $$//$$__  $$ /$$__  $$ /$$__  $$|  $$ /$$/| $$  | $$
 \  $$ $$/| $$  \ $$| $$  \__/| $$  \ $$ \  $$$$/ | $$  | $$
  \  $$$/ | $$  | $$| $$      | $$  | $$  >$$  $$ | $$  | $$
   \  $/  | $$$$$$$/| $$      |  $$$$$$/ /$$/\  $$|  $$$$$$$
    \_/   | $$____/ |__/       \______/ |__/  \__/ \____  $$
          | $$                                     /$$  | $$
          | $$       by eran@cyberint.com         |  $$$$$$/
          |__/                                     \______/ 

	"""

	#Define The ArgParse
	parser = argparse.ArgumentParser(
	    epilog = ''' Example: 
   python vproxy.py -localip '''+ colored("192.168.1.9","yellow") + ''' -phost ''' + colored("192.168.1.10", "yellow") + ''' -pport '''+colored("8080","yellow")+''' -port 80,443''',
	    formatter_class=argparse.RawTextHelpFormatter)

	parser.add_argument('-localip', help='Make sure bridge mode is configured', required=True)
	parser.add_argument('-phost', help='Proxy host, e.g 192.168.1.0', required=False)
	parser.add_argument('-pport', help='Proxy port, e,g 8080', required=False)
	parser.add_argument('-port', help='Which port to forward to proxy, e.g 80,443', required=False)
	args = parser.parse_args()

	print colored("Starting Vproxy...", "green")
	if (args.phost and args.pport and not args.port):
		print colored("[!] missing port argument", "red")
	elif ((args.phost and not args.pport) or (args.pport and not args.phost)):
		print colored("[!] missing proxy arguments check again","red")
	elif (args.phost and args.pport and args.localip and args.port):
		print colored("[V]Configuring PPTP server and redirect HTTP/S traffic on port: ","green")+colored(str(args.port.split(",")),"yellow")+colored(" to proxy: ","green")+colored(args.phost+":"+args.pport,"yellow")
		write_conf(args.phost,args.pport,args.port.split(","),isr=True)
		print "================================================="
		print "Vproxy Output: "
		print "1.Export and install Proxy SSL Certificate"
		print "2.Configure new VPN profile:"
		print "	PPTP Server: "+ colored(args.localip,"yellow")
		print "	PPTP User: "+ colored("Vproxy","yellow")
		print "	PPTP Password: "+ colored("Vproxy123","yellow")
		print "3. Analzye HTTP/S traffic using your favorite proxy software"
		print "================================================="

		try:
			raw_input("[!]Press any key to close Vproxy...")
		except KeyboardInterrupt:
			cleanup()

		cleanup()
	elif (not args.phost and not args.pport and not args.port):
		print colored("[V]Configuring PPTP server without proxy redirection ...","green")
		write_conf(args.phost,args.pport,None,isr=False)
		print "================================================="
		print "Vproxy Output: "
		print "1.Configure new VPN profile on the mobile device"
		print "	PPTP Server: "+ colored(args.localip,"yellow")
		print "	PPTP User: "+ colored("Vproxy","yellow")
		print "	PPTP Password: "+ colored("Vproxy123","yellow")
		print "2. Use Wireshark or TCPDump to analyze the traffic"
		print "================================================="
		
		try:
			raw_input("[!]Press any key to close Vproxy...")
		except KeyboardInterrupt:
			cleanup()

		cleanup()

if __name__ == '__main__':
    main()
