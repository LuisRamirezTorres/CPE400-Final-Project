import pyshark

#Set the path to the pcap file I want to analyze
capture = pyshark.FileCapture('./WireSharkCaps/firsttrial.pcapng')

pkt_num = 0

#display packets in the capture file
for packet in capture:
    pkt_num += 1
    if 'dns' in packet:
        hostname = packet.dns.qry_name
        if hostname and 'tiktok.com' in hostname:
            print(f"\n\nPACKET {pkt_num} with hostname tiktok found!\n\n")
            print(packet)


