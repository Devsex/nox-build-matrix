import nox

@nox.session(python=["3.6", "3.7", "3.8", "3.9"])
def multi_version(session):
    pass

@nox.session(python="3.9")
def single_version(session):
    pass

@nox.session(python="3.9")
@nox.parametrize("param", ["a", "b", "c"])
def parametrized(session, param):
    pass