# Password used to access the website's admin panel
ADMIN_PASSWORD = "heypatell"

# Telegram API_ID and API_HASH obtained from https://my.telegram.org/auth
API_ID = 23032012  # Your Telegram API ID
API_HASH = "5e47a644cc456147dbc79a24511c4dbb"  # Your Telegram API Hash

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = 60  # 1 minute

# Choose whether to use .session files for session persistence or in-memory sessions
USE_SESSION_FILE = True  # Set to False to use in-memory sessions

# List of Telegram bot tokens used for file upload/download operations
BOT_TOKENS = ["6791410591:AAFWTCs74gbqQt8ehLoqhDvA5bkkS0T-Z5o"]
# You can add multiple bot tokens like this: BOT_TOKENS = ["bot_token1", "bot_token2", ...]

# Maximum file size (in bytes) allowed for uploading to Telegram (2GB)
MAX_FILE_SIZE = 1.98 * 1024 * 1024 * 1024  # 2GB

# Chat ID of the Telegram storage channel where files will be stored
STORAGE_CHANNEL = -1002163575017  # Your storage channel's chat ID

# Message ID of a file in the storage channel used for storing database backups
DATABASE_BACKUP_MSG_ID = 123  # Your database backup message ID

# Database backup interval in seconds. Backups will be sent to the storage channel at this interval
DATABASE_BACKUP_TIME = 60  # 1 minute
