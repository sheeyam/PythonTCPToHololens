import asyncio

#THIS CODE WORKS SENDING STRING MESSAGE TO HOLOLENS

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('192.168.1.110', 9090, loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()


message = 'hello there frend'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
