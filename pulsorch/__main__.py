from pulsorch.server import app
from pulsorch.config import create_server_config
from pulsorch.db import create_tables


def main():
    create_tables()
    config = create_server_config()
    app.run(host=config.host, port=config.port)


if __name__ == "__main__":
    main()
