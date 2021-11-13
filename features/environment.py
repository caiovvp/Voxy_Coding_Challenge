from behave import *
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

from features.context.fixtures import *


def before_all(context):
    use_fixture(browser_firefox, context)
    use_fixture(timeout_for_page_load, context)


def after_step(context, step):
    # method to activate ipdb debugger everytime an error occurs
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def before_feature(context, feature):
    # method to autoretry the whole feature or scenario if it fails
    for scenario in feature.walk_scenarios():
        if "autoretry" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=3)
