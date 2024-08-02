import logging

from django.core.cache import cache


logger = logging.getLogger("main")
CACHE_TTL = 60 * 60 * 2  # 2 hours


def delete_cache(key_prefix: str) -> None:
    try:
        cache.delete_pattern(f"*{key_prefix}*")  # type: ignore[attr-defined]
        logger.debug("Cache with key prefix %s deleted", key_prefix)
    except AttributeError:
        logger.warning(
            "Skipping cache deletion for key prefix %s in test environment",
            key_prefix,
        )
