ROOT = pathlib.Path(__file__).resolve().parent

# Modal storage support
MODAL_STORAGE_ROOT = pathlib.Path(
    os.environ.get("MODAL_STORAGE_ROOT", str(ROOT))
).resolve()

MODELS = Path(os.environ.get("MODAL_MODELS_DIR", "/mnt/krea2-models"))

# Keep all generated files under the configured storage root so the same
# Modal volume can be reused across notebook/app runs.
INPUT = MODAL_STORAGE_ROOT / "input"
OUTPUT = MODAL_STORAGE_ROOT / "output"
CUSTOM_NODES = MODAL_STORAGE_ROOT / "custom_nodes"

# Keep a local ComfyUI folder for code, but pin data paths to the Modal volume.
# This allows the app to still call the same generation logic without storing
# generated content on ephemeral disk.
