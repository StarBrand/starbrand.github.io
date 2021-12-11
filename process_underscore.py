import os
import sys
import logging


def replace_underscores(path: str) -> None:
    logging.debug("Working on {}".format(path))
    if os.path.isdir(path):
        for subpath in os.listdir(path):
            replace_underscores(os.path.join(path, subpath))
    else:
        if path.split(".")[-1] == "html":
            logging.info("Modifying {}...".format(path))
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            content = content.replace("_static", "static")
            content = content.replace("_modules", "modules")
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)
        else:
            logging.debug("Not an html file")
    return


if __name__ == "__main__":
    try:
        if sys.argv[2] == "info":
            logging.basicConfig(level=logging.INFO)
        elif sys.argv[2] == "debug":
            logging.basicConfig(level=logging.DEBUG)
        else:
            print("Not identify second argument", file=sys.stderr)
    except IndexError:
        logging.basicConfig(level=logging.INFO)
    logging.info("Running replacing undercore reference...")
    try:
        replace_underscores(sys.argv[1])
    except:
        raise RuntimeError("Path must be passed")
