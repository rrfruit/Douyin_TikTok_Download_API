# ==============================================================================
# Copyright (C) 2021 Evil0ctal
#
# This file is part of the Douyin_TikTok_Download_API project.
#
# This project is licensed under the Apache License 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# 　　　　 　　  ＿＿
# 　　　 　　 ／＞　　フ
# 　　　 　　| 　_　 _ l
# 　 　　 　／` ミ＿xノ
# 　　 　 /　　　 　 |       Feed me Stars ⭐ ️
# 　　　 /　 ヽ　　 ﾉ
# 　 　 │　　|　|　|
# 　／￣|　　 |　|　|
# 　| (￣ヽ＿_ヽ_)__)
# 　＼二つ
# ==============================================================================
#
# Contributor Link, Thanks for your contribution:
# - https://github.com/Evil0ctal
# - https://github.com/Johnserf-Seed
# - https://github.com/Evil0ctal/Douyin_TikTok_Download_API/graphs/contributors
#
# ==============================================================================

import sys
import os

# 将项目目录下的 python 文件夹添加到 Python 路径中，以便找到本地安装的依赖
project_root = os.path.dirname(os.path.abspath(__file__))
python_lib_path = os.path.join(project_root, 'python')
if os.path.exists(python_lib_path):
    # 将 python 目录添加到 sys.path 的最前面，优先使用本地依赖
    sys.path.insert(0, python_lib_path)

from app.main import Host_IP, Host_Port
import uvicorn

if __name__ == '__main__':
    uvicorn.run('app.main:app', host=Host_IP, port=Host_Port, reload=True, log_level="info")
