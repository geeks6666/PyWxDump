# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         __init__.py.py
# Description:  
# Author:       xaoyaoo
# Date:         2023/10/14
# -------------------------------------------------------------------------------
from .wx_info import BiasAddr, read_info, get_wechat_db, encrypt, batch_decrypt, decrypt
from .wx_info import merge_copy_db, merge_msg_db, merge_media_msg_db, merge_db
from .analyzer.db_parsing import read_img_dat, read_emoji, decompress_CompressContent, read_audio_buf, read_audio, \
    parse_xml_string, read_BytesExtra
from .analyzer import export_csv
from .ui import app_show_chat, get_user_list, export

import os, json

try:
    VERSION_LIST_PATH = os.path.join(os.path.dirname(__file__), "version_list.json")
    with open(VERSION_LIST_PATH, "r", encoding="utf-8") as f:
        VERSION_LIST = json.load(f)
except:
    VERSION_LIST = {}
    VERSION_LIST_PATH = None

__version__ = "2.4.12"
