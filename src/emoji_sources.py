from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile, Path as ZipPath

from tree_graph import Tree


@dataclass
class EmojiSource:
    size: int
    zip_path: Path
    path_prefix: str = ""
    sep: str = '-'
    uppercase_hex: bool = False
    remove_fe0f: bool = False

    def filter_tree(self, tree: Tree) -> Tree:
        if isinstance(tree, tuple):
            filtered = tuple(filter(lambda x: x not in (None, ()), (self.filter_tree(subtree) for subtree in tree)))
            return filtered[0] if len(filtered) == 1 else filtered
        else:
            return tree if self.get_emoji_zip_path(emoji=tree).exists() else None

    def get_emoji_path(self, emoji: str) -> str:
        if self.remove_fe0f:
            emoji = emoji.replace('\ufe0f', '')
        hex_codepoints = self.sep.join(
            f"{ord(ch):X}" if self.uppercase_hex else f"{ord(ch):x}" for ch in emoji
        )
        return f'{self.path_prefix}{hex_codepoints}.svg'

    def get_emoji_svg(self, emoji: str) -> str:
        return self.get_emoji_zip_path(emoji=emoji).open().read()

    def get_emoji_zip_path(self, emoji) -> ZipPath:
        emoji_path = self.get_emoji_path(emoji=emoji)
        return ZipPath(ZipFile(file=self.zip_path), emoji_path)


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
