import asyncio
import orm
from models import User, Blog, Comment

async def insert(loop):
    await orm.create_pool(loop=loop, host='localhost', user='root', password='123456', db='awesome')
    u = User(name='Test', email='test2@example.com', passwd='123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(insert(loop))
loop.close()