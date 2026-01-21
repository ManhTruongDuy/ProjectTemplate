import subprocess
import sys
import os
import getpass


def get_github_username():
    """
    Trả về GitHub username nếu gh có và đã login
    Trả về None nếu không detect được
    """
    try:
        result = subprocess.run(
            ["gh", "api", "user", "--jq", ".login"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            check=True,
        )
        username = result.stdout.strip()
        return username if username else None
    except Exception:
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: create_project.py <project_name>")
        sys.exit(1)

    project = sys.argv[1].strip()
    if not project:
        print("Project name is required")
        sys.exit(1)

    # 1. Detect GitHub username
    github = get_github_username()

    # 2. Fallback nếu không có gh / chưa login
    author = github if github else getpass.getuser()
    github_username = github if github else author

    print(f"[info] author = {author}")
    print(f"[info] github = {github_username}")

    template = r"C:/Users/ManhTD/source/repos/ProjectTemplate/C"
    output = os.getcwd()

    cmd = [
        "cookiecutter",
        template,
        "--no-input",
        "--output-dir",
        output,
        f"project_name={project}",
        f"author={author}",
        f"github_username={github_username}",
    ]

    print("[cookiecutter] creating project...")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
