import jinja2
import aiohttp_jinja2
import asyncpgsa
from aiohttp import web
from .routes import setup_routes


__all__ = ('create_app', )


async def create_app(config):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('demo', 'templates'))
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    setup_routes(app)
    return app


async def on_start(app):
    config = app['config']
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])


async def on_shutdown(app):
    await app['db'].close()