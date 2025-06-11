import asyncio
from aioquic.asyncio import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.asyncio.protocol import QuicConnectionProtocol

HOST = 'localhost'
PORT = 4433

class EchoQuicProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if hasattr(event, 'data') and event.data:
            print(f"[QUIC SERVER] Received: {event.data.decode()}")
            self._quic.send_stream_data(event.stream_id, event.data, end_stream=True)

async def main():
    configuration = QuicConfiguration(is_client=False)
    configuration.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    await serve(HOST, PORT, configuration=configuration, create_protocol=EchoQuicProtocol)
    print(f"[QUIC SERVER] Listening on {HOST}:{PORT}")
    await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
