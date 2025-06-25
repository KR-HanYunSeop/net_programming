import asyncio
import random
port = 2500
BUFSIZE = 1024

async def handle_echo(reader, writer):
    while True:
        data = await reader.read(BUFSIZE)
        # data = await reader.readline()
        # data = await reader.readuntil(separator=b'i')
        addr = writer.get_extra_info('peername')
        print(f'Received {data.decode()!r} from {addr!r}')

        if data == b'1':
            temp = random.randint(0,40)
            msg = f'Temp={temp}'
        elif data == b'2':
            humid = random.randint(0,100)
            msg = f'Humid={humid}'          
        
        writer.write(msg.encode())
        await writer.drain()
        print(f'Send: {data.decode()!r}')


async def main():
    server = await asyncio.start_server(handle_echo, '', port)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    await server.serve_forever()

asyncio.run(main())