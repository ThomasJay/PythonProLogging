import sys
import logging as logger

import mymodule

logger.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s (Line: %(lineno)d [%(filename)s])",
    level=logger.INFO,
    handlers=[
        logger.FileHandler("myapp.log"),
        logger.StreamHandler(sys.stdout),
    ],
)


if __name__ == "__main__":
    logger.info("Hi There")

    mymodule.do_something()

    logger.critical("We're done")
