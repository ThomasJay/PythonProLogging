# PythonProLogging

Python Logging example with multiple outputs (File and stdout) with configuration for date/time, message, line number and file name

## logging config

```
logger.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s (Line: %(lineno)d [%(filename)s])",
    level=logger.INFO,
    handlers=[
        logger.FileHandler("myapp.log"),
        logger.StreamHandler(sys.stdout),
    ],
)
```
