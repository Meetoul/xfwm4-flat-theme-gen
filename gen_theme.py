BORDER_THICKNESS = 0

ACTIVE_COLORS = {
    '.': '#2A373E',
    '+': '#FFFFFF',
}

CLOSE_PRELIGHT_COLORS = {
    '.': '#FF0000',
    '+': '#FFFFFF',
}

PRELIGHT_COLORS = {
    '.': '#658595',
    '+': '#FFFFFF',
}

INACTIVE_COLORS = {
    '.': '#50505F',
    '+': '#FFFFFF',
}

BORDER_ACTIVE_COLORS = {
    '.': '#FFFFFF'
}

BORDER_INACTIVE_COLORS = {
    '.': '#A9A9A9'
}


CLOSE_PATTERN = ( # 30x20
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '...........++....++...........',
    '...........+++..+++...........',
    '............++++++............',
    '.............++++.............',
    '.............++++.............',
    '............++++++............',
    '...........+++..+++...........',
    '...........++....++...........',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
)

MAXIMIZE_PATTERN = ( # 30x20
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..........++++++++++..........',
    '..........++++++++++..........',
    '..........++++++++++..........',
    '..........++......++..........',
    '..........++......++..........',
    '..........++......++..........',
    '..........++++++++++..........',
    '..........++++++++++..........',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
)

HIDE_PATTERN = ( # 30x20
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '.........++++++++++++.........',
    '.........++++++++++++.........',
    '.........++++++++++++.........',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
    '..............................',
)

assert len(CLOSE_PATTERN) == len(MAXIMIZE_PATTERN) == len(HIDE_PATTERN), \
    "Buttons patterns height must be the same!"

TITLE_HEIGHT = len(CLOSE_PATTERN)

TITLE_PATTERN = tuple('.' for _ in range(TITLE_HEIGHT))

BORDER_PATTERN = tuple('.' * BORDER_THICKNESS for _ in range(BORDER_THICKNESS))

FILES_TO_GENERATE = [
    {
        'name': 'close-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  CLOSE_PATTERN,
    },
    {
        'name': 'close-prelight.xpm',
        'colors': CLOSE_PRELIGHT_COLORS,
        'pattern':  CLOSE_PATTERN,
    },
    {
        'name': 'close-pressed.xpm',
        'colors': CLOSE_PRELIGHT_COLORS,
        'pattern':  CLOSE_PATTERN,
    },
    {
        'name': 'close-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  CLOSE_PATTERN,
    },

    {
        'name': 'maximize-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  MAXIMIZE_PATTERN,
    },
    {
        'name': 'maximize-prelight.xpm',
        'colors': PRELIGHT_COLORS,
        'pattern':  MAXIMIZE_PATTERN,
    },
    {
        'name': 'maximize-pressed.xpm',
        'colors': PRELIGHT_COLORS,
        'pattern':  MAXIMIZE_PATTERN,
    },
    {
        'name': 'maximize-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  MAXIMIZE_PATTERN,
    },

    {
        'name': 'hide-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  HIDE_PATTERN,
    },
    {
        'name': 'hide-prelight.xpm',
        'colors': PRELIGHT_COLORS,
        'pattern':  HIDE_PATTERN,
    },
    {
        'name': 'hide-pressed.xpm',
        'colors': PRELIGHT_COLORS,
        'pattern':  HIDE_PATTERN,
    },
    {
        'name': 'hide-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  HIDE_PATTERN,
    },

    {
        'name': 'title-1-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-1-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-2-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-2-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-3-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-3-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-4-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-4-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-5-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name': 'title-5-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },

    {
        'name':'top-left-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name':'top-left-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name':'top-right-active.xpm',
        'colors': ACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },
    {
        'name':'top-right-inactive.xpm',
        'colors': INACTIVE_COLORS,
        'pattern':  TITLE_PATTERN,
    },

    {
        'name':'right-active.xpm',
        'colors': BORDER_ACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'right-inactive.xpm',
        'colors': BORDER_INACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'bottom-active.xpm',
        'colors': BORDER_ACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'bottom-inactive.xpm',
        'colors': BORDER_INACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'bottom-left-active.xpm',
        'colors': BORDER_ACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'bottom-left-inactive.xpm',
        'colors': BORDER_INACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'bottom-right-active.xpm',
        'colors': BORDER_ACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'bottom-right-inactive.xpm',
        'colors': BORDER_INACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'left-active.xpm',
        'colors': BORDER_ACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
    {
        'name':'left-inactive.xpm',
        'colors': BORDER_INACTIVE_COLORS,
        'pattern':  BORDER_PATTERN,
    },
]

XPM_FILE_FORMAT = '/* XPM */\nstatic char * {}_xpm[] = {{\n"{} {} {} {}",\n{},\n{}}};'

def norm_name(name):
    return name.split('.')[0].replace('-', '_')

def norm_colors(colors):
    return ',\n'.join(['"{} c {}"'.format(k, v) for k, v in colors.items()])

def norm_pattern(pattern):
    return ',\n'.join(['"{}"'.format(line) for line in pattern])

def gen_xpm_file_content(name, colors, pattern, char_per_pixel=1):
    height = len(pattern)
    width = 0 if height == 0 else len(pattern[0])
    colors_num = len(colors)

    name = norm_name(name)
    colors = norm_colors(colors)
    pattern = norm_pattern(pattern)

    return XPM_FILE_FORMAT.format(name,
                                    width,
                                    height,
                                    colors_num,
                                    char_per_pixel,
                                    colors,
                                    pattern)


for xpm_file in FILES_TO_GENERATE:
    xpm_file_content = gen_xpm_file_content(
        xpm_file['name'], xpm_file['colors'], xpm_file['pattern']
    )

    with open(xpm_file['name'], 'w') as f:
        f.write(xpm_file_content)
        f.close()
