from scapy.all import rdpcap

# Choose pcap file I want to analyze
packets = rdpcap('./WireSharkCaps/secondtrial.pcapng')


# print short summary of packet(s)
for packet in packets:
    if packet.haslayer('DNS'):  
        print(packet.summary())