from datetime import datetime
import pathlib
import os

build_time = datetime.now()
commit_sha = os.getenv('CF_PAGES_COMMIT_SHA', 'Error')
branch = os.getenv('CF_PAGES_BRANCH', 'Error')
file_path = pathlib.Path("index.html")
content = file_path.read_text(encoding="utf-8")
content = content.replace("latiao_build_time", build_time)
content = content.replace("latiao_commit_sha", commit_sha)
content = content.replace("latiao_branch", branch)
file_path.write_text(content, encoding="utf-8")

print(build_time,commit_sha,branch)