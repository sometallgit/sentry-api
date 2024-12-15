import os
from sentry_analytics.api import api_config
from pytest import raises

def current_file_dir():
    return os.path.dirname(__file__)

def make_path(path: str) -> str:
    return os.path.join(current_file_dir(), path)

# ensure config values are passed through
def test_config():
    config = api_config.ApiConfig("auth_token", "org_slug", "project_name")

    assert config.get_auth_token() == "auth_token" 
    assert config.get_org_slug() == "org_slug"
    assert config.get_project_name() == "project_name"

# ensure empty config values raise error
def test_empty_config():
    with raises(ValueError):
        api_config.ApiConfig("", "y", "z")
    with raises(ValueError):
        api_config.ApiConfig("x", "", "z")
    with raises(ValueError):
        api_config.ApiConfig("x", "y", "")

# test loading from a config files
def test_config_file():
    config = api_config.ApiConfigFile(make_path("file/config.json"))

    assert config.get_auth_token() == "auth_token" 
    assert config.get_org_slug() == "org_slug"
    assert config.get_project_name() == "project_name"