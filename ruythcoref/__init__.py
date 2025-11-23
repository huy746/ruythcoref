__version__ = "1.0.0"
__author__ = "ruythbot_huy"

from .advanced_file_converter import AdvancedFileConverter

def convert(src_path, dest_path):
    """Hàm tiện lợi để chuyển đổi file"""
    return AdvancedFileConverter.convert(src_path, dest_path)

__all__ = ["convert", "AdvancedFileConverter"]
