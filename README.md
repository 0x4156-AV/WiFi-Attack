# WiFi-Attack
A tool created by Aaron Vigal to brute force the password for any WiFi Network. This tool works by finding the MAC Address of the networks router and sending it deauthentication packets, and sniffing the network for the devices to reconnect. Once the program has intercepted the hand shake then it will start hashing passwords from a chosen wordlist and comparing it to the handshakes hash. This uses a combination of tools from the aircrack-ng suite and would not be possible without it.

This tool should run under most versions of Linux but is optimized for working on Kali. The setup is very straight-forward just copy and paste the following code into a terminal:

```{r, engine='bash', count_lines}
wget https://raw.githubusercontent.com/AaronVigal/WiFi-Attack/master/setup
sudo chmod +x setup
sudo ./setup 
```

The setup file checks/installs the following dependencies:

1. aircrack-ng
2. Python 3.5
3. at
4. libnotify-bin

##*Warning!!!*
Me, my Affiliates and all of this projects Contributers in no way promote or encourage un-lawful hacking and this toolkit should be rightfully used for it's purpose for penetration testing on your own network or any network that you have explicit consent from the Administrator. Me, my Affiliates and any Contributers cannot and will not be held liable for any damage or unlawful action that may occur while using this toolkit. 

Happy Hacking!
