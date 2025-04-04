from scapy.all import *
import random

# Convert hex-encoded flag to string
flag_hex = "666c61677b796f755f676f745f615f676f6f645f6b6e6f776c656467655f696e5f77697265736861726b7d"
flag_text = bytearray.fromhex(flag_hex).decode()

packets = []

# 1. Simulated ARP traffic
for i in range(3):
    arp = ARP(op=1, pdst="192.168.216.128", psrc="192.168.216.128")
    packets.append(Ether(dst="ff:ff:ff:ff:ff:ff") / arp)

# 2. Simulated DNS queries
dns_domains = ["google.com", "example.com", "ctfchallenge.local"]
for domain in dns_domains:
    dns_req = IP(src="192.168.216.128", dst="192.168.216.128") / UDP(sport=random.randint(1024,65535), dport=53) / DNS(rd=1, qd=DNSQR(qname=domain))
    packets.append(dns_req)

# 3. Simulated HTTP GET traffic
http_get = IP(src="192.168.216.128", dst="192.168.216.128") / TCP(dport=80, sport=12345, flags="PA") / (
    "GET /index.html HTTP/1.1\r\nHost: 192.168.216.128\r\nUser-Agent: FakeBrowser\r\n\r\n")
packets.append(http_get)

# 4. Random ICMP noise packets
for i in range(5):
    pkt = IP(src="192.168.216.128", dst="192.168.216.128") / ICMP() / Raw(load="randomping" + str(i))
    packets.append(pkt)

# 5. Flag hidden in real ICMP payloads (split into chunks)
for i in range(0, len(flag_text), 8):
    chunk = flag_text[i:i+8]
    pkt = IP(src="192.168.216.128", dst="192.168.216.128") / ICMP() / chunk
    packets.append(pkt)

# 6. Add some TCP handshake traffic (more noise)
tcp_handshake = [
    IP(src="192.168.216.128", dst="192.168.216.128") / TCP(sport=1234, dport=80, flags="S"),
    IP(src="192.168.216.128", dst="192.168.216.128") / TCP(sport=1234, dport=80, flags="SA"),
    IP(src="192.168.216.128", dst="192.168.216.128") / TCP(sport=1234, dport=80, flags="A"),
]
packets.extend(tcp_handshake)

# Shuffle all packets to make the order non-obvious
random.shuffle(packets)

# Save to PCAP
wrpcap("forensic_ctf_complex.pcap", packets)
print("âœ… PCAP file created: forensic_ctf_complex.pcap with traffic on 192.168.216.128")
