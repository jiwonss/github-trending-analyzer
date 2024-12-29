import requests
from app.core.config import settings

GITHUB_API_BASE_URL = settings.github_api_base_url
GITHUB_TOKEN = settings.github_token

if not GITHUB_TOKEN:
    raise ValueError("GitHub Token is not set in the environment variables")


headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}


# Github Search(Repository)
def fetch_repositories(query: str, sort: str, order: str, per_page: int, page: int):
    url = f"{GITHUB_API_BASE_URL}/search/repositories"

    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
        "page": page,
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            f"GitHub API 호출 실패: {response.status_code}, {response.text}"
        )
    return response.json()
