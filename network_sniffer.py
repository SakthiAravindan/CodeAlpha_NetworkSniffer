from scapy.all import sniff

# This function runs every time a packet is captured
def show_packet(packet):
    if packet.haslayer("IP"):
        ip = packet["IP"]
        print(f"📦 Packet - Source: {ip.src} → Destination: {ip.dst} | Protocol: {ip.proto}")

print("🟢 Sniffer started... (It will capture 10 packets)")
sniff(prn=show_packet, count=10)
