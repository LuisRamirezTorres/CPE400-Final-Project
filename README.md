# CPE400-Final-Project
Final Project For CPE400 Computer Communication Networks, Spring 2024 at UNR


# SET UP: 

Assuming Python is installed on your local machine, clone the repository and travel to the directory where your files can be found. If Pyshark or Scapy are not installed:

> pip install pyshark

> pip install scapy

# To Run The Scripts:

Make sure the Wireshark capture files you wish to parse are in either the same folder as the scripts or in a different folder of your choice.
My folder was called WireSharkCaps as seen in the analyzeCaps.py script. You can change the path to the Wireshark capture file in line 4 of the analyzeCaps.py and pktSum.py script.

> pyshark.FileCapture('YOUR PATH')

> rdpcap('YOUR PATH')

Finally, run the scripts:

> python analyzeCaps.py

> python pktSum.py
