import os

product_list_config = {
    "ENV_" + key: os.environ.get(key)
    for key in (
        "LANG",
        "SEARCH_URL_PREFIX",
        "SEARCH_URL_SUFFIX",
        "WAREHOUSE_URL_PREFIX",
        "WAREHOUSE_URL_SUFFIX",
    )
}


def inject_environment() -> dict:
    return product_list_config
