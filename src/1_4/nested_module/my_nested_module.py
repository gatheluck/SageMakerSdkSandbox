def version_check(module) -> None:  # type: ignore
    print("my_nested_module.version_check is called.")
    print(f" {module.__name__} version is {module.__version__}")
    return None
