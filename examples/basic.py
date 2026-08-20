"""Minimal example for LandingSplit."""

from landingsplit import landingsplit


def main():
 runner = landingsplit({"name": "LandingSplit", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()