# Network Protocol Demo - Transport Layer Protocols

This demo shows simple TCP, UDP, and QUIC client-server communication in Python. You can run each protocol's server and client, and inspect the traffic using Wireshark.

## Prerequisites

- Python 3.8+
- Install dependencies:
  - For QUIC: `pip install aioquic cryptography`
  - For all: No extra dependencies for TCP/UDP
- (Optional) Wireshark for packet inspection

## Files

- `tcp_server.py` / `tcp_client.py`: TCP echo server/client
- `udp_server.py` / `udp_client.py`: UDP echo server/client
- `quic_server.py` / `quic_client.py`: QUIC echo server/client
- `gen_cert.py`: Generates self-signed certs for QUIC
- `cert.pem`, `key.pem`: Certificate and key for QUIC

## Usage

### 1. Generate Certificates (for QUIC)

```
python3 gen_cert.py
```

### 2. Start Servers (in separate terminals)

#### TCP Server

```
python3 tcp_server.py
```

#### UDP Server

```
python3 udp_server.py
```

#### QUIC Server

```
python3 quic_server.py
```

### 3. Run Clients (in separate terminals)

#### TCP Client

```
python3 tcp_client.py
```

#### UDP Client

```
python3 udp_client.py
```

#### QUIC Client

```
python3 quic_client.py
```

## Inspecting Traffic in Wireshark

1. Open Wireshark and start capturing on the appropriate network interface (e.g., `lo0` for localhost).
2. Use filters to view protocol-specific traffic:
   - TCP: `tcp.port == 6000`
   - UDP: `udp.port == 6002`
   - QUIC: `quic && udp.port == 4433` (QUIC runs over UDP)
3. Run the servers and clients as above, and observe the packets in Wireshark.

---

**Note:**

- For QUIC, you may need to add the server's certificate to Wireshark for decryption (see Wireshark docs for TLS/QUIC decryption).
- All scripts use `localhost` by default. Adjust IPs/ports as needed for your setup.
