import asyncio
from aioquic.asyncio import connect
from aioquic.quic.configuration import QuicConfiguration

HOST = 'localhost'  # Change to your server's IP
PORT = 4433

async def run():
    configuration = QuicConfiguration(is_client=True)
    configuration.verify_mode = False  # Disable certificate verification for self-signed cert
    async with connect(HOST, PORT, configuration=configuration) as client:
        # Use high-level stream API
        reader, writer = await client.create_stream()
        message = b"Hello from QUIC client!"
        print(f"[QUIC CLIENT] Sending: {message.decode()}")
        writer.write(message)
        await writer.drain()
        writer.write_eof()  # Close the stream for writing
        # Wait for response
        data = await reader.read()
        if data:
            print(f"[QUIC CLIENT] Received: {data.decode()}")

if __name__ == "__main__":
    asyncio.run(run())
