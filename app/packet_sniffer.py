from scapy.all import sniff, IP
from threading import Thread
from .detector import detect_anomaly

packets_data = []
anomalies = []

def process_packet(packet):
    if packet.haslayer(IP):
        entry = {
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'len': len(packet)
        }
        packets_data.append(entry)
        detect_anomaly(entry, packets_data, anomalies)

def start_sniffing():
    sniff(prn=process_packet, store=False)

# Start sniffing in a separate thread
sniff_thread = Thread(target=start_sniffing)
sniff_thread.daemon = True
sniff_thread.start()
