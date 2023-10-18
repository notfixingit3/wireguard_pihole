# Info
Meant to quickly spin up a Wireguard VPN running over 443  
using pihole to block ads and DoH to protect dns queries

# Why?
Bypass Hotel Wi-Fi filtering  
You want your traffic to be private  
You want to appear to be coming from another location/country  

# OS Supported
Debian 12 Bookworm  
Ubuntu 22.04  
CentOS Stream 9  
Fedora Server 38  

# Tested on
Tested on DO $4 droplet Ubuntu 22.04  
Azure Standard_B1s $11/month Ubuntu 22.04  
AWS t2.micro Ubuntu 22.04  

# Make sure you can SSH under your current username and succesfully sudo -s  

# Ansible local files
Edit hosts file and change IP to your new VM Public IP and set the username that you will use to ssh to VM with  
Edit vars/main.yml and adjust as needed  
Install: ansible-playbook -i hosts tasks/main.yml -K  

# Wireguard UI
Load up wiregguard UI https://<vm-ip>:8443/ *sometimes takes a second for it*  
* On Wireguard Clients Page, click New Client, enter name, leave the rest as default  
     * Download user config or use QR code in Wirguard Mobile app  
   * Apply settings in top right and test. 
    

# Changelog
10/17/23 Added some utils for expanding block list and updating pihole  
10/10/23 Added Support for AWS  
10/8/23 Linted all playbooks  
10/3/23 Added support for Azure (and probably AWS, etc. That do not assign IP directly to the VM)  
9/30/23 Removed user having to specify interface in vars  
9/26/23 Got bored, started this  

# Sometimes the lie is easier to live with ~ Tom M