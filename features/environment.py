from behave import *
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

from features.context.fixtures import *


def before_all(context):
    use_fixture(browser_firefox, context)
    use_fixture(timeout_for_page_load, context)


def after_step(context, step):
    # FUNCTION TO ACTIVATE IPDB DEBUGGER EVERYTIME AN ERROR OCCURS
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def before_feature(context, feature):
    # FUNCTION TO AUTORETRY THE WHOLE FEATURE OR SCENARIO IF IT FAILS
    for scenario in feature.walk_scenarios():
        if "autoretry" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=3)