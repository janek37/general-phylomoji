from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile


@dataclass
class EmojiSource:
    size: int
    zip_path: Path
    path_prefix: str = ""
    sep: str = '-'
    uppercase_hex: bool = False
    remove_fe0f: bool = False

    def get_emoji_path(self, emoji: str) -> str:
        if self.remove_fe0f:
            emoji = emoji.replace('\ufe0f', '')
        hex_codepoints = self.sep.join(
            f"{ord(ch):X}" if self.uppercase_hex else f"{ord(ch):x}" for ch in emoji
        )
        return f'{self.path_prefix}{hex_codepoints}.svg'

    def get_emoji_svg(self, emoji: str) -> str:
        emoji_path = self.get_emoji_path(emoji=emoji)
        with ZipFile(file=self.zip_path) as zip_file:
            with zip_file.open(emoji_path) as emoji_file:
                return emoji_file.read().decode()


NOTO_EMOJI = EmojiSource(
    size=128,
    path_prefix='noto-emoji-main/svg/emoji_u',
    zip_path=Path('./svg-sets/noto-emoji-main.zip'),
    sep='_',
    remove_fe0f=True,
)

OPENMOJI = EmojiSource(
    size=72,
    zip_path=Path('./svg-sets/openmoji-svg-color.zip'),
    uppercase_hex=True,
)

TWEMOJI = EmojiSource(
    size=36,
    zip_path=Path('./svg-sets/twemoji-color-font-main.zip'),
    path_prefix='twemoji-color-font-main/assets/twemoji-svg/',
)
