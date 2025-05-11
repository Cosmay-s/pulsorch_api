from flask import Flask
import logging
from pulsorch.views import runs, jobs, systems, dependence, scheduleds

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)
app = Flask(__name__)

app.register_blueprint(runs.view)
app.register_blueprint(jobs.view)
app.register_blueprint(systems.view)
app.register_blueprint(dependence.view)
app.register_blueprint(scheduleds.view)
