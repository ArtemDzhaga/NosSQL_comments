from fastapi import FastAPI

# функции для обработки событий запуска и остановки приложения
from handler.event_handlers import startup, shutdown
# маршрутизаторы для обработки различных разделов API
from router.hosts_router import router as hosts_router
from router.users_router import router as users_router
from router.data_loader_router import router as data_loader_routers
from router.reservations_router import router as reservations_router

app = FastAPI()

# Включение маршрутизаторов
# app.include_router(router_name, tags=[...], prefix="/api/.../"): Эта команда включает отдельные маршрутизаторы в основное приложение, объединяя их в единый API.
# router_name: Название подключаемого маршрутизатора.
# tags=[...]: Список тегов, которые будут связаны с маршрутами данного маршрутизатора для организации документации.
# prefix="/api/.../": Префикс URL-адресов для всех маршрутов данного маршрутизатора, позволяющий разделить API на разделы.
app.include_router(hosts_router, tags=["Rooms"], prefix="/api/rooms")
app.include_router(users_router, tags=["Names"], prefix="/api/users")
app.include_router(data_loader_routers, tags=[
                   "DataLoader"], prefix="/api/data_loader")
app.include_router(reservations_router, tags=[
                   "Reservations"], prefix="/api/reservations")
# Обработка событий:
# app.add_event_handler("startup", startup): Регистрирует функцию startup для выполнения действий перед запуском приложения, например, инициализация баз данных или подключение к внешним сервисам.
# app.add_event_handler("shutdown", shutdown): Регистрирует функцию shutdown для выполнения действий перед остановкой приложения, например, закрытие соединений или сохранение данных.
# prefix="/api/.../": Префикс URL-адресов для всех маршрутов данного маршрутизатора, позволяющий разделить API на разделы.
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)
