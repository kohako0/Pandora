MODEL_PATH = r"D:\barozp\Qwen3.6-28B-REAP20-A3B-GGUF\Qwen3.6-28B-REAP20-A3B-Q4_K_S.gguf"
CONTEXT_SIZE = 64000

LLAMA_SETTINGS = {
    "model_path": MODEL_PATH,
    "n_ctx": CONTEXT_SIZE,
    "n_batch": 2048,
    "n_ubatch": 1024,
    "n_gpu_layers": 99,
    "use_mmap": True,
    "use_mlock": True,
    "n_threads": 3,
    "n_threads_batch": 3,
    "verbose": True,
    "logits_all": False,
    "thinking": False
}