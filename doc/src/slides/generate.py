from __future__ import print_function
# NOTE: This is a program used to test all slides styles in all combinations.
# Fine for new slide environments, but optimal combinations are what
# a user needs, not all combinations.
# The recommended combinations of styles for slides are autogenerated by
# doconce slides_html file all

import os, shutil, sys

def system(cmd):
    print(cmd)
    failure = os.system(cmd)
    if failure:
        print('could not run', cmd)
        sys.exit(1)

from collections import OrderedDict as dict
themes = dict(
    reveal=['beige', 'beigesmall', 'blood', 'darkgray', 'moon',
            'night', 'serif', 'simple', 'sky', 'solarized'],
    deck=['neon', 'swiss','web-2.0', 'mnml', 'sandstone.aurora',
          'sandstone.dark', 'sandstone.default', 'sandstone.firefox',
          'sandstone.light', 'sandstone.mdn', 'sandstone.nightly',
          'beamer'],
    csss=['csss_default'],
    dzslides=['dzslides_default'],
    )

dark_styles = ['csss_default',
               'night', 'moon',
               'neon', 'sandstone.aurora', 'sandstone.dark',
               'sandstone.mdn', 'sandstone.nightly']
dark_pygments=['monokai', 'fruity', 'native']
light_pygments = ['default', 'manni', 'autumn', 'perldoc', 'emacs']

system('sh clean.sh')

def generate(name, many_pygments=False):
    for slide_system in themes:
        for theme in themes[slide_system]:
            if theme in dark_styles:
                pygm_styles = dark_pygments
            else:
                pygm_styles = light_pygments
            if not many_pygments:
                pygm_styles = pygm_styles[:1]

            pygm_styles += ['none']  # plain <pre> too for code
            for pygm_style in pygm_styles:
                shutil.copy('%s.do.txt' % name, 'tmp1.do.txt')
                system('doconce format html tmp1 --pygments-html-style=%s' %
                       (pygm_style))
                system('doconce slides_html tmp1 %s --html-slide-theme=%s' %
                       (slide_system, theme))
                shutil.copy('tmp1.html', '%s_%s_%s_%s.html' %
                            (name, slide_system, theme, pygm_style))
            #sys.exit(0)

generate('demo', True)
