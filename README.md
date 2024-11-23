# Info
Meant to quickly spin up a WireGuard VPN running over 443  
using pihole to block ads and DoH to protect dns queries  
via ansible  

## Why?
Bypass Hotel Wi-Fi filtering  
You want your traffic to be private  
You want to appear to be coming from another location/country  

## OS Supported
Debian 12  
Ubuntu 22.04 and possible 24.04, more testing needed. 
CentOS Stream 9  
Fedora Server 38  
AlmaLinux 9.2  

## Tested on
Tested on DO $4 droplet  
Azure Standard_B1s $11/month  
AWS t2.micro   

## SSH User 
Make sure you can ssh and sudo -s into your VPS before tne next step.  
If you need to use a different username, uncomment and set ansible_user in the host file. 

## External Firewall: like Digital Ocean Firewall, Azure Inbound Ports, AWS Security Groups
You will need to open the following  
  * UDP > Port 443  
  * TCP > Port 8443   
  * TCP > Port 22
  * Make sure to adjust these if you change any of the port settings in the vars file  


## Ansible local files - install
* Edit hosts file and change IP to your new VM Public IP  
* Edit vars/main.yml and adjust as needed  
* Install: ansible-playbook -i hosts tasks/main.yml -K  

## WireGuard UI
Load up WireGuard UI *sometimes takes a second for it*  
* On WireGuard Clients Page, click New Client, enter name, leave the rest as default  
* Download user config or use QR code in Wirguard Mobile app  
* Apply settings in top right and test. 
    

## Changelog
10/19/23 Added Support For AlmaLinux, changing DoH Servers, and FireBog Extended block list  
10/19/23 Added Support For Fedora Server 38 and CentOS Stream 9 with SELinux Enabled  
10/17/23 Added some utils for expanding block list and updating pihole  
10/10/23 Added Support for AWS  
10/8/23 Linted all playbooks  
10/3/23 Added support for Azure (and probably AWS, etc. That do not assign IP directly to the VM)  
9/30/23 Removed user having to specify interface in vars  
9/26/23 Got bored, started this  

## Sometimes the lie is easier to live with ~ Tom