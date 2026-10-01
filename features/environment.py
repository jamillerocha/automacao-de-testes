# features/environment.py
from tests.fixtures.driver import create_driver


def before_scenario(context, scenario):
    context.driver = create_driver()
    context.driver.implicitly_wait(0)  # você já usa esperas explícitas


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()