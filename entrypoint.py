import importlib.util
import json
import sys
from argparse import Namespace

from nox import manifest, registry

spec = importlib.util.spec_from_file_location("Noxfile", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

manifest_obj = manifest.Manifest(
    registry.get(),
    Namespace(
        force_venv_backend=False,
        default_venv_backend="virtualenv",
        extra_pythons=[],
        posargs=[],
    ),
)
if sys.argv[2]:
    manifest_obj.filter_by_keywords(sys.argv[2])

session_list = [
    session.friendly_name
    for (session, selected) in manifest_obj.list_all_sessions()
    if selected
]

print(f"::set-output name=matrix::{json.dumps(session_list)}")
