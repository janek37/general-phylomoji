CARNIVORANS = (
    (
        (('🐕', '🐺'), '🦊'),
        (((('🦝', '🦨'), ('🦦', '🦡')), '🦭'), (('🐻', '🐻‍❄️'), '🐼'))
    ),
    ('🐈', (('🦁', '🐆'), '🐅'))
)

UNGULATA = (
    (('🐎', '🦓'), '🦏'),
    (
        (
            (
                (('🦌', ((('🦬', '🐄'), '🐃'), ('🐑', '🐐'))), '🦒'),
                ('🦛', ('🐋', '🐬'))
            ),
            ('🐖', '🐗')
        ),
        (('🐪', '🐫'), '🦙')
    )
)

PRIMATES = ('🐒', (('🦍', '🧍'), '🦧'))

RODENTS = (((('🐁', '🐀'), '🐹'), '🦫'), '🐿')

MAMMALS = (
    (
        (
            (((CARNIVORANS, UNGULATA), '🦇'), '🦔'),
            (PRIMATES, (RODENTS, '🐇'))
        ),
        (('🐘', '🦣'), '🦥')
    ),
    ('🐨', '🦘')
)

BIRDS = (
    (('🦃', ('🐓', '🦚')), ('🦆', '🦢')),
    (('🕊', '🦤'), ('🐧', ('🦅', '🦉', ('🦜', '🐦'))), '🦩'),
)


REPTILES = (((((BIRDS, '🦖'), '🦕'), '🐊'), '🐢'), ('🦎', '🐍'))

INSECTS = (((('🦋', ('🦟', '🪰')), ('🐜', '🐝')), ('🪲', '🐞')), ('🦗', '🪳'))

ARTHROPODS = ((INSECTS, (('🦀', '🦞'), '🦐')), ('🕷', '🦂'))

ANIMALS = (
    (
        ((((MAMMALS, REPTILES), '🐸'), ('🐟', '🐠', '🐡')), '🦈'),
        (ARTHROPODS, ((('🦑', '🐙'), '🐌', '🦪'), '🪱'))
    ),
    '🧽'
)

ROSACEAE = ((('🍑', '🍒'), ('🍎', '🍐')), ('🌹','🍓'))

FABIDS = (((ROSACEAE, '🍺'), (((('🍈', '🥒'), '🍉'), '🎃'), '🌰')), ('🥜', '☘'))

MALVIDS = (((('🍊', '🍋'), '🍁'), '🥭'), (('🍫', '🌺'), '🥦'))

ROSIDS = ((FABIDS, MALVIDS), '🍇')

LAMIIDS = ((((((('🍅', '🥔'), '🍆'), ('🌶', '🫑')), '🚬'), '🍠'), '🫒'), '☕')

ASTERIDS = ((LAMIIDS, ((('🌻', '🌼'), '🥕'), '🧉')), (('🥝', '🫐'), '🍵'))

EUDICOTS = (ROSIDS, (ASTERIDS, '🌵'))

MONOCOTS = ((((((('🎋', '🌾'), '🌽'), '🍍'), '🍌'), '🌴'), ('🧄', '🧅')), '🌷')

PLANTS = (((EUDICOTS, MONOCOTS), '🥑'), '🌲')

LIFE_EMOJI = ('🦠', ((ANIMALS, '🍄'), PLANTS))
