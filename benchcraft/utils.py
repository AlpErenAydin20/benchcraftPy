def format_bytes(bytes_count):
    if bytes_count > 1024*1024:
        mb_format = bytes_count / (1024*1024)
        return f"{mb_format:.2f} MB"

    elif bytes_count > 1024:
        kb_format = bytes_count / 1024
        return f"{kb_format:.2f} KB"

    else: return f"{bytes_count} B"
