
import string
from re import sub
from APP.config import letter_subs, chars_replace, max_message_len

async def fix_message(message):
    for k,v in letter_subs.items():
        message = message.replace(k,v)
    return message

async def sanitize_name(message):
    if len(message) > max_message_len:
        message = message[-max_message_len:]
    # Using the last part of the message because this is used to sanitize file names and it will remove the extension.
    # if you use the first part; so we would need to account for that if we want to use the first part.
    message = sub(r'[,…<>:"/\\|?*\n]', '', message)
    message = message.replace("..","")
    if message.endswith('.'):
        message = message.replace('.','')
    message = message.strip()
    message = await sanitize_patch(message)
    return message

async def sanitize_patch(filename):
    # Replace invalid characters with underscores
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_filename = ''.join(c if c in valid_chars else '_' for c in filename)
    return sanitized_filename