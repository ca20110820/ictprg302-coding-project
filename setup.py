from setuptools import find_packages, setup

setup(
    name="wordle",
    version="0.1.0",
    description="ICTPRG302 - Coding Project",
    author="Cedric Anover",
    packages=find_packages(),
    data_files=[
        ('wordle/word-bank', ['word-bank/all_words.txt', 'word-bank/target_words.txt'])
    ],
    install_requires=[
        "pytermgui"
    ],
    setup_requires=[
        'setuptools'
    ],
    entry_points={
        "console_scripts": [
            "wordle = wordle.main:main",
            "wordle_ptg = wordle_ptg.main:main"
        ],
    },
    python_requires=">=3.10"
)
