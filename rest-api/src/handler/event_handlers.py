import asyncio

from utils.memcached_utils import MemcachedManager
from utils.mongo_manager import MongoDBManager
from utils.elasticsearch_utils import ElsaticSearchManager


# выполняется сразу при запуске приложения
async def startup():
    # запускает асинхронную инициализацию клиента MongoDB, возвращая объект future
    init_mongo_future = MongoDBManager.init_mongo_client()
    # запускает асинхронное подключение и инициализацию Elasticsearch, возвращая объект Future
    init_elasticsearch_future = ElsaticSearchManager.connect_and_init_elasticsearch()
    # ожидает завершения обоих асинхронных операций, обеспечивая их параллельное выполнение. Что-то из разряда мониторов в С++
    await asyncio.gather(init_mongo_future, init_elasticsearch_future)
    # инициализирует клиент Memcached, операция синхронная
    MemcachedManager.init_memcached_client()

# что происходит при остановке
async def shutdown():
    # закрывает соединение с MongoDB
    MongoDBManager.close_connection()
    # закрывает соединение с Memcached.
    MemcachedManager.close_memcached_connect()
    # закрывает соединение с Elasticsearch, но операция асинхронная
    await ElsaticSearchManager.close_elasticsearch_connect()
