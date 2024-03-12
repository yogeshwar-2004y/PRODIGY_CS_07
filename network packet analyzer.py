import sys
from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto
        payload = packet["IP"].payload

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")
        print("Payload:", payload)

def main():
    print("Network Packet Analyzer - Press Ctrl+C to stop capturing.")

    # Sniff packets and call packet_callback for each captured packet
    try:
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("Capture stopped. Exiting...")

if __name__ == "__main__":
    main()
