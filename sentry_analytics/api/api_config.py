import json

class ApiConfig():
    def __init__(self, 
                 auth_token : str = "", 
                 org_slug: str = "", 
                 project_name: str = ""):

        self._auth_token = auth_token
        self._org_slug = org_slug
        self._project_name = project_name

        if self._auth_token == "":
            raise ValueError("auth_token is required")
        if self._org_slug == "":
            raise ValueError("org_slug is required")
        if self._project_name == "":
            raise ValueError("project_name is required")

    def get_auth_token(self) -> str:
        return self._auth_token

    def get_org_slug(self) -> str:
        return self._org_slug
    
    def get_project_name(self) -> str:
        return self._project_name


class ApiConfigFile(ApiConfig):
    def __init__(self, file_path: str):
        self.init_from_file(file_path)

    def init_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            json_data = json.load(f)
            super().__init__(
                auth_token=json_data["auth_token"],
                org_slug=json_data["org_slug"],
                project_name=json_data["project_name"]
            )