import subprocess
import sys


def ensure_setuptools():
    try:
        import pkg_resources
    except ImportError:
        print("Installing setuptools...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'setuptools'])
    finally:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-e', '.'])
        except subprocess.CalledProcessError as e:
            print("Error while running setup.py:", e)


if __name__ == "__main__":
    ensure_setuptools()
