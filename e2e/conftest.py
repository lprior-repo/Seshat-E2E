import pytest
import subprocess
import os
import time
import requests


@pytest.fixture(scope="session", autouse=True)
def start_server():
    # Allow overriding the SESHAT path for CI or different setups
    seshat_dir = os.environ.get(
        "SESHAT_DIR", os.path.abspath("../../seshat/diagram_tool")
    )

    if not os.path.exists(seshat_dir):
        raise Exception(
            f"Seshat directory not found at {seshat_dir}. Set SESHAT_DIR environment variable to the correct path."
        )

    print(f"Building app from {seshat_dir}...")
    subprocess.run(["dx", "build", "--platform", "web"], cwd=seshat_dir, check=True)

    print("Starting server...")

    # Run dx serve to host the frontend
    server = subprocess.Popen(
        ["dx", "serve", "--platform", "web", "--port", "8082"],
        cwd=seshat_dir,
        env={**os.environ},
    )

    # Wait for server
    for i in range(40):
        try:
            r = requests.get("http://localhost:8082")
            if r.status_code == 200:
                print("Server started!")
                break
        except Exception:
            pass
        time.sleep(1.0)
    else:
        server.kill()
        raise Exception("Server failed to start")

    yield

    print("Killing server...")
    server.kill()
    server.wait()
