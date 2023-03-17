import platform
from pathlib import Path
import tarfile
import zipfile
import os
import sys

PANDOC_VERSION = '3.1.1'

PROCESSOR = 'amd64' if platform.processor() == 'x86_64' else 'arm64'

BASE_URL = f'https://github.com/jgm/pandoc/releases/download/{PANDOC_VERSION}/pandoc-{PANDOC_VERSION}-'

PANDOC_URLS = {
    'Windows': f'{BASE_URL}windows-x86_64.zip',
    'Darwin': f'{BASE_URL}macOS.zip',
    'Linux': f'{BASE_URL}linux-{PROCESSOR}.tar.gz'
}

APPDATA_DIR = Path.joinpath(Path.home(), '.config', 'RuithDesktop') if not platform.system() == 'Windows' \
    else Path(
    os.path.expandvars(r'%LOCALAPPDATA%\RuithDesktop')
)

PANDOC_ARCHIVE_FILE_PATH = Path.joinpath(APPDATA_DIR, (
    'pandoc.tar.gz' if platform.system() == 'Linux' else 'pandoc.zip'
))

PANDOC_PATH = Path.joinpath(APPDATA_DIR, f'pandoc-{PANDOC_VERSION}',
                            'bin', 'pandoc')
if(platform.system() == 'Windows'):
    PANDOC_PATH = Path.joinpath(APPDATA_DIR, f'pandoc-{PANDOC_VERSION}',
                                'pandoc.exe')


def get_pandoc_url():
    return PANDOC_URLS[platform.system()]


def get_pandoc_archive_file_path():
    if not os.path.exists(APPDATA_DIR):
        os.mkdir(APPDATA_DIR)
    return Path.joinpath(PANDOC_ARCHIVE_FILE_PATH)


def extract_pandoc():
    if platform.system() == 'Linux':
        tar = tarfile.TarFile.open(PANDOC_ARCHIVE_FILE_PATH)
        tar.extractall(APPDATA_DIR)
        tar.close()
    else:
        zip = zipfile.ZipFile(PANDOC_ARCHIVE_FILE_PATH)
        zip.extractall(APPDATA_DIR)


def add_pandoc_to_path():
    print(str(PANDOC_PATH))
    sys.path.insert(0, str(PANDOC_PATH))


def setup_pandoc():
    extract_pandoc()
    add_pandoc_to_path()
