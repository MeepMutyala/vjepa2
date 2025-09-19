# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages
import os

NAME = "vjepa2"
VERSION = "0.0.1"
DESCRIPTION = "PyTorch code and models for V-JEPA 2."
URL = "https://github.com/facebookresearch/vjepa2"


def get_requirements():
    reqs = []
    reqs_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(reqs_path):
        with open(reqs_path, "r", encoding="utf-8") as f:
            reqs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return reqs


if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        url=URL,
        python_requires=">=3.11",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=get_requirements(),
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
    )
