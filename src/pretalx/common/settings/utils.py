def log_initial(*, debug, config_files, db_name, db_backend, LOG_DIR, plugins):
    from pretalx.common.console import start_box, end_box, print_line
    from pretalx import __version__

    mode = 'development' if debug else 'production'
    lines = [
        ('This is pretalx v{} calling, running in {mode} mode.'.format(__version__), True),
        ('', False),
        ('Settings:', True),
        ('Read from: {}'.format(", ".join(config_files)), False),
        ('Database:  {} ({})'.format(db_name, db_backend), False),
        ('Logging:   {}'.format(LOG_DIR), False),
    ]
    if plugins:
        lines += [('Plugins:   {}'.format(','.join(plugins)), False)]
    else:
        lines += [('', False)]
    image = '''
┏━━━━━━━━━━┓
┃  ┌─·──╮  ┃
┃  │  O │  ┃
┃  │ ┌──╯  ┃
┃  └─┘     ┃
┗━━━┯━┯━━━━┛
    ╰─╯
    '''.strip().split(
        '\n'
    )
    img_width = len(image[0])
    image[-1] += ' ' * (img_width - len(image[-1]))
    image += [' ' * img_width for _ in range((len(lines) - len(image)))]

    lines = [('{}  {}'.format(image[n], lines[n][0]), lines[n][1]) for n in range(len(lines))]

    size = max(len(line[0]) for line in lines) + 4
    start_box(size)
    for line in lines:
        print_line(line[0], box=True, bold=line[1], size=size)
    end_box(size)


def reduce_dict(data):
    return {
        section_name: {
            key: value for key, value in section_content.items() if value is not None
        }
        for section_name, section_content in data.items()
    }
