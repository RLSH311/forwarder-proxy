from typing import Dict


class Config:
    pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config: Dict[str, type(Config)] = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig,
    'Test': TestingConfig,
    'Default': DevelopmentConfig
}


def get_configuration(name: str) -> type(Config):
    return config.get(name)
