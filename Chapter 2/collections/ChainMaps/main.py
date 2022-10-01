from collections import ChainMap

if __name__ == "__main__":
    defaults = {
        "theme": "Default",
        "language": "eng",
        "showIndex": True,
        "showFooter": True,
    }
    cm = ChainMap(defaults)  # Creates a chainmap with th default configuration
    cm2 = cm.new_child({
        "theme": "bluesky",
    })  # creates a new chainmap with a child that overides the parent
    print(cm2["theme"])  # bluesky
    cm2.pop("theme")
    print(cm2["theme"])  # Default
    cm2.maps[0] = {
        "theme": "desert",
        "showIndex": False,
    }  # adds a root context same as new_child
    print(cm2["showIndex"])  # False
    print(cm2.parents)  # return defaults settings
