from package.module import ModuleClass


class TestMyClass:
    """
    Docstring for this test.
    """

    def test_something(self) -> None:
        module_class = ModuleClass()
        assert module_class.function() == "python-tox-template"
