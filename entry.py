import aiohttp, asyncio, argparse, aioreloader
from demo import create_app
from demo.settings import load_config


try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except:
    print("Library uvloop is not available")

parser = argparse.ArgumentParser(description="Bla-bla")
parser.add_argument('--host', help="Host to listen", default="0.0.0.0")
parser.add_argument('--port', help="Port to accept connection", default=5000)
parser.add_argument('--reload', action="store_true", help="Autoreload")
parser.add_argument('-c', '--config', type=argparse.FileType('r'), help="Path to config file")
args = parser.parse_args()
app = create_app(config=load_config(args.config))

if args.reload:
    print("Start with code reload")
    aioreloader.start()
if __name__ == "__main__":
    aiohttp.web.run_app(app, host=args.host, port=args.port)
